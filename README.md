# Blockchain Simulation

## Overview

This project is a simple blockchain simulation written in Python. It includes basic functionalities such as transaction handling, block mining, and chain validation. The implementation uses SHA-256 hashing to secure the blockchain.

## Features

- **Transaction Management**: Supports creating and processing transactions.
- **Block Mining**: Implements proof-of-work (PoW) with adjustable difficulty.
- **Blockchain Integrity Check**: Validates the blockchain by verifying hashes.
- **Mining Reward System**: Rewards miners for successfully mining blocks.
- **Balance Calculation**: Tracks balances of different addresses.

## Installation

1. Ensure you have Python installed (>=3.6 recommended).
2. Clone this repository or download the script.
3. Install required dependencies (if any).

## Usage

1. Run the script:
   ```bash
   python blockchain.py
   ```
2. The script will:
   - Create a blockchain instance.
   - Add transactions.
   - Mine blocks.
   - Display balances of addresses.
   - Save the blockchain data to `blockchain_output.json`.

## Code Structure

- `Transaction`: Represents a transaction with sender, receiver, and amount.
- `Block`: Represents a block containing transactions and a hash.
- `Blockchain`: Manages the chain, mining process, and transaction handling.

## Example Output

```
Mining first block:
Block mined! Nonce: 23456, Hash: 000abc...
Balance of miner's wallet: 10
...

```
## License

This project is open-source and available under the MIT License.

