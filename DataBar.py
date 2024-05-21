import streamlit as st
import time


st.title("Open Data Bar - Streamlit Demo")
session_state = st.session_state


#Page setup
page1, page2, page3 = st.tabs(["Page 1", "Page 2", "Page 3"])

with page1:
    col1, col2, col3= st.columns(3)
    with col1: #Add the buttons
        st.subheader("Layouts")
        sidebarbutton = st.button("st.sidebar") #-- add a side bar
        containerbutton = st.button("st.container") #-- add a container
        columnbutton = st.button("st.columns") #-- add columns
        tabsbutton = st.button("st.tabs") #-- add page tabs

    if tabsbutton == True:
        st.divider()
        #Show the code
        code = '''page1, page2, page3 = st.tabs(["Page 1", "Page 2", "Page 3"])
with page1:
    col1, col2, col3 = st.columns(3)
    with col1: #Add the buttons
        st.subheader("Layouts")
        tabsbutton = st.button("st.tabs") #-- add page tabs'''
        st.code(code, language='python')
    if sidebarbutton == True:
        st.divider()
        st.sidebar.write("Yipeeee")
        #Show the code
        code = '''sidebarbutton = st.button("Add sidebar")
if sidebarbutton == True:
    st.sidebar.write("Yipeeee")'''
        st.code(code, language='python')
    
    #add a container 
    if containerbutton == True:
        st.divider()
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
        st.divider()
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
        st.divider()
        st.title("This is st.title")
        st.header("This is st.header")
        st.subheader("This is st.subheader")
        st.write("This is st.write")

    if codetext == True:
        st.divider()
        code = '''SELECT employee,
salary 

FROM hardis

WHERE salary>100000

ORDER BY salary DESC'''
        st.code(code, language='sql')

    if texttext == True:
        st.divider()
        st.text("Merci - Nous avons reçu votre demande.") 
        st.text("Nous vous répondrons dans un délai de 12 mois (minimum).")
        st.text("Cordialement")
        st.text("L'administration Française")
        
    with col3: #Add the buttons
        st.subheader("User Interaction")
        textinput = st.button("Text Input")
        clicks = st.button("Clicks")
        loading = st.button("Loading icon")
        warnings = st.button("Warnings")
        
    if textinput == True:
        st.divider()
        st.text_input("Please enter a message", 
                      placeholder = "This is made with st.text_input")
        options = st.selectbox("Please select an option",
                     ("Option 1", "Option 2", "Option 3"))
        
        code = '''st.text_input("Please enter a message", 
              placeholder = "This is made with st.text_input")
options = st.selectbox("Please select an option",
             ("Option 1", "Option 2", "Option 3"))'''
        st.code(code, language='python')

    if clicks == True:
        st.divider()
        agree = st.checkbox("I agree")
        genre = st.radio("What is your favourite cheese",
        ["Emmental", "Bleu", "Chevre"])
        uploaded_files = st.file_uploader("Please upload a file")
        code = '''agree = st.checkbox("I agree")
genre = st.radio("What is your favourite cheese",
["Emmental", "Bleu", "Chevre"])
uploaded_files = st.file_uploader("Please upload a file")'''
        st.code(code, language='python')

    if loading:
        st.divider()
        with st.spinner('loading...'):
            time.sleep(3)
            st.success('Done!')
        code = '''with st.spinner('loading...'):
    time.sleep(5)
    st.success('Done!')'''
        st.code(code, language='python')
            
    if warnings:
        st.divider()
        st.success("st.success", icon="🚀")
        st.info("st.info", icon="ℹ️")
        st.warning("st.warning",icon="☢️")
        st.error("st.error", icon="😱")
        code = '''st.success("st.success", icon="🚀")
st.info("st.info", icon="ℹ️")
st.warning("st.warning",icon="☢️")
st.error("st.error", icon="😱")'''
        st.code(code, language='python')
    
with page2:

    #Initialise my session states
    if 'disp_session_state' not in session_state:
        session_state['disp_session_state'] = False
    if 'taco' not in session_state:
        session_state['taco'] = None
    
    st.write("Page2Selected")
    st.write("Launched in 2019. Limited information available besides the official docs. ChatGPT-3.5 goes up to Jan 2022 so isnt very helpful.")

    col1_top, col2_top = st.columns([0.7,0.3])
    with col1_top:
        st.header("Execution limitations")
    with col2_top:
        disp_session_state = st.toggle("Display session state")
        if disp_session_state:
            session_state['disp_session_state'] = True
        else:
            session_state['disp_session_state'] = False
    if session_state['disp_session_state'] == True:
        session_state

    with st.container(border=True):
        
