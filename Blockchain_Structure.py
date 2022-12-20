# For timestamp
import datetime

# Calculating the hash for the blocks
# fingerprints to the blocks is added as it is the hash number
import hashlib

# To store data
# in our blockchain in the JSON object
import json


class Blockchain:

    # This function is created
    # to create the first or the genesis block and set its hash to "0"
    def __init__(self):
        self.chain = []
        # Creates a genesis block whenever the blockchain instance is created
        self.create_block(proof=1, previous_hash='0')

    # This function is created
    # to add more blocks into the chain
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    # This function is created to give us the previous block
    # or the last block in the chain
    def print_last_block(self):
        return self.chain[-1]

    # This function is created to give us the first block or the genesis
    # block in the chain
    def print_genesis_block(self):
        return self.chain[0]

    # This function is created to give us the first block or the genesis
    # block in the chain
    def get_chain_height(self):
        return len(self.chain)

    # This is the function for proof of work
    # and used to successfully mine the block
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            # This is the calculation of the hashing using the SHA256 hashing algorithm
            hash_operation = hashlib.sha256(str(new_proof ** 2 + previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                print("This is the hash operation:" + str(hash_operation))
                new_proof += 1

        # Checking the right hash number that is calculated
        print("This is the right hash: " + str(hash_operation))
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
        # Print the full chain using the following command
        # print(f"This is the chain {chain}")
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            # This if condition will invalidate the chain if the previous hash value of a block
            # does to match the previous block's hash value
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']

            hash_operation = hashlib.sha256(
                str(proof ** 2 + previous_proof ** 2).encode()).hexdigest()

            if hash_operation[:5] != '00000':
                return False

            previous_block = block
            block_index += 1

            print("This is the right hash" + str(hash_operation))
        return True


# This is the code for the
# mining of the block
def mine_block(blockchain):
    previous_block = blockchain.print_last_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
