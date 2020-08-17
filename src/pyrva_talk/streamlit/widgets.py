import streamlit as st


# with st.echo():
#     selected = st.checkbox('Checkbox')
#     st.write(selected)
# with st.echo():
#     selection = st.radio('Radio', ['PyRVA', 'rvatech'])
#     st.write(selection)
# with st.echo():
#     selection = st.selectbox('Select Box', ['PyRVA', 'rvatech'])
#     st.write(selection)
# with st.echo():
#     selections = st.multiselect('Multi Select', ['PyRVA', 'rvatech'], ['PyRVA', 'rvatech'])
#     st.write(selections)
with st.echo():
    value = st.slider('Slider', 1, 11, 11)
    st.write(value)
with st.echo():
    values = st.slider('Range Slider', 1, 10, (3, 8))
    st.write(values)
with st.echo():
    text = st.text_input('Text', ['PyRVA', 'rvatech'][0])
    st.write(text)
with st.echo():
    file = st.file_uploader('File')
    st.write(file)
