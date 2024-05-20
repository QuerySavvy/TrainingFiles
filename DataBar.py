import streamlit as st

st.title("Open Data Bar - Streamlit Demo")
st.subheader("Whats possible, limitations, and solutions")


#Page setup
page1, page2, page3 = st.tabs(["Page 1", "Page 2", "Page 3"])


with page1:
    col1, col2, col3, col4 = st.columns(4)
    with col1: #Add the buttons
        st.subheader("Layouts")
        sidebarbutton = st.button("st.sidebar") #-- add a side bar
        containerbutton = st.button("st.container") #-- add a container
        columnbutton = st.button("st.columns") #-- add columns
        tabsbutton = st.button("st.tabs") #-- add page tabs

    if tabsbutton == True:
        #Show the code
        code = '''page1, page2, page3 = st.tabs(["Page 1", "Page 2", "Page 3"])
with page1:
    col1, col2, col3, col4 = st.columns(4)
    with col1: #Add the buttons
        st.subheader("Layouts")
        tabsbutton = st.button("st.tabs") #-- add page tabs'''
        st.code(code, language='python')
    if sidebarbutton == True:
        st.sidebar.write("Yipeeee")
        #Show the code
        code = '''sidebarbutton = st.button("Add sidebar")
if sidebarbutton == True:
    st.sidebar.write("Yipeeee")'''
        st.code(code, language='python')
    
    #add a container 
    if containerbutton == True:
        with st.container(border=True):
            st.write("Yipeeee")
            #Show the code
        code = '''containerbutton = st.button("Add container")
if containerbutton == True:
    with st.container(border=True):
        st.write("Yipeeee")'''
        st.code(code, language='python')
    
    
    #add columns
    if columnbutton == True:
        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.write("col_1")
        with col_2:
            st.write("col_2")
        with col_3:
            st.write("col_3")
            
        col_1, col_2, col_3 = st.columns([0.1,0.7, 0.1])
        with col_1:
            st.write("col_1")
        with col_2:
            st.write("col_2")
        with col_3:
            st.write("col_3")
            #Show the code
        code = '''columnbutton = st.button("st.columns")
if columnbutton == True:
    col_1, col_2, col_3 = st.columns(3) 
    with col_1:
    st.write("col_1")
    with col_2:
        st.write("col_2")
    with col_3:
        st.write("col_3")
            
    col_1, col_2, col_3 = st.columns([0.1,0.8, 0.1]) 
    with col_1:
        st.write("col_1")
    with col_2:
        st.write("col_2")
    with col_3:
        st.write("col_3")'''
        st.code(code, language='python')
        
    with col2: #Add the buttons
        st.subheader("Text options")
        commontext = st.button("Text elements") 
        codetext = st.button("st.code")
        texttext = st.button("st.text")

    if commontext == True:
        st.title("This is st.title")
        st.header("This is st.header")
        st.subheader("This is st.subheader")
        st.write("This is st.write")

    if codetext == True:
        code = '''SELECT employee,
salary 

FROM hardis

WHERE salary>100000

ORDER BY salary DESC'''
        st.code(code, language='SQL')

    if texttext == True:
        st.text("Merci - Nous avons bien reçu votre demande")
        
    with col3: #Add the buttons
        st.subheader("User Input")
        textinput = st.button("Text Input")
        clicks = st.button("Clicks")
        
    if textinput == True:
        st.text_input("Please enter a message", 
                      placeholder = "This is made with st.text_input")
        options = st.selectbox("Please select an option",
                     ("Option 1", "Option 2", "Option 3"))
        
        multioptions = st.multiselect(
        "What are your favorite colors",
        ["Green", "Yellow", "Red", "Blue"])
        
        st.divider()
        code = '''st.text_input("Please enter a message", 
              placeholder = "This is made with st.text_input")
options = st.selectbox("Please select an option",
             ("Option 1", "Option 2", "Option 3"))'''
        st.code(code, language='python')



    if clicks == True:
        agree = st.checkbox("I agree")


with page2:
    st.write("Test")
