# import librarys
# import files
from config import *

# page_config, import csv
# st.set_page_config(layout=page_layout,
#                    page_title=app_name,
#                    page_icon=app_icon)
def main():
    background()
    

    # import css
    st.markdown(css_text_subheader, unsafe_allow_html=True)
    st.markdown(css_text_header, unsafe_allow_html=True)
    st.markdown(css_box_false, unsafe_allow_html=True)
    st.markdown(css_box_true, unsafe_allow_html=True)
    st.markdown(css_box_half_true, unsafe_allow_html=True)
    st.markdown(css_button, unsafe_allow_html=True)
    # set columns
    tmp1, main_col, tmp2 = st.columns([1,4,1])

    # session state
    ss = st.session_state
    main_df = pd.read_excel('AOVChamp.xlsx', sheet_name='Info')
    main_df = main_df.sort_values(by=['role', 'champ', 'release_year'])
    image_df = pd.read_excel('AOVChamp.xlsx', sheet_name='Image')

    with main_col:
        st.markdown(f"<div class='header'>{app_name}</div>", unsafe_allow_html=True)

        # initialize random champ
        if 'champ_id_list' not in ss:
            ss.champ_id_list = list(main_df['id'])
            ss.rand = random.randrange(0, len(ss.champ_id_list))
            ss.champ_id_list.pop(ss.rand)
        today_champ_df = main_df[main_df['id'] == ss.rand] # TEST

        # random_num = random.randint(1, len(champ_id_list))

        # champ select box
        champ_list = main_df['champ']
        
        selected_champ_name = st.selectbox(label='', options=champ_list, index=None, placeholder="Chọn tên tướng")

            # if selected_champ_name in ss.champ_list:
            #     ss.champ_list.remove(selected_champ_name)
            # st.write(ss.champ_list)

        # delete champ from selectable
        # # dang thu select tuong nao xoa tuong no trong bang select
        # ss.selectable_df = ss.selectable_df.drop(index=ss.selectable_df[ss.selectable_df['champ'] == selected_champ_name].index)
        # st.dataframe(ss.selectable_df)
        if selected_champ_name is not None:

            global selected_champ_df
            # selected history, guesses
            def update_history(selected_champ_name, main_df, history_df, selected_champ_list):
                global selected_champ_df
                selected_champ_df = main_df[main_df['champ'] == selected_champ_name]
                if selected_champ_name not in selected_champ_list:
                    history_df = pd.concat([selected_champ_df, history_df]).reset_index(drop=True)
                return history_df
            if 'history_df' not in st.session_state:    
                ss.history_df = pd.DataFrame(columns=main_df.columns)
            selected_champ_list = list(ss.history_df['champ'])
            ss.history_df = update_history(selected_champ_name, main_df, ss.history_df, selected_champ_list)
            history_df = ss.history_df
            guesses = len(history_df.index)        


            # show img and name, clues
            info_img_col, info_name_col, quote_col, role_col, alias_col, give_up_col  = st.columns([1, 1, 2, 1, 1, 1], gap='small')
            clue1, clue2, clue3, clue4 = 4, 7, 9, 13

            with info_img_col:
                info_img_link = image_df[image_df['id'] == selected_champ_df['id'].values[0]]['image'].values[0]
                st.image(info_img_link, use_column_width=True)

            with info_name_col:
                st.write('')
                st.markdown(f"<div class='subheader'>{selected_champ_name}</div>", unsafe_allow_html=True)
                # show quote
            with quote_col:
                st.write('')
                def disabling():
                    if guesses >= clue1: 
                        return False
                    else: return True
                
                def helping():
                    if guesses < clue1: return f'Đoán {clue1 - guesses} lần nữa để mở khóa.'

                quote_button = st.button(label='Câu nói', help=helping(), disabled=disabling(), key='quote_button')
                if 'clicked_quote' not in ss:
                    ss.clicked_quote = False
                if quote_button or ss.clicked_quote:
                    ss.clicked_quote = True
                    idx = today_champ_df.columns.get_loc('quote')
                    st.markdown(f'<div class=subheader_not_center> "{today_champ_df.iloc[0, idx]}" </div>', unsafe_allow_html=True) # replace with today_champ_df['quote']

            with role_col:
                st.write('')
                
                def disabling():
                    if guesses >= clue2: return False
                    else: return True
                
                def helping():
                    if guesses < clue2: return f'Đoán {clue2 - guesses} lần nữa để mở khóa.'

                role_button = st.button(label='Vai trò', help=helping(), disabled=disabling())
                if 'clicked_role' not in ss:
                    ss.clicked_role = False
                if role_button or ss.clicked_role:
                    ss.clicked_role = True
                    idx = today_champ_df.columns.get_loc('role')
                    st.markdown(f'<div class=subheader_not_center> {today_champ_df.iloc[0, idx]} </div>', unsafe_allow_html=True)# replace with today_champ_df['role']

            with alias_col:
                st.write('')
                
                def disabling():
                    if guesses >= clue3: return False
                    else: return True
                
                def helping():
                    if guesses < clue3: return f'Đoán {clue3 - guesses} lần nữa để mở khóa.'

                alias_button = st.button(label='Biệt danh', help=helping(), disabled=disabling())
                if 'clicked_alias' not in ss:
                    ss.clicked_alias = False
                if alias_button or ss.clicked_alias:
                    ss.clicked_alias = True
                    idx = today_champ_df.columns.get_loc('alias')
                    st.markdown(f'<div class=subheader_not_center> {today_champ_df.iloc[0, idx]} </div>', unsafe_allow_html=True) # replace with today_champ_df['role']

            with give_up_col:
                st.write('')

                def disabling():
                    if guesses >= clue4: return False
                    else: return True
                
                def helping():
                    if guesses < clue4: return f'Đoán {clue4 - guesses} lần nữa để mở khóa.'

                alias_button = st.button(label='Đầu hàng T.T', help=helping(), disabled=disabling())
                if 'clicked_give_up' not in ss:
                    ss.clicked_give_up = False
                if alias_button or ss.clicked_give_up:
                    ss.clicked_give_up = True
                    idx = today_champ_df.columns.get_loc('champ')
                    st.markdown(f'<div class=subheader_not_center> {today_champ_df.iloc[0, idx]} </div>', unsafe_allow_html=True) # replace with today_champ_df['role']

            # when user guesses right
            if selected_champ_df.iloc[0, 0] == today_champ_df.iloc[0, 0]:
                # increase point
                if 'point' not in ss: ss.point = 0
                ss.point += 1
                st.toast(f"Chúc mừng bạn đã đoán trúng {ss.point} lần!!!")
                st.balloons()

                # reset history and show previous champ
                del ss.history_df
                ss.previous_champ_id = selected_champ_df.iloc[0,0]
                ss.previous_champ_name = selected_champ_df.iloc[0,1]

                # make new guess
                ss.rand = random.randrange(0, len(ss.champ_id_list))
                ss.champ_id_list.pop(ss.rand)

                # reset button
                ss.clicked_quote = False
                ss.clicked_role = False
                ss.clicked_alias = False
                ss.clicked_give_up = False
                
                # next round
                st.markdown(f'<div class="subheader_not_center" style="color:#01BC01"> Ấn chọn để bắt đầu lượt tiếp theo</div>', unsafe_allow_html=True)

            if 'previous_champ_id' in ss:
                st.markdown(f'<div class="subheader_not_center"> Tướng lần trước là #{ss.previous_champ_id} {ss.previous_champ_name}</div>', unsafe_allow_html=True)
                st.write('')

            # show elements
            element_cols = st.columns(7)
            with element_cols[0]:
                
                ss.element_cols_index = 2
                st.markdown(f'<div class="subheader"> Giới Tính </div>', unsafe_allow_html=True)
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
                    selected_champ_position = history_df.iloc[index, ss.element_cols_index]
                    today_champ_position = today_champ_df.iloc[0, ss.element_cols_index]
                    selected_champ_position = selected_champ_position.split(', ')
                    today_champ_position = today_champ_position.split(', ')

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

            with element_cols[2]:

                ss.element_cols_index += 1
                st.markdown(f'<div class="subheader"> Tài Nguyên </div>', unsafe_allow_html=True)
                for index in history_df.index:    
                    if history_df.iloc[index, ss.element_cols_index] == today_champ_df.iloc[0, ss.element_cols_index]:
                        st.markdown(f'<div class="true-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="false-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                    st.write('')
                


            with element_cols[3]:
                ss.element_cols_index += 1
                st.markdown(f'<div class="subheader"> Tầm Đánh </div>', unsafe_allow_html=True)
                for index in history_df.index:    
                    selected_champ_range = history_df.iloc[index, ss.element_cols_index]
                    today_champ_range = today_champ_df.iloc[0, ss.element_cols_index]
                    selected_champ_range = selected_champ_range.split(', ')
                    today_champ_range = today_champ_range.split(', ')

                    if history_df.iloc[index, ss.element_cols_index] == today_champ_df.iloc[0, ss.element_cols_index]:
                        st.markdown(f'<div class="true-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                    else:
                        for i in selected_champ_range:
                            if i in today_champ_range:
                                st.markdown(f'<div class="half-true-box">{history_df.iloc[index, ss.element_cols_index]}</div>', unsafe_allow_html=True)
                                break
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
            

            


