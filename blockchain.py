import hashlib
import time
import json


class Transaction:
    def __init__(self, from_addr, to_addr, amount):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount


class Block:
    def __init__(self, timestamp, transactions, prior_hash=''):
        self.timestamp = timestamp
        self.transactions = transactions
        self.prior_hash = prior_hash
        self.nonce = 0
        self.hash = self.create_hash()

    def create_hash(self):
        block_string = (str(self.prior_hash) + str(self.timestamp) +
                        str(self.transactions) + str(self.nonce)).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        target = '000'
        start_time = time.time()
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.create_hash()
        end_time = time.time()
        print(f"Block mined! Nonce: {self.nonce}, Hash: {self.hash}")
        print((f"Time taken to mine block: {end_time - start_time}"))


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 3
        self.pending_transactions = []
        self.mining_reward = 10

    def create_genesis_block(self):
        genesis_block = Block(time.time(), [], "0")
        genesis_block.hash = ""
        return genesis_block

    def get_last_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address):
        block = Block(time.time(), self.pending_transactions, self.get_last_block().hash)
        block.mine_block(self.difficulty)

        self.chain.append(block)

        self.pending_transactions = [Transaction(None, mining_reward_address, self.mining_reward)]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance_of_address(self, address):
        balance = 0

        for block in self.chain:
            for transaction in block.transactions:
                if transaction.from_addr == address:
                    balance -= transaction.amount
                if transaction.to_addr == address:
                    balance += transaction.amount

        return balance

    def is_bc_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.create_hash():
                return False

            if current_block.prior_hash != previous_block.hash:
                return False

        return True


# %%%%%%%%%% EXAMPLE USAGE %%%%%%%%%%
if __name__ == "__main__":
    # Blockchain initiation
    crypto_coin = Blockchain()

    # Creating 2 transactions in the first block
    crypto_coin.create_transaction(Transaction('address1', 'address2', 75))
    crypto_coin.create_transaction(Transaction('address3', 'address4', 25))

    # Block mining
    print("Mining first block: ")
    crypto_coin.mine_pending_transactions('miner-address')
    print(f"\nBalance of miner's wallet: {crypto_coin.get_balance_of_address('miner-address')}")

    # Creating 3 transactions in the second block
    crypto_coin.create_transaction(Transaction('address5', 'address6', 100))
    crypto_coin.create_transaction(Transaction('address7', 'address8', 10))
    crypto_coin.create_transaction(Transaction('address9', 'address10', 50))

    print("\nMining second block: ")
    crypto_coin.mine_pending_transactions('miner-address')
    print(f"\nBalance of miner's wallet after second mining: {crypto_coin.get_balance_of_address('miner-address')}")

    print("\nMining third block: ")
    crypto_coin.mine_pending_transactions('miner-address')
    print(f"\nBalance of miner's wallet after third mining: {crypto_coin.get_balance_of_address('miner-address')}")

    # Writing the output to json file
    with open("blockchain_output.json", 'w') as file:
        json.dump(crypto_coin.chain, file, default=lambda o: o.__dict__, indent=4)
