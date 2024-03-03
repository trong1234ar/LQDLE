from config import *

def about_us():
    background2()
    st.markdown(css_text_subheader, unsafe_allow_html=True)
    st.markdown(f'<div class="subheader_not_center"> Made by Tron </div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subheader_not_center"> Inspired by LoLdle.org </div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subheader_not_center"> Background source: https://wall.alphacoders.com/big.php?i=1103575 </div>', unsafe_allow_html=True)
