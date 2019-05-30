#import json
import sys
from web3 import Web3

# print("This is the name of the script: ", sys.argv[0])
# print("Number of arguments: ", len(sys.argv))
# print("The arguments are: ", str(sys.argv))

contract_address = sys.argv[1]
infura_url = sys.argv[2]

web3 = Web3(Web3.HTTPProvider(infura_url))
bytecode = web3.eth.getCode(contract_address)
print(bytecode)
