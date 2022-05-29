#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Last Updated : 19 Feb, 2022

@author: Abhishek Tiwari, Simran Arora, Nikunj, Punam
https://www.geeksforgeeks.org/create-simple-blockchain-using-python/

"""
'''
Create simple Blockchain using Python
Difficulty Level : Medium
A blockchain is a time-stamped decentralized series of fixed records that contains data of any size is 
controlled by a large network of computers that are scattered around the globe and not owned by a single 
organization. Every block is secured and connected with each other using hashing technology which protects it 
from being tempered by an unauthorized person. 

Creating Blockchain using Python, mining new blocks, and displaying the whole blockchain: 

The data will be stored in JSON format which is very easy to implement and easy to read. The data is stored 
in a block and the block contains multiple data. Each and every minute multiple blocks are added and to 
differentiate one from the other we will use fingerprinting. The fingerprinting is done by using hash and to 
be particular we will use the SHA256 hashing algorithm. Every block will contain its own hash and also the 
hash of the previous function so that it cannot get tampered with. This fingerprinting will be used to chain 
the blocks together. Every block will be attached to the previous block having its hash and to the next block 
by giving its hash. The mining of the new block is done by giving successfully finding the answer to the proof
of work. To make mining hard the proof of work must be hard enough to get exploited. After mining the block 
successfully the block will then be added to the chain. After mining several blocks the validity of the chain 
must be checked in order to prevent any kind of tampering with the blockchain. Then the web app will be made 
by using Flask and deployed locally or publicly as per the need of the user.
'''
# Python program to create Blockchain
 
# For timestamp
import datetime
 
# Calculating the hash in order to add digital fingerprints to the blocks
import hashlib
 
# Flask is for creating the web app and jsonify is for displaying the blockchain
from flask import Flask, jsonify, render_template, request
 
# To store data in our blockchain
import json
 

class ModelContainer:
    ''' Intended to support only established frameworks such as PyTorch or TensorFlow. See version 1 
        for custom framework support.'''
    def __init__(self,modelParams,modelReadMe,modelHash,modelSignatures):
        self.modelParams = modelParams # all details needed to implement model, given library 
        self.modelReadMe = modelReadMe
        self.modelHash = modelHash # to identify the model
        self.modelSignatures = modelSignatures # to verify integrity, etc.

    def getParams(self):
        for item in self.modelParams:# everything needed to instantiate and run a model
            yield item
    
    def evalModel(self, modelID):
        ''' This is where the model gets checked for compatibility and then evaluated on users data.
            If model tested is different from and/or better than indigenous model, append own signature
            and rebroadcast. If none better than indigenous, create new container and append to data.'''
        #this will have to work for now. need to improve this because this should not allow passing args
        exec(self.modelParams['content'])
        
        ''' alternatively,  fname = self.modelParams['title']
                            exec(open(fname).read())'''
        ''' Maybe need to use IPC or something to run evaluation, i.e. Tensorflow or PyTorch or custom 
            frameworks. How to get results to compare between models? '''
        #pass



    def signModel(self, signingKey, yournamehere):
        if(signingKey.getPublic('hex') != yournamehere):
            raise ValueError('Who are you?')
        hashMod = self.hash(
            str(self.modelParams) +
            str(self.modelReadMe) +
            str(self.modelHash) 
        )
        sig = signingKey.sign(hashMod,'base64')
        
        self.modelSignatures.append(sig.toDER('hex'))
        #encoded_model = JSON.dumps(modelstuff, sort_keys=True).encode()
        #return hashlib.sha256(encoded_block).hexdigest()


class Blockchain:
   
    # This function creates the very first block and sets its hash to "0"
    def __init__(self, numModels, modSizeLim):
        self.chain = []
        self.create_block(ckpt=1, previous_hash='0', data=[])#Genesis block
        self.numModels = numModels
        self.modSizeLim = modSizeLim
 
    # This function adds further blocks onto the chain
    def create_block(self, ckpt, previous_hash, data): #proof, previous_hash, data):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'ckpt': ckpt,# replace this with something else
                 'data': data,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
       
    # This function displays the previous block
    def print_previous_block(self):
        return self.chain[-1]
       
    # This PoW needs to be modified to suit the application
    def checkpoint(self, previous_ckpt):
        this_block = self.chain[-1]
        new_ckpt = str(this_block['data'])
         
        # while check_proof is False:
        hash_operation = hashlib.sha256(new_ckpt.encode()).hexdigest()
            #str(new_ckpt**2 - previous_ckpt**2).encode()).hexdigest()

        return hash_operation
 
    # This function needs modification to fit the PoW replacement
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
         
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
               
            # previous_ckpt = previous_block['ckpt']
            # ckpt = block['ckpt']
            # #ckpt = self.checkpoint(previous_ckpt)
            # hash_operation = hashlib.sha256(
            #     str(ckpt**2 - previous_ckpt**2).encode()).hexdigest()#str(proof**2 - previous_proof**2).encode()).hexdigest()
             
            previous_block = block
            block_index += 1
         
        return True
 
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def updateChain(self):
        '''  need a connection here and to send a beacon to request or broadcast a response to beacon '''
        pass

    def broadcastChain(self):
        ''' need additional functionality here '''
        """ validating the whole chain would require walking the whole chain, potentially petabytes of 
            data, thus it may be more feasible, or even necessary, to maintain only a portion"""
        if len(self.chain) > 3:
            return self.chain[:-3]
        else:
            return self.chain
    
pathstub = '</your/path/here/>'
# Creating the Web App using Flask
app = Flask(__name__, template_folder=pathstub)
 
# Create an instance of the class Blockchain
blockchain = Blockchain(numModels=5,modSizeLim=200)
 
# Mining a new block, needs to be modified
#@app.route('/mine_block', methods=['GET', 'POST'])
def mine_block(ins):
    ''' need to check that nothing in 'data' that is not an instance of ModelContainer class and that no 
        more than 5 ModelContainers in data '''
        

    modelParams = ins
    modelReadMe = """ """
    encoded_model = str([item for item in modelParams]) + modelReadMe
    modelHash = hashlib.sha256(encoded_model.encode()).hexdigest()
    key = 'this is a temporary key, like lorem ipsum'
    modelSignatures = hashlib.sha256(key.encode()).hexdigest()
    # data is an object, not a list or dict
    modcon = ModelContainer(modelParams, modelReadMe, modelHash, modelSignatures)

    previous_block = blockchain.print_previous_block()
    previous_ckpt = previous_block['ckpt']
    ckpt = blockchain.checkpoint(previous_ckpt)
    previous_hash = blockchain.hash(previous_block)
    if (len(previous_block['data']) > 5):
        block = blockchain.create_block(ckpt, previous_hash, data=[modcon])
     
        response = {'message': 'A block is MINED',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'ckpt': block['ckpt'],
                    'previous_hash': block['previous_hash']}
        return jsonify(response), 200
    else:
        previous_block['data'].append(modcon)
        # bidx is the index of the block in the chain
        # cidx is the index of the modelcontainer in the data
        bidx, cidx = str(previous_block['index']), str(len(previous_block['data'])-1)
        #response = {'message': 'Model added at block '+block['index']+'container '+len(previous_block['data']-1)}
        response = {'message': 'Model added at block ' + bidx + ' container '+ cidx}
        return jsonify(response), 200
    #pass

@app.route('/get_specs', methods=('GET', 'POST'))
def get_specs():     
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        mine_block(content)
        print(content)
    return render_template('newblock.html')


def model_specs(mfw, layers, weights, params):
    main_framework = mfw
    layers = layers
    weights = weights
    learn_rate = params['LR']# default value
    dropout = params['DO'] # percent to drop, pkeep = 1 - dropout
    activations = params['ACT']
    biases = params['BL']
    
# Display blockchain in JSON format
@app.route('/get_chain', methods=['GET'])
def display_chain():
    # response = {'chain': str(blockchain.chain),
    #             'length': len(blockchain.chain)}
    response = [len(blockchain.chain)]
    response.extend([x for x in blockchain.chain])
    print(blockchain.chain)
    #return jsonify(response), 200
    return render_template('lastblock.html', messages=response)
 
# Check validity of the blockchain
@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
     
    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200
 

messages = [{'title': 'Message the First',
             'content': 'These messages are in the main code file'},
            {'title': 'TODO',
             'content': ' - signing models'},
            {'title': '',
             'content': ' - parsing input'},
            {'title': '',
             'content': ' - broadcasting and recieving'},
            {'title': '',
             'content': ' - evaluating models'}
            ]


@app.route('/')
def index():
    return render_template('index.html', messages=messages)

 @app.route('/about')
def about():
    return render_template('about.html')
 
# Run the Flask server locally
app.run(host='127.0.0.1', port=5000)
