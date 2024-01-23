import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=350)

with col2:
    st.title("Dan Toms")
    content = """
    About me bit
    """
    st.info(content)