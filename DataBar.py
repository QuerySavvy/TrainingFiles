import streamlit as st

st.title("Streamlit")
st.subheader("Whats possible, limitations, and solutions")

#add a side bar
sidebarbutton = st.button("Add sidebar")
if sidebarbutton == True:
  st.sidebar.write("Yipeeee")

#add a container bar
containerbutton = st.button("Add container")
if containerbutton == True:
  with st.container():
    write("Yipeeee")
