import streamlit as st

st.title("Streamlit")
st.subheader("Whats possible, limitations, and solutions")

page1, page2, page3 = st.tabs(["Page 1", "Page 2", "Page 3"])
col1, col2, col3 = st.columns(3)

with page1:
  #add a side bar
  sidebarbutton = st.button("Add sidebar")
  with col1:
    if sidebarbutton == True:
      st.sidebar.write("Yipeeee")
      #Show the code
      code = '''sidebarbutton = st.button("Add sidebar")
      if sidebarbutton == True:
      st.sidebar.write("Yipeeee")'''
      st.code(code, language='python')

    #add a container bar
    containerbutton = st.button("Add container")
    if containerbutton == True:
      with st.container(border=True):
        st.write("Yipeeee")
