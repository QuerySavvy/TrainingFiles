import streamlit as st

st.title("Open Data Bar - Streamlit Demo")
st.subheader("Whats possible, limitations, and solutions")


#Page setup
page1, page2, page3 = st.tabs(["Page 1", "Page 2", "Page 3"])
code = '''#Page setup
page1, page2, page3 = st.tabs(["Page 1", "Page 2", "Page 3"])'''
st.code(code, language='python')

with page1:
    col1, col2, col3 = st.columns(3)
    st.write("Test high p1")
    with col1: #Add the buttons
        st.subheader("layouts")
        sidebarbutton = st.button("st.sidebar") #-- add a side bar
        containerbutton = st.button("st.container") #-- add a container
        columnbutton = st.button("st.columns") #-- add columns
    st.write("Test low p1")

with page2:
    st.write("Test high p2")
    st.write("Test low p2")
