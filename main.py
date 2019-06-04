import sys
from web3 import Web3

contract_address = sys.argv[1]
infura_url = sys.argv[3]

web3 = Web3(Web3.HTTPProvider(infura_url))

low = 0
high = web3.eth.blockNumber # set high to latest block number
mid = high // 2

while(low < high - 1): # using high - 1 to avoid infinite loop
	
	bytecode = web3.eth.getCode(account = contract_address, block_identifier = mid).hex()

	# using binary approach to find first instance of contract
	if len(bytecode) == 2: # contract doesn't exist yet at this block
		low = mid
		mid = (low + high) // 2
	else: # contract exists at this block
		high = mid
		mid = (low + high) // 2

# check needed in rare case that first checked block was the one needed
if len(web3.eth.getCode(account = contract_address, block_identifier = mid).hex()) == 2:
	mid += 1

# holders of information from the block's data
block = web3.eth.getBlock(mid)
block_hash = block.hash
transactions = block.transactions

# loop through the block's transactions to find a matching contract address
for transaction in transactions:
	receipt = web3.eth.getTransactionReceipt(transaction)
	if(receipt.contractAddress == contract_address):
		trans_hash = receipt.transactionHash


# print results to the terminal
print()
print("Block: " + block_hash.hex())
print("Transaction: " + trans_hash.hex())
print()
