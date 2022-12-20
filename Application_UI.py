import streamlit as st
import base64
# Main_Chain is imported to make blocks in this chain
# from main import Main_Chain

#from trilio import Trilio
from trilio import *
blockchain = Trilio()

#images : https://www.finance-monthly.com/Finance-Monthly/wp-content/uploads/2021/12/iStock-862230824-724x430.jpg
#images: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.tasmeemme.com%2Fen%2Fstore-items%2Fblockchain-technology-background-blue-digital-pattern-bussines-concept-banner-blockchain-vector-concept-illustration-vector-technology-blockchain-background%2F%3Fitem%3D10123671546&psig=AOvVaw0mXOgjMfGDSIdlzOIakQ2-&ust=1670053496733000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOiTmp242vsCFQAAAAAdAAAAABAs
#image: https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dblack%2Bblockchain&psig=AOvVaw0uI-O-XWKLTi3wm-TZUsdb&ust=1670053764944000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCKiHqp252vsCFQAAAAAdAAAAABAF
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.finance-monthly.com/Finance-Monthly/wp-content/uploads/2021/12/iStock-862230824-724x430.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('BG.jpg')


# Title
st.title("Employee Data Storage System ")


# Header
st.header("Corporate data storage using blockchain an decentralised storage")


# ----------------- Blockchain Metrics ----------------------------------------------
col1, col2, col3 = st.columns(3)
col1.metric('Block Difficulty', str(blockchain.validate_chain()), '1.2')
"""These are the blockchain metrics, showing the current state of the blockchain"""
col2.metric('Hash rate', '9', '8')
col3.metric('Transactions', '86', '4')
# A neat combination of st.columns with metrics.



# -------------- Input field ---------------------------------------------
name = st.write("Press to get a Public and Private key!")
if st.button("Get Private and Public Key"):
    wallet = blockchain.Wallet.create_wallet()
    address = wallet["address"]
    st.write(address["pbc"])
    st.write(address["pve"])


# -------------- Input field ---------------------------------------------
name = st.text_input("Enter your Private key here", "Your Private Key ...")
data = name

if st.button("Enter"):
    st.write("Account Validated!")

# ----------- Asking the user for a file to be upload ---------------------------------
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    # st.write(bytes_data)
    st.success("Data has been added to Blockchain!")

# ------------------------- Sidebar -------------------------------------
with st.sidebar:
    st.title("Employee Data Storage : About")
    st.write("The corporate data storage system uses a decentralised storage for keeping the employee data.The "
             "transactions are logged in the block structures in the blockchain")
    # import Image from pillow to open images
    from PIL import Image

    img = Image.open("Corporate.png")

    # display image using streamlit
    # width is used to set the width of an image
    st.image(img, width=200)

    st.write("The block height is the same as the length of the block, this means it is the number of blocks that are added in the blockchain")

    img = Image.open("Crypto.png")

    # display image using streamlit
    # width is used to set the width of an image
    st.image(img, width=250)