#-------- Taco v1
        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            taco1 = st.button("Make a Taco v1")
        with col_2:
            taco2 = st.button("Make a Taco v2")
        with col_3:
            taco3 = st.button("Make a Taco v3")
            
        if taco1:
            session_state['taco'] = False
            col_1, col_2, col_3 = st.columns(3)
            with col_1:
                size = st.radio("Choose a size",["mini", "une viande", "deux viandes"])
            with col_2:
                meat = st.multiselect("Choose the meat",["Poulet panné", "Cordon bleu", "kebab"])
            with col_3:
                sauce = st.multiselect("Choose the sauce",["Allondoise", "Algerienne", "Blanche"])
                
            if size and meat and sauce:
                st.write("Order:" + size + meat + " with" + sauce + "sauce")

            code = '''taco = st.button("Make a Taco")
if taco:
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        size = st.radio("Choose a size",["mini", "une viande", "deux viandes"])
    with col_2:
        meat = st.multiselect("Choose the meat",["Poulet panné", "Cordon bleu", "kebab"])
    with col_3:
        sauce = st.multiselect("Choose the sauce",["Allondoise", "Algerienne", "Blanche"])
    if size and meat and sauce:
        st.write("Order:" + size + meat + "with" + sauce + "sauce")'''
            st.code(code, language='python')

#-------- Taco v2
               
        if taco2:
            session_state['taco'] = False
            code = '''taco = st.button("Make a Taco")
if taco2:
    session_state['taco'] = True
    
if session_state['taco'] == True:
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        size = st.radio("Choose a size",["mini", "une viande", "deux viandes"])
    with col_2:
        meat = st.multiselect("Choose the meat",["Poulet panné", "Cordon bleu", "kebab"])
    with col_3:
        sauce = st.multiselect("Choose the sauce",["Allondoise", "Algerienne", "Blanche"])
        
    if size and meat and sauce:
        st.text("You have ordered:")
        st.text(size + " Taco")
        st.text("With " + str(meat))
        st.text("And " + str(sauce) + " Sauce")
'''
            st.code(code, language='python')
            st.error('''KeyError: 'st.session_state has no key "taco". Did you forget to initialize it? 

More info: 

https://docs.streamlit.io/library/advanced-features/session-state#initialization''')

        if taco3:
            session_state['taco'] = True
                
        if session_state['taco'] == True:
            col_1, col_2, col_3 = st.columns(3)
            with col_1:
                size = st.radio("Choose a size",["mini", "une viande", "deux viandes"])
            with col_2:
                meat = st.multiselect("Choose the meat",["Poulet panné", "Cordon bleu", "kebab"])
            with col_3:
                sauce = st.multiselect("Choose the sauce",["Allondoise", "Algerienne", "Blanche"])
                
            if size and meat and sauce:
                st.divider()
                st.text("You have ordered:")
                st.text(size + " Taco")
                st.text("With " + str(meat))
                st.text("And " + str(sauce) + " Sauce")
                st.divider()
            code ='''taco3 = st.button("Make a Taco")
if taco3:
    session_state['taco'] = True
        
if session_state['taco'] == True:
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        size = st.radio("Choose a size",["mini", "une viande", "deux viandes"])
    with col_2:
        meat = st.multiselect("Choose the meat",["Poulet panné", "Cordon bleu", "kebab"])
    with col_3:
        sauce = st.multiselect("Choose the sauce",["Allondoise", "Algerienne", "Blanche"])
        
    if size and meat and sauce:
        st.divider()
        st.text("You have ordered:")
        st.text(size + " Taco")
        st.text("With " + str(meat))
        st.text("And " + str(sauce) + " Sauce")
        st.divider()'''
            st.code(code, language='python')
    
    st.write("session state")
    st.write("placeholder")
    st.write("placeholder")
    if st.button("BigFunction"):
        with st.spinner('loading...'):
            time.sleep(3)


with page3:
    st.write("Page3Selected")
    st.write("Custom componants")
    st.write("placeholder")
    st.write("placeholder")
    st.write("placeholder")
