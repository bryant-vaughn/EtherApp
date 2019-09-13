# EtherApp
This is a python CLI application utilizing web3.py to interact with the Ethereum blockchain. It uses a 20 byte contract address to return the block and transaction hashes for the block containing the contract deployment.
To run the app from the command line / terminal, use the following command:

`python3 main.py 0xcontract_address_here --host https://mainnet.infura.io/<API_SECRET>`

The app will provide a response of:

`Block: 0xblock_from_which_contract_was_deployed`

`Transaction: 0xtransaction_with_which_contract_was_deployed`
