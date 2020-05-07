import streamlit as st

def main():
    st.image('CabreiraLogo.png')
    st.title('Codenation')

    st.markdown('Button')
    button = st.button('Button Name')
    if button:
        st.markdown('ON')

    st.markdown('checkbox')
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('ON')

    st.markdown('Radio')
    radio = st.radio('Chose Options', ('Option 1', 'Option 2') )
    if radio == 'Option 1':
        st.markdown('Option 1')
    if radio == 'Option 2':
        st.markdown('Option 2')

    st.markdown('SelectBox')
    select = st.selectbox('Choose option', ('Option 1', 'Option 2'))
    if select == 'Option 1':
        st.markdown('Option 1')
    if select == 'Option 2':
        st.markdown('Option 2')

    st.markdown('Multiselect')
    multi = st.multiselect('Choose:', ('Option 1' , 'Option 2'))
    if multi == 'Option 1':
        st.markdown('Option 1')
    if multi == 'Option 2':
        st.markdown('Option 2')

    st.markdown('File Uploader')
    file = st.file_uploader('Upload File', type ='csv')
    if file is not None:
        st.markdown('Not empty')




if __name__ == '__main__':
    main()
