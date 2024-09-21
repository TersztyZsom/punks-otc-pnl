
#Punks_otc_pnl

## Overview
This Python application leverages the Web3.py library to interact with the Ethereum blockchain via the Infura API. 
It's designed to fetch and analyze transactions related to the CryptoPunks smart contract, providing financial insights 
such as profit and loss calculations in both EUR and HUF currencies.

## Features
- Connect to Ethereum mainnet using Infura.
- Fetch transactions for any Ethereum address.
- Analyze transactions to determine buys and sells of CryptoPunks.
- Calculate and display Profit & Loss in both EUR and HUF.
- Export transaction data and P&L reports to Excel.

## Installation

### Prerequisites
- Python 3.6 or newer
- pip
- Virtual environment (recommended)

### Libraries
Use the following command to install the required libraries:
```bash
pip install pandas requests web3 python-decimal os
```

### Setup
1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```
2. Navigate into the project directory:
   ```bash
   cd ethereum-transactions-analyzer
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Update the `ETHERSCAN_API_KEY` and `INFURA_PROJECT_ID` in the script to match your API keys. You may need to create accounts 
on Etherscan and Infura if you don't already have them.

## Usage
Run the script from the command line:
```bash
python analyzer.py
```
Follow the interactive prompts to enter your Infura Project ID and the Ethereum address for which you want to fetch transactions.

## Output
The results are exported to an Excel file named `CryptoPunks_Transactions.xlsx` on your desktop, containing detailed 
transaction data, monthly P&L, and yearly P&L sheets.

## Contributing
Contributions are welcome. Please open an issue first to discuss what you would like to change.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Debugger for Punks_otc_pnl


# Ethereum Transaction Fetcher

## Overview
This Python script facilitates the interaction with the Ethereum blockchain by fetching transaction histories for specified Ethereum addresses. 
It uses the Etherscan API to retrieve transactions and the Web3.py library to connect to the Ethereum network via Infura.

## Features
- Fetch Ethereum transaction history for any specified address.
- Display the date of the first and last transaction.
- Connection to Ethereum network using Infura.
- Detailed output for debugging and transaction analysis.

## Installation

### Prerequisites
- Python 3.6 or newer.
- An active Internet connection.
- API keys for both Infura and Etherscan.

### Dependencies
Install the required libraries using the following command:
```bash
pip install requests pandas web3
```

### Setup
1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```
2. Navigate to the project directory:
   ```bash
   cd ethereum-transaction-fetcher
   ```

## Configuration
Before running the script, ensure you have set your Etherscan and Infura API keys in the script:
- `ETHERSCAN_API_KEY`
- `INFURA_PROJECT_ID`

## Usage
To run the script, use the following command in the terminal:
```bash
python fetch_transactions.py
```
Follow the interactive prompts to enter the Ethereum address you wish to analyze.

## Output
The script will print details of the transactions found, including the timestamps of the first and last transactions, directly to the console.

## Contributing
Feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
