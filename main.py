# A simple blockchain which represents a fictional cryptocurrency in Python
import hashlib


class HaoChainBlock:
    def __init__(self, prev_block_hash, transaction_list):
        self.prev_block_hash = prev_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + prev_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Lee sends 2 HC to Wong"
t2 = "Jack sends 4.5 HC to Louis"
t3 = "Bob sends 3 HC to Wong"
t4 = "Mike sends 6 HC to Wong"
t5 = "Lee sends 1.2 HC to Wong"
t6 = "Jack sends 4.4 HC to Wong"

initial_block = HaoChainBlock("Initial String", [t1, t2])

print(initial_block.block_hash)
print(initial_block.block_data)

second_block = HaoChainBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_hash)
print(second_block.block_data)

third_block = HaoChainBlock(initial_block.block_hash, [t5, t6])

print(third_block.block_hash)
print(third_block.block_data)


