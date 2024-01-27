# import librarys
import pandas as pd
import random 
import streamlit as st
import traceback
import time

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
    main_df = pd.read_excel('AOVchamp.xlsx')
    # initialize random champ
    champ_id_list = main_df['id']
    # random_num = random.randint(1, len(champ_id_list))
    today_champ_df = main_df[main_df['id'] == 5] # TEST

    # champ select box
    champ_list = main_df['champ']
    selected_champ_name = st.selectbox(label='', options=champ_list, index=None, placeholder="Chọn tên tướng")
    if selected_champ_name is not None:

        # selected history
        def update_history(selected_champ_name, main_df, history_df):
            global selected_champ_df 
            selected_champ_df = main_df[main_df['champ'] == selected_champ_name]
            history_df = pd.concat([selected_champ_df, history_df]).reset_index(drop=True)
            return history_df
        
        if 'history_df' not in st.session_state:    
            ss.history_df = pd.DataFrame(columns=main_df.columns)
        ss.history_df = update_history(selected_champ_name, main_df, ss.history_df)
        history_df = ss.history_df
        
        # show img and name
        info_img_col, info_name_col, tmp = st.columns([1, 1, 3])
        with info_img_col:
            st.write('this iss image')
        
        with info_name_col:
            st.markdown(f'<div class="subheader"> {selected_champ_df.iloc[0, 1]} </div>', unsafe_allow_html=True)
        
        # point when user guesses right
        if selected_champ_df.iloc[0, 0] == today_champ_df.iloc[0, 0]:
            if 'point' not in ss: ss.point = 0
            ss.point += 1

            del ss.history_df
            st.toast(f"Congrats on your {ss.point} successes")
            st.balloons()
            ss.previous_champ_id = selected_champ_df.iloc[0,0]
            ss.previous_champ_name = selected_champ_df.iloc[0,1]
            st.write(f'Last champ was #{ss.previous_champ_id} {ss.previous_champ_name}')

        # show elements
        element_cols = st.columns(7)
        with element_cols[0]:
            
            ss.element_cols_index = 2
            st.markdown(f'<div class="subheader"> Tên </div>', unsafe_allow_html=True)
            for index in history_df.index:
                if history_df.iloc[index, ss.element_cols_index] == today_champ_df.iloc[0, ss.element_cols_index]:
                    st.markdown(f'<div class="true-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="false-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                st.write('')

        with element_cols[1]:

            ss.element_cols_index += 1
            st.markdown(f'<div class="subheader"> Vị Trí </div>', unsafe_allow_html=True)
            for index in history_df.index:    
                if history_df.iloc[index, ss.element_cols_index] == today_champ_df.iloc[0, ss.element_cols_index]:
                    st.markdown(f'<div class="true-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="false-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                st.write('')

        with element_cols[2]:

            ss.element_cols_index += 1
            st.markdown(f'<div class="subheader"> Tài Nguyên </div>', unsafe_allow_html=True)
            for index in history_df.index:    
                selected_champ_position = history_df.iloc[index, ss.element_cols_index]
                today_champ_position = today_champ_df.iloc[0, ss.element_cols_index]
                selected_champ_position = selected_champ_position.split(' / ')
                today_champ_position = today_champ_position.split(' / ')

                if history_df.iloc[index, ss.element_cols_index] == today_champ_df.iloc[0, ss.element_cols_index]:
                    st.markdown(f'<div class="true-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                else:
                    for i in selected_champ_position:
                        if i in today_champ_position:
                            st.markdown(f'<div class="half-true-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                            break
                    else:
                        st.markdown(f'<div class="false-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                st.write('')


        with element_cols[3]:
            ss.element_cols_index += 1
            st.markdown(f'<div class="subheader"> Tầm Đánh </div>', unsafe_allow_html=True)
            for index in history_df.index:  
                if history_df.iloc[index, ss.element_cols_index] == today_champ_df.iloc[0, ss.element_cols_index]:
                    st.markdown(f'<div class="true-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="false-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                st.write('')

        with element_cols[4]:
            ss.element_cols_index += 1
            st.markdown(f'<div class="subheader"> Nơi Sinh </div>', unsafe_allow_html=True)
            for index in history_df.index:    
                if history_df.iloc[index, ss.element_cols_index] == today_champ_df.iloc[0, ss.element_cols_index]:
                    st.markdown(f'<div class="true-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="false-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                st.write('')

        with element_cols[5]:
            ss.element_cols_index += 1
            st.markdown(f'<div class="subheader"> Trang Phục </div>', unsafe_allow_html=True)
            for index in history_df.index:    
                if history_df.iloc[index, ss.element_cols_index] == today_champ_df.iloc[0, ss.element_cols_index]:
                    st.markdown(f'<div class="true-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                elif history_df.iloc[index, ss.element_cols_index] < today_champ_df.iloc[0, ss.element_cols_index]:
                    st.markdown(f'<div class="false-box">{history_df.iloc[index, ss.element_cols_index] } ⬆ </div>', unsafe_allow_html=True)
                else: 
                    st.markdown(f'<div class="false-box">{history_df.iloc[index, ss.element_cols_index] } ⬇ </div>', unsafe_allow_html=True)
                st.write('')

        with element_cols[6]:
            ss.element_cols_index += 1
            st.markdown(f'<div class="subheader"> Năm Ra Mắt </div>', unsafe_allow_html=True)
            for index in history_df.index:    
                if history_df.iloc[index, ss.element_cols_index] == today_champ_df.iloc[0, ss.element_cols_index]:
                    st.markdown(f'<div class="true-box">{history_df.iloc[0, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                elif history_df.iloc[index, ss.element_cols_index] < today_champ_df.iloc[0, ss.element_cols_index]:
                    st.markdown(f'<div class="false-box">{history_df.iloc[index, ss.element_cols_index] } ⬆ </div>', unsafe_allow_html=True)
                else: 
                    st.markdown(f'<div class="false-box">{history_df.iloc[index, ss.element_cols_index] } ⬇ </div>', unsafe_allow_html=True)
                st.write('')
        

        
    

    