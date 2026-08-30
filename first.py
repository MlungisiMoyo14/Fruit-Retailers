import streamlit as st

st.title('Fruit Retailers')
st.write('Here are our best-sellers')

name = st.text_input('Enter your name: ')
choice = st.selectbox('Choose fruit:', ['bananas', 'apples', 'pineapples'])

prices = {
    'bananas': 'R11.53',
    'apples': 'R9.70',
    'pineapples': 'R7.58'
}
if st.button('Check price'):
    if not name:
        st.warning('Please enter your name first')
else:
    st.success(f'Hello {name}, you chose {choice}, this will cost you {prices[choice]}')
    purchase = st.radio('Would you like to purchase it?', ('Yes', 'No'))
    if purchase == 'Yes':
        st.balloons()
        st.write('Feel free to purchase in our retail stores')
    else:
        st.write('No worries, feel free to purchase when you are ready')
st.write('Thank you for shopping at Fruit Retailers')
