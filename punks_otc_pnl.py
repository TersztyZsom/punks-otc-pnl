import requests
import pandas as pd
from datetime import datetime, timezone
from web3 import Web3
from decimal import Decimal
import os

# Constants
ETHERSCAN_API_KEY = 'A31U76N2SZNJSRBCXFUH8NPS3ADABYCFWT'
INFURA_PROJECT_ID = 'fc3f2e17f2a049e2a421c0164e0534c6'
CRYPTOPUNKS_CONTRACT = '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=EUR,HUF"

def create_infura_url():
    infura_project_id = input("Enter your Infura Project ID (default is pre-filled): ") or INFURA_PROJECT_ID
    return f"https://mainnet.infura.io/v3/{infura_project_id}"

def connect_to_ethereum(infura_url):
    web3 = Web3(Web3.HTTPProvider(infura_url))
    if not web3.is_connected():
        print("Connection failed. Check your Infura URL.")
        exit(1)
    return web3

def check_latest_block(web3):
    latest_block = web3.eth.block_number
    print(f"Current latest block on the network: {latest_block}")
    return latest_block

def get_eth_price_in_fiat():
    response = requests.get(COINGECKO_API_URL)
    data = response.json()
    return Decimal(data['ethereum']['eur']), Decimal(data['ethereum']['huf'])

def fetch_transactions(address, web3):
    current_block = check_latest_block(web3)
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': address,
        'startblock': 0,
        'endblock': current_block,  # Ensure fetching up to the most recent block
        'sort': 'asc',
        'apikey': ETHERSCAN_API_KEY
    }
    response = requests.get("https://api.etherscan.io/api", params=params)
    transactions = response.json().get('result', [])
    if not transactions:
        print("No new transactions found or node may be out of sync.")
    return transactions

def analyze_transactions(transactions):
    eur, huf = get_eth_price_in_fiat()
    data = []
    for tx in transactions:
        if tx['to'].lower() == CRYPTOPUNKS_CONTRACT.lower() or tx['from'].lower() == CRYPTOPUNKS_CONTRACT.lower():
            direction = 'Buy' if tx['to'].lower() == CRYPTOPUNKS_CONTRACT.lower() else 'Sell'
            dt = datetime.fromtimestamp(int(tx['timeStamp']), timezone.utc)
            eth_price = Decimal(Web3.from_wei(int(tx['value']), 'ether'))
            data.append({
                'Date': dt.strftime('%Y-%m-%d %H:%M:%S'),
                'From': tx['from'],
                'To': tx['to'],
                'Value ETH': eth_price,
                'EUR Price': (eth_price * eur).quantize(Decimal('0.01')),
                'HUF Price': (eth_price * huf).quantize(Decimal('0.01')),
                'Transaction Hash': tx['hash'],
                'Direction': direction
            })
    return pd.DataFrame(data)

def calculate_pnl(data):
    data['MonthYear'] = pd.to_datetime(data['Date']).dt.to_period('M')
    monthly_pnl = data.groupby('MonthYear').agg({'Value ETH': 'sum', 'EUR Price': 'sum', 'HUF Price': 'sum'})
    yearly_pnl = data.groupby(pd.to_datetime(data['Date']).dt.to_period('Y')).agg({'Value ETH': 'sum', 'EUR Price': 'sum', 'HUF Price': 'sum'})
    return monthly_pnl, yearly_pnl

def export_to_excel(data, monthly_pnl, yearly_pnl, filename="CryptoPunks_Transactions.xlsx"):
    desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
    file_path = os.path.join(desktop_path, filename)
    with pd.ExcelWriter(file_path) as writer:
        data.to_excel(writer, sheet_name='Transactions', index=False)
        monthly_pnl.to_excel(writer, sheet_name='Monthly PnL')
        yearly_pnl.to_excel(writer, sheet_name='Yearly PnL')
    print(f"Data exported to {file_path}")

def main():
    infura_url = create_infura_url()
    web3 = connect_to_ethereum(infura_url)
    address = input("Enter the Ethereum address to fetch transactions: ")
    transactions = fetch_transactions(address, web3)
    analyzed_data = analyze_transactions(transactions)
    monthly_pnl, yearly_pnl = calculate_pnl(analyzed_data)
    export_to_excel(analyzed_data, monthly_pnl, yearly_pnl)

if __name__ == "__main__":
    main()
