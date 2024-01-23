import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=350)

with col2:
    st.title("Dan Toms")
    content = """
    About me bit

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin malesuada dapibus. Aenean vitae tortor bibendum elit accumsan sagittis. Nulla ultricies in ante non consequat. Suspendisse sed dolor et enim iaculis pulvinar non sed elit. Cras malesuada hendrerit eros. Nunc luctus auctor auctor. Curabitur volutpat, magna vel mollis imperdiet, quam massa molestie turpis, quis vestibulum ligula quam eu arcu. Aliquam porttitor cursus ultrices. Proin feugiat massa eget augue faucibus, in consectetur neque facilisis. Sed tellus leo, blandit ut neque eu, semper congue metus. Cras in erat suscipit est pretium rutrum. Phasellus maximus placerat justo. Sed laoreet facilisis nulla, malesuada tincidunt sem fermentum vitae. Nunc venenatis eget justo sed imperdiet. 
    """
    st.info(content)

content2 = """Below you can find some if the apps I have built in Python. Feel free to contact me."""

st.write(content2)