DEFAULT_ADDRESS = '0x5face5582CaE06bE3E51B05DA2c3853D353A5CC5'
URL = 'https://ropsten.infura.io/v3/5fc49ffa7ebe42f282366f4a13230f1e'

REGISTRY_ADDRESS = '0x645342Aa53571ABC47EA292Cea3aD00c5439E69f'
NFT_ADDRESS = '0x4ed5E88BfEb02Cd44Ec18BB23DFc74ABc66ACf47'

REGISTRY_ABI = """ [{"inputs": [], "stateMutability": "payable", "type": "constructor", "name": "constructor"}, {"anonymous": false, "inputs": [{"indexed": false, "internalType": "address", "name": "owner_address", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "id", "type": "uint256"}, {"indexed": false, "internalType": "string", "name": "firstName", "type": "string"}, {"indexed": false, "internalType": "string", "name": "lastName", "type": "string"}, {"indexed": false, "internalType": "string", "name": "codiceFiscale", "type": "string"}, {"indexed": false, "internalType": "string", "name": "docType", "type": "string"}, {"indexed": false, "internalType": "string", "name": "docNumber", "type": "string"}], "name": "NewOwnerCreated", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "internalType": "uint256", "name": "id", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "areaSqm", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "floor", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "zipCode", "type": "uint256"}, {"indexed": false, "internalType": "string", "name": "country", "type": "string"}, {"indexed": false, "internalType": "string", "name": "region", "type": "string"}, {"indexed": false, "internalType": "string", "name": "city", "type": "string"}, {"indexed": false, "internalType": "string", "name": "street", "type": "string"}, {"indexed": false, "internalType": "string", "name": "streetNumber", "type": "string"}, {"indexed": false, "internalType": "string", "name": "adressAdditional", "type": "string"}, {"indexed": false, "internalType": "string", "name": "houseType", "type": "string"}], "name": "NewPropertyRegistered", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "internalType": "address", "name": "new_owner", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "propert_id", "type": "uint256"}], "name": "OwnershipTransferred", "type": "event"}, {"inputs": [], "name": "Payment", "outputs": [], "stateMutability": "payable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "_property_id", "type": "uint256"}, {"internalType": "address", "name": "_new_owner_address", "type": "address"}], "name": "Transfer", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "_id", "type": "uint256"}, {"internalType": "uint256", "name": "_areaSqm", "type": "uint256"}, {"internalType": "uint256", "name": "_floor", "type": "uint256"}, {"internalType": "uint256", "name": "_zipCode", "type": "uint256"}, {"internalType": "string", "name": "_country", "type": "string"}, {"internalType": "string", "name": "_region", "type": "string"}, {"internalType": "string", "name": "_city", "type": "string"}, {"internalType": "string", "name": "_street", "type": "string"}, {"internalType": "string", "name": "_streetNumber", "type": "string"}, {"internalType": "string", "name": "_addressAdditional", "type": "string"}, {"internalType": "string", "name": "_houseType", "type": "string"}], "name": "Update", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "address_to_owner", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "addresses_list", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "all_prop_id_to_personal_prop_id", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "_new_price_registration", "type": "uint256"}], "name": "changePriceRegistration", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "_new_price_transfers", "type": "uint256"}], "name": "changePriceTransfer", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_owner", "type": "address"}], "name": "countOwnerProperties", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "customerBalance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_owner", "type": "address"}], "name": "findOwner", "outputs": [{"internalType": "string", "name": "", "type": "string"}, {"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "_id", "type": "uint256"}], "name": "findPropertyOwner", "outputs": [{"internalType": "string", "name": "", "type": "string"}, {"internalType": "string", "name": "", "type": "string"}, {"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_owner", "type": "address"}], "name": "find_properties", "outputs": [{"internalType": "uint256[]", "name": "", "type": "uint256[]"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "ownerPropertyCount", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "", "type": "address"}, {"internalType": "uint256", "name": "", "type": "uint256"}], "name": "owner_to_property", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "owners", "outputs": [{"internalType": "uint256", "name": "id", "type": "uint256"}, {"internalType": "string", "name": "firstName", "type": "string"}, {"internalType": "string", "name": "lastName", "type": "string"}, {"internalType": "string", "name": "codiceFisc", "type": "string"}, {"internalType": "string", "name": "docType", "type": "string"}, {"internalType": "string", "name": "docNumber", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "properties", "outputs": [{"internalType": "uint256", "name": "id", "type": "uint256"}, {"internalType": "uint256", "name": "sqm", "type": "uint256"}, {"internalType": "uint256", "name": "floor", "type": "uint256"}, {"internalType": "uint256", "name": "zipCode", "type": "uint256"}, {"internalType": "string", "name": "country", "type": "string"}, {"internalType": "string", "name": "region", "type": "string"}, {"internalType": "string", "name": "city", "type": "string"}, {"internalType": "string", "name": "street", "type": "string"}, {"internalType": "string", "name": "streetnum", "type": "string"}, {"internalType": "string", "name": "addressAdditional", "type": "string"}, {"internalType": "string", "name": "houseType", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "string", "name": "_firstName", "type": "string"}, {"internalType": "string", "name": "_lastName", "type": "string"}, {"internalType": "address", "name": "_address", "type": "address"}, {"internalType": "string", "name": "_codiceFiscale", "type": "string"}, {"internalType": "string", "name": "_docType", "type": "string"}, {"internalType": "string", "name": "_docNumber", "type": "string"}], "name": "registerOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_Owner", "type": "address"}, {"internalType": "uint256", "name": "_areaSqm", "type": "uint256"}, {"internalType": "uint256", "name": "_floor", "type": "uint256"}, {"internalType": "uint256", "name": "_zipCode", "type": "uint256"}, {"internalType": "string", "name": "_country", "type": "string"}, {"internalType": "string", "name": "_region", "type": "string"}, {"internalType": "string", "name": "_city", "type": "string"}, {"internalType": "string", "name": "_street", "type": "string"}, {"internalType": "string", "name": "_streetNumber", "type": "string"}, {"internalType": "string", "name": "_addressAdditional", "type": "string"}, {"internalType": "string", "name": "_houseType", "type": "string"}], "name": "registerProperty", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "revenue", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "showBalance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_owner", "type": "address"}], "name": "showOwnerBalance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "showOwnersCount", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "showPropertyCount", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "showRegistrationPrice", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "showTransferPrice", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "show_revenue", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"stateMutability": "payable", "type": "receive"}] """


