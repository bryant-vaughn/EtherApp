import sys
from web3 import Web3

contract_address = sys.argv[1]
infura_url = sys.argv[2]

web3 = Web3(Web3.HTTPProvider(infura_url))

low = 0
high = web3.eth.blockNumber
mid = high // 2

while(low < high):
	bytecode = web3.eth.getCode(account = contract_address, block_identifier = mid).hex()

	# using binary approach to find first instance of contract
	if bytecode == '0x': # contract doesn't exist yet at this block
		low = mid
		mid = (low + high) // 2
	elif bytecode != '0x': # contract could 
		high = mid
		mid = (low + high) // 2

print(bytecode)
