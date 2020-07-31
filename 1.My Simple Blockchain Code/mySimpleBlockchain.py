# Module 1 - Create a Blockchain
 
# To be installed:
# Flask==0.12.2: pip install Flask==0.12.2
# Postman HTTP Client: https://www.getpostman.com/
 
# Importing the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify
 
# Part 1 - Building a Blockchain
 
class Blockchain:
 
    def __init__(self):
# Initialize list for containing different blocks
        self.chain = []
# Creation of Genesis Block i.e First block of blockchain
        self.create_block(proof = 1, previous_hash = '0')
# Now we will append different blocks that will be mined together in the empty list
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
# Getting the last block of current chain
    def get_previous_block(self):
        return self.chain[-1]
# Defining PoW for miners to solve
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':# Number of leading zeros increase hardness of problem for miners to solve
                check_proof = True
            else:
                new_proof += 1
        return new_proof
  
# Checking if everything is right in blockchain. I.e check for PoW and if prev_hash= hash of previous block
# Creation of Hash function  
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
 
# Part 2 - Mining our Blockchain
 
# Creating a Web App
app = Flask(__name__)
 
# Creating a Blockchain
blockchain = Blockchain()
 
# Mining a new block
# route() decorator to tell Flask that what URL should trigger our function
@app.route('/mine_block', methods = ['GET'])
def mine_block():
# Getting the Proof of work function
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
# Call create block function to append the newly mined block
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations Sonu, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200
 
# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200
 
# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good Sonu. The Blockchain is valid.'}
    else:
        response = {'message': 'Sonu, we have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200
 
# Running the app
app.run(host = '0.0.0.0', port = 5000)
 
