# import librarys
import pandas as pd
import random 
import streamlit as st
import traceback  # Import the traceback module


# import files
from config import *

# page_config, import csv
st.set_page_config(layout=page_layout)
main_df = pd.read_excel('AOVchamp.xlsx')

# import css
st.markdown(css_text_subheader, unsafe_allow_html=True)

st.markdown(css_box_false, unsafe_allow_html=True)
st.markdown(css_box_true, unsafe_allow_html=True)
st.markdown(css_box_half_true, unsafe_allow_html=True)
# set columns
tmp1, main_col, tmp2 = st.columns([1,4,1])

# session state
ss = st.session_state

with main_col:

    st.header(app_name)

    # initialize random champ
    champ_id_list = main_df['id']
    # random_num = random.randint(1, len(champ_id_list))
    today_champ_df = main_df[main_df['id'] == 5] # TEST

    # champ select box
    champ_list = main_df['champ']
    selected_champ_name = st.selectbox('', champ_list)
    
    # selected history
    def update_history(selected_champ_name, main_df, history_df):
        global selected_champ_df 
        selected_champ_df = main_df[main_df['champ'] == selected_champ_name]
        history_df = pd.concat([selected_champ_df, history_df]).reset_index(drop=True)
        return history_df
    
    if 'history_df' not in st.session_state:    
        st.session_state.history_df = pd.DataFrame(columns=main_df.columns)
    ss.history_df = update_history(selected_champ_name, main_df, st.session_state.history_df)

    # show elements
    main_cols = st.columns(7)
    with main_cols[0]:
        
        ss.index = 2
        st.markdown(f'<div class="subheader"> Tên </div>', unsafe_allow_html=True)
        for index in st.session_state.history_df.index:
            if st.session_state.history_df.iloc[index, ss.index] == today_champ_df.iloc[0, ss.index]:
                st.markdown(f'<div class="true-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="false-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            st.write('')

    with main_cols[1]:

        ss.index += 1
        st.markdown(f'<div class="subheader"> Tài Nguyên </div>', unsafe_allow_html=True)
        for index in st.session_state.history_df.index:    
            if st.session_state.history_df.iloc[index, ss.index] == today_champ_df.iloc[0, ss.index]:
                st.markdown(f'<div class="true-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="false-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            st.write('')

    with main_cols[2]:

        ss.index += 1
        st.markdown(f'<div class="subheader"> Vị Trí </div>', unsafe_allow_html=True)
        for index in st.session_state.history_df.index:    
            selected_champ_position = st.session_state.history_df.iloc[index, ss.index]
            today_champ_position = today_champ_df.iloc[0, ss.index]
            selected_champ_position = selected_champ_position.split(' / ')
            today_champ_position = today_champ_position.split(' / ')

            if st.session_state.history_df.iloc[index, ss.index] == today_champ_df.iloc[0, ss.index]:
                st.markdown(f'<div class="true-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            else:
                for i in selected_champ_position:
                    if i in today_champ_position:
                        st.markdown(f'<div class="half-true-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
                        break
                else:
                    st.markdown(f'<div class="false-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            st.write('')


    with main_cols[3]:
        ss.index += 1
        st.markdown(f'<div class="subheader"> Tầm Đánh </div>', unsafe_allow_html=True)
        for index in st.session_state.history_df.index:  
            if st.session_state.history_df.iloc[index, ss.index] == today_champ_df.iloc[0, ss.index]:
                st.markdown(f'<div class="true-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="false-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            st.write('')

    with main_cols[4]:
        ss.index += 1
        st.markdown(f'<div class="subheader"> Nơi Sinh </div>', unsafe_allow_html=True)
        for index in st.session_state.history_df.index:    
            if st.session_state.history_df.iloc[index, ss.index] == today_champ_df.iloc[0, ss.index]:
                st.markdown(f'<div class="true-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="false-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            st.write('')

    with main_cols[5]:
        ss.index += 1
        st.markdown(f'<div class="subheader"> Trang Phục </div>', unsafe_allow_html=True)
        for index in st.session_state.history_df.index:    
            if st.session_state.history_df.iloc[index, ss.index] == today_champ_df.iloc[0, ss.index]:
                st.markdown(f'<div class="true-box">{st.session_state.history_df.iloc[index, ss.index]}</div>', unsafe_allow_html=True)
            elif st.session_state.history_df.iloc[index, ss.index] < today_champ_df.iloc[0, ss.index]:
                st.markdown(f'<div class="false-box">{st.session_state.history_df.iloc[index, ss.index] } ⬆ </div>', unsafe_allow_html=True)
            else: 
                st.markdown(f'<div class="false-box">{st.session_state.history_df.iloc[index, ss.index] } ⬇ </div>', unsafe_allow_html=True)
            st.write('')

    with main_cols[6]:
        ss.index += 1
        st.markdown(f'<div class="subheader"> Năm Ra Mắt </div>', unsafe_allow_html=True)
        for index in st.session_state.history_df.index:    
            if st.session_state.history_df.iloc[index, ss.index] == today_champ_df.iloc[0, ss.index]:
                st.markdown(f'<div class="true-box">{st.session_state.history_df.iloc[0, ss.index]}</div>', unsafe_allow_html=True)
            elif st.session_state.history_df.iloc[index, ss.index] < today_champ_df.iloc[0, ss.index]:
                st.markdown(f'<div class="false-box">{st.session_state.history_df.iloc[index, ss.index] } ⬆ </div>', unsafe_allow_html=True)
            else: 
                st.markdown(f'<div class="false-box">{st.session_state.history_df.iloc[index, ss.index] } ⬇ </div>', unsafe_allow_html=True)
            st.write('')
