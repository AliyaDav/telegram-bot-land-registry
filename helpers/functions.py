import json
from web3 import Web3

def RegisterOwner(URL, contract, abi,_firstName,_lastName,owner_address, _codiceFiscale, _docType, _docNumber): # all inputs are strings
    #connect to the contract
    web3 = Web3(Web3.HTTPProvider(URL))
    web3.eth.defaultAccount = web3.toChecksumAddress('0x5face5582CaE06bE3E51B05DA2c3853D353A5CC5')
    # web3.eth.defaultAccount = web3.eth.accounts.privateKeyToAccount('0x2c092433de46556c8569194b39474cc058389a2245242591eb7640eb8034a4af')
    abi = json.loads(abi)
    address = web3.toChecksumAddress(contract)
    print("Starting registring...")
    contract = web3.eth.contract(address = address, abi = abi) # connect to the subscription/registry contract
    print("Connected to the contract...")
    tx = contract.functions.registerOwner(_firstName,_lastName,owner_address, _codiceFiscale, _docType, _docNumber).buildTransaction({'nonce': web3.eth.getTransactionCount(web3.eth.defaultAccount)})
    signed_tx = web3.eth.account.signTransaction(tx, private_key='0x2c092433de46556c8569194b39474cc058389a2245242591eb7640eb8034a4af')
    web3.eth.sendRawTransaction(signed_tx.rawTransaction)


def RegisterProperty(URL,contract,abi, _Owner_address, _areaSqm, _floor, _zipCode, _country, _region, _city, _street,  _streetNumber, _addressAdditional, _houseType):
    web3 = Web3(Web3.HTTPProvider(URL))
    web3.eth.defaultAccount = web3.toChecksumAddress('0x5face5582CaE06bE3E51B05DA2c3853D353A5CC5')
    abi = json.loads(abi)
    address = web3.toChecksumAddress(contract)
    print("Starting registring...")
    contract = web3.eth.contract(address = address, abi = abi) # connect to the subscription/registry contract
    print("Connected to the contract...")
    print(_Owner_address, _areaSqm, _floor, _zipCode, _country, _region, _city, _street,  _streetNumber, _addressAdditional, _houseType)
    tx = contract.functions.registerProperty(_Owner_address, _areaSqm, _floor, _zipCode, _country,_region, _city, _street,  _streetNumber, _addressAdditional, _houseType).buildTransaction({'nonce': web3.eth.getTransactionCount(web3.eth.defaultAccount)})
    signed_tx = web3.eth.account.signTransaction(tx, private_key='0x2c092433de46556c8569194b39474cc058389a2245242591eb7640eb8034a4af')
    web3.eth.sendRawTransaction(signed_tx.rawTransaction)

def MintNFT(URL,contract,abi, uri, owner_address): # all inputs are strings
    #connect to the contract
    web3 = Web3(Web3.HTTPProvider(URL))
    web3.eth.defaultAccount = web3.toChecksumAddress('0x5face5582CaE06bE3E51B05DA2c3853D353A5CC5')
    abi = json.loads(abi)
    address = web3.toChecksumAddress(contract)
    contract = web3.eth.contract(address = address, abi = abi) # connect to the nft contract
    print("Connected to the contract...")
    tx = contract.functions.mintNFT(uri, owner_address).buildTransaction({'nonce': web3.eth.getTransactionCount(web3.eth.defaultAccount)})
    signed_tx = web3.eth.account.signTransaction(tx, private_key='0x2c092433de46556c8569194b39474cc058389a2245242591eb7640eb8034a4af')
    web3.eth.sendRawTransaction(signed_tx.rawTransaction)

	

