import streamlit as st
import random
ss = st.session_state
if 'lis' not in ss:
    ss.lis = ['a', 'v', 'c', 'd' , 'g']


s = st.button('delete')
if s:
    rand = random.randrange(0, len(ss.lis))
    st.write(f'idx {rand} is deleted')
    ss.lis.pop(rand)
st.write(ss.lis)
