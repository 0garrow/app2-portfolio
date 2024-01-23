import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Dan Toms")
    content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin malesuada dapibus. Aenean vitae tortor bibendum elit accumsan sagittis. Nulla ultricies in ante non consequat. Suspendisse sed dolor et enim iaculis pulvinar non sed elit. 
    """
    st.info(content)

content2 = """Below you can find some if the apps I have built in Python. Feel free to contact me."""

st.subheader(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
