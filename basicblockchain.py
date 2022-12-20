import hashlib

class CoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "----" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "bob send to alice HC"
t2 = "alice send to bob 2.5 HC"
t3 = "mike send to bob 4.5 HC"
t4 = "bob send to alice  4.5 HC"

initial_hash = hashlib.sha256("initial_hash".encode()).hexdigest()
initial_block = CoinBlock(initial_hash, [t1,t2])
second_block = CoinBlock(initial_block.block_hash, [t2,t3])
third_block = CoinBlock(second_block.block_hash, [t3,t4])

print(initial_block.block_data)
print(second_block.block_data)
print(third_block.block_data)