import json
from web3 import Web3

def RegisterOwner(URL,contract,abi,_firstName,_lastName,owner_address, _codiceFiscale, _docType, _docNumber): # all inputs are strings
    #connect to the contract
    web3 = Web3(Web3.HTTPProvider(URL))
    web3.eth.defaultAccount = web3.toChecksumAddress('0x5face5582CaE06bE3E51B05DA2c3853D353A5CC5')
    abi = json.loads(abi)
    address = web3.toChecksumAddress(contract)
    contract = web3.eth.contract(address = address, abi = abi) # connect to the subscription/registry contract
    contract.functions.registerOwner(_firstName,_lastName,owner_address, _codiceFiscale, _docType, _docNumber).call()


def RegisterProperty(URL,contract,abi, _Owner_address, _areaSqm, _floor, _zipCode, _country, _region, _city, _street,  _streetNumber, _addressAdditional, _houseType):
    web3 = Web3(Web3.HTTPProvider(URL))
    web3.eth.defaultAccount = web3.toChecksumAddress('0x5face5582CaE06bE3E51B05DA2c3853D353A5CC5')
    abi = json.loads(abi)
    address = web3.toChecksumAddress(contract)
    contract = web3.eth.contract(address = address, abi = abi) # connect to the subscription/registry contract
    contract.functions.registerOwner(_Owner_address, _areaSqm, _floor, _zipCode, _country, _region, _city, _street,  _streetNumber, _addressAdditional, _houseType).call()
	

def MintNFT(URL,contract,abi, uri, owner_address): # all inputs are strings
    #connect to the contract
    web3 = Web3(Web3.HTTPProvider(URL))
    web3.eth.defaultAccount = web3.toChecksumAddress('0x5face5582CaE06bE3E51B05DA2c3853D353A5CC5')
    abi = json.loads(abi)
    address = web3.toChecksumAddress(contract)
    contract = web3.eth.contract(address = address, abi = abi) # connect to the nft contract
    contract.functions.mintNFT(uri, owner_address).call()	
	

