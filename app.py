#importing streamlit
import streamlit as st

#title
st.title('Addition of two number')

#input for first number
st.text('Enter first number:')
number1 = st.number_input('insert a number')
st.write('First number is', number1)

#input for second number
st.text('Enter second number')
number2 = st.number_input('insert a number')
st.write('Second number is', number2)

#output
st.write('Sum of numbers', number1 + number2)
