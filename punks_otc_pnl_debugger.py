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

def fetch_transactions(address):
    """Fetch transactions using Etherscan API with detailed debugging."""
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': address,
        'startblock': 0,
        'endblock': 99999999,
        'sort': 'asc',
        'apikey': ETHERSCAN_API_KEY
    }
    response = requests.get("https://api.etherscan.io/api", params=params)
    transactions = response.json().get('result', [])
    if transactions:
        print(f"First transaction date: {transactions[0]['timeStamp']}, Last transaction date: {transactions[-1]['timeStamp']}")
    else:
        print("No transactions found.")
    return transactions

def main():
    web3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}"))
    if web3.is_connected():
        print("Connected to Ethereum network")
    else:
        print("Failed to connect to Ethereum network")
        return

    address = input("Enter the Ethereum address to fetch transactions: ")
    transactions = fetch_transactions(address)
    # Continue with transaction analysis or other operations

if __name__ == "__main__":
    main()