NFT_ABI = """ [{"inputs": [], "stateMutability": "nonpayable", "type": "constructor", "name": "constructor"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": true, "internalType": "address", "name": "approved", "type": "address"}, {"indexed": true, "internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": true, "internalType": "address", "name": "operator", "type": "address"}, {"indexed": false, "internalType": "bool", "name": "approved", "type": "bool"}], "name": "ApprovalForAll", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "internalType": "uint256", "name": "tokenId", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "TokenCollateralized", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}, {"indexed": true, "internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "priceCalculation", "type": "event"}, {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "_checkCollateralization", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}, {"internalType": "uint256", "name": "collateralization_amount", "type": "uint256"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "_collateralize", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "_requireCollateralValue", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "approve", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "burnNFT", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "getApproved", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "gettokenURI", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "operator", "type": "address"}], "name": "isApprovedForAll", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "isOwner", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "string", "name": "_uri", "type": "string"}, {"internalType": "address", "name": "_owner", "type": "address"}], "name": "mintNFT", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "ownerOf", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "tokenId", "type": "uint256"}, {"internalType": "bytes", "name": "_data", "type": "bytes"}], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "operator", "type": "address"}, {"internalType": "bool", "name": "approved", "type": "bool"}], "name": "setApprovalForAll", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "bytes4", "name": "interfaceId", "type": "bytes4"}], "name": "supportsInterface", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "tokenCounter", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "tokenURI", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "transferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function"}] """

