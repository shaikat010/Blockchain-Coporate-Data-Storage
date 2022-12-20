from Blockchain_Structure import *

# Testing the created class
# using the following commands
Main_Chain = Blockchain()
Validity = Main_Chain.chain_valid(Main_Chain.chain)
print(f'This is the validity status of the main chain : {Validity}')


# Printing the data
# in the blocks individually
data = Main_Chain.chain
for i in data:
    print(i)

# Getting the last block in the chain
print(f"This is the previous block {Main_Chain.print_last_block()}")

# Getting the length of the chain
# This is also called chain height
print(f" This is the height or the length of the chain: {Main_Chain.get_chain_height()}")


mine_block(Main_Chain)
print(f" This is the height or the length of the chain: {Main_Chain.get_chain_height()}")

mine_block(Main_Chain)
print(f" This is the height or the length of the chain: {Main_Chain.get_chain_height()}")
print(f" This is the main chain: " + str(Main_Chain.chain))


Validity = Main_Chain.chain_valid(Main_Chain.chain)
print(f'This is the validity status of the main chain : {Validity}')

# Printing the data
# in the blocks individually
data = Main_Chain.chain
for i in data:
    print(i)


# Checking the validity of the chain
Validity = Main_Chain.chain_valid(Main_Chain.chain)
print(f'This is the validity status of the main chain : {Validity}')
