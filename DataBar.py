import streamlit as st

st.title("Streamlit")
st.subheader("Whats possible, limitations, and solutions")

page1, page2, page3 = st.tabs(["Page 1", "Page 2", "Page 3"])
col1, col2, col3 = st.columns(3)

with page1:
    with col1: #Add the buttons
        st.subheader("layouts")
        sidebarbutton = st.button("Add sidebar") #-- add a side bar
        containerbutton = st.button("Add container") #-- add a container
        
if sidebarbutton == True:
    st.sidebar.write("Yipeeee")
    #Show the code
    code = '''sidebarbutton = st.button("Add sidebar")
if sidebarbutton == True:
    st.sidebar.write("Yipeeee")'''
    st.code(code, language='python')

#add a container bar
if containerbutton == True:
    with st.container(border=True):
        st.write("Yipeeee")
        #Show the code
    code = '''containerbutton = st.button("Add container")
if containerbutton == True:
    with st.container(border=True):
        st.write("Yipeeee")'''
    st.code(code, language='python')
