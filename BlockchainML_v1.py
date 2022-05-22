#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Last Updated : 19 Feb, 2022

@author: Abhishek Tiwari, Simran Arora, Nikunj, Punam
https://www.geeksforgeeks.org/create-simple-blockchain-using-python/

"""
'''
Extended and modified from BlockchainML_v0.py to suit only custom frameworks
'''
# Python program to create Blockchain

import datetime
import hashlib
import json
from flask import Flask, jsonify

class Layer:
    def __init__(self, neuroncount, neurontype, connectivity, activation, dact):
        #dropout mask, derivatives, normalization, etc
        self.neuroncount = neuroncount
        self.neurontype = neurontype
        self.connectivity = connectivity
        self.activation = activation
        self.dact = dact
    
    def forward(self,inputs):
        pass
    
    def backward(self,gradients):
        pass
    
    def loss(self,inputs):

class DataSet: # not included in blockchain, this class exists only to service the model on device
    def __init__(self, datadict, inputdim, outputdim):
        self.datadict = datadict # contains the actual data
        self.inputdim = inputdim
        self.outputdim = outputdim    

class ModelContainer:
    def __init__(self):
        self.modelType = modelType     # e.g. classifier, object detection, etc.
        self.modelParams = modelParams # all details needed to implement model, including custom libraries
        self.modelReadMe = modelReadMe # an explaination and/or additional info
        self.depends = depends         # standard library dependencies 
        self.modelHash = modelHash     # to identify the model
        self.modelSignatures = modelSignatures # to verify integrity, etc.

    def getParams(self):
        for item in self.modelParams:# everything needed to instantiate and run a model
            yield item
    
    def evalModel(self, modelID):
        ''' This is where the model gets checked for compatibility and then evaluated on users data.
            If model tested is different from and/or better than indigenous model, append own signature
            and rebroadcast. If none better than indigenous, create new container and append to data.'''
        ''' Maybe need to use IPC or something to run evaluation, i.e. Tensorflow or PyTorch or custom 
            frameworks '''
        pass

    def addModel(self, modelBluePrint):
        ''' This is where a new model would be added given "modelBluePrint", a dictionary of specifications,
            i.e. number of layers, neurons in each layer, activations, regularizations, which environment, 
            frameworks, libraries, etc. Also included in the dictionary should be paths and file names.'''
        pass

    def signModel(signingKey):
        if(signingKey.getPublic('hex') !== yournamehere):
            raise new Error('Who are you?')
        hashMod = self.hash(
            str(self.modelParams) +
            str(self.modelReadMe) +
            str(self.modelHash) +
            str(self.modelSignatures) 
        )
        sig = signingKey.sign(hashMod,'base64')
        self.signature = sig.toDER('hex')
        #encoded_model = JSON.dumps(modelstuff, sort_keys=True).encode()
        #return hashlib.sha256(encoded_block).hexdigest()

class Blockchain:
   
    # This function creates the very first block and sets its hash to "0"
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')#Genesis block
        self.numModels = numModels
        self.modSizeLim = modSizeLim
 
    # This function adds further blocks onto the chain
    def create_block(self, proof, previous_hash, data):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,# replace this with something else
                 'data': data,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
       
    # This function displays the previous block
    def print_previous_block(self):
        return self.chain[-1]
       
    # This PoW needs to be modified to suit the application
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
         
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
                 
        return new_proof
 
    # This function needs modification to fit the PoW replacement
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
         
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
               
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
             
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
         
        return True
 
    def hash(self, block):
        encoded_block = JSON.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def updateChain(self):
        '''  need a connection here and to send a beacon to request or broadcast a response to beacon '''
        pass

    def broadcastChain(self):
        if 
    
# Creating the Web App using Flask
app = Flask(__name__)
 
# Create an instance of the class Blockchain
blockchain = Blockchain()
 
# Mining a new block, needs to be modified
@app.route('/mine_block', methods=['GET'])
def mine_block():
    ''' need to check that nothing in 'data' that is not an instance of ModelContainer class and that no 
        more than 5 ModelContainers in data '''
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    if (len(previous_block.data) >5):
        block = blockchain.create_block(proof, previous_hash)
     
        response = {'message': 'A block is MINED',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'proof': block['proof'],
                    'previous_hash': block['previous_hash']}
        return jsonify(response), 200
    else:
        previous_block.data.append(ownModel)
      
# Display blockchain in JSON format
@app.route('/get_chain', methods=['GET'])
def display_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200
 
# Check validity of the blockchain
@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
     
    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200
 
 
# Run the Flask server locally
app.run(host='127.0.0.1', port=5000)
