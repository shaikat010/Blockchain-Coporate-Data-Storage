import streamlit as st
import base64
# Main_Chain is imported to make blocks in this chain
from main import Main_Chain

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
st.title("Blockchain Coin Transfer Application")


# Header
st.header("Creative Coin Transfer Application")


# ----------------- Blockchain Metrics ----------------------------------------------
col1, col2, col3 = st.columns(3)
col1.metric('Block Height', str(Main_Chain.get_chain_height()), '1.2')
"""These are the blockchain metrics, showing the current state of the blockchain"""
col2.metric('Hash rate', '9', '8')
col3.metric('Transactions', '86', '4')
# A neat combination of st.columns with metrics.


# -------------- Input field ---------------------------------------------
name = st.text_input("Enter your transaction data here", "Type Here ...")
data = name

# ----------- Asking the user for a file to be upload ---------------------------------
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# ------------------------- Sidebar -------------------------------------
with st.sidebar:
    st.title("Creative Coin: About")
    st.write("Creative Coin in a simulatory coin created to understand the working of a crypto token or currency via connecting into a self developed blockchain structure. The transactions are stored in the blocks and the accounts are updated accordingly. ")
    # import Image from pillow to open images
    from PIL import Image

    img = Image.open("Creative_Coin.png")

    # display image using streamlit
    # width is used to set the width of an image
    st.image(img, width=200)

    st.write("The block height is the same as the length of the block, this means it is the number of blocks that are added in the blockchain")

    img = Image.open("Crypto.png")

    # display image using streamlit
    # width is used to set the width of an image
    st.image(img, width=250)


