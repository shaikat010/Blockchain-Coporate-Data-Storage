#from trilio import Trilio
from trilio import *


blockchain = Trilio()
print(blockchain)

print("This is the validity Status ------------------------------------->")
valid = blockchain.validate_chain()  # True = Valid, False = Invalid
print(valid)

wallet = blockchain.Wallet.create_wallet()  # Will return json with wallet information
print("This is the wallet object ----------------------------------------------------------->")
print(wallet)

address = wallet["address"]
print("This is the private key ------------------------------------------------------------>")
print(address["pve"])  # Private key
print("This is the public key -------------------------------------------------------------->")
print(address["pbc"])  # Public key

print(f"This is the address {address}")

print("These are the balance details:")

# This shows that there is zero balance
print(blockchain.Wallet.get_balance(private_key=address["pve"], public_key=address["pbc"]))  # Get a wallet's balance

# This shows that there is no asset currently
print(blockchain.Wallet.get_assets(private_key=address["pve"], public_key=address["pbc"]))  # Get a wallet's assets

# This shows that there are no collections
print(blockchain.Wallet.get_collections(private_key=address["pve"],
                                        public_key=address["pbc"]))  # Get a wallet's collections

# If we want to convert the wallet key then we use this code:
# blockchain.Wallet.get_public_key(private_key=<private_key>)

# Crediting a wallet:
# mention the public key and the amount that you want to credited
blockchain.Wallet.credit_wallet(public_key=address["pbc"], amount=10)
print("This is the current balance after crediting the wallet --------------------------------------->")
print(blockchain.Wallet.get_balance(private_key=address["pve"], public_key=address["pbc"]))  # Get a wallet's balance
# Validating a wallet:
# mention the keys
# True = found, False = not found
print("This is the validity of the wallet -------------------------------------------------------------->")
#print(blockchain.Wallet.validate_wallet(private_key=address["pve"], public_key=address["pbc"]))


print(blockchain.trilio.chain)
print(blockchain)
print(blockchain.validate_chain())

# Sending tokens to the wallet:
# Need to import datetime
# mention the keys and the amount
# blockchain.create_transaction(
#     datetime.now(),
#     data = {
#         "type":"token-transfer",
#         "data":{
#             "to":<public_key (Wallet receiving)>,
#             "from":<private_key (Wallet sending)>,
#             "amount":<amount>
#         }
#     }
# )


# Creating a collection

# Need to import datetime
# blockchain.create_transaction(
#     datetime.now(),
#     data = {
#         "type":"contract-action",
#         "action":"collection-creation",
#         "data":{
#             "name":<collection_name>,
#             "description":<collection_description>,
#             "url":<collection_url>,
#             "icon":<collection_icon>,
#             "tags":<collection_tags>,
#             "signer":<private_key>
#         }
#     }
# )

# print(blockchain.Wallet.get_collections(private_key=<private_key>, public_key=<public_key>))


# Creating Asset
# Need to import datetime
# blockchain.create_transaction(
#     datetime.now(),
#     data={
#         "type":"contract-action",
#         "action":"asset-creation",
#         "data":{
#             "name":<asset_name>,
#             "description":<asset_description>,
#             "collection_id":<collection_id>,
#             "quantity":<asset_mint_amount>,
#             "signer":<private_key>
#         }
#     }
# )
# print(blockchain.Wallet.get_assets(private_key=<private_key>, public_key=<public_key>))
