from config import *
from main import *
from about_us import *
from rule import *
st.set_page_config(layout=page_layout,
                   page_title=app_name,
                   page_icon=app_icon)

local_css('style.css')

with st.sidebar:
    selected = option_menu(
            menu_title=None,
            options=["Trang Chính", "Cách Chơi", "Giới Thiệu"],
            icons=["house", 'book', 'info'],
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#FFFFFF"},
                "icon": {"color": "#7FC7D9", "font-size": "18px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#DCF2F1",
                    "font-family": "Candara",
                },
                "nav-link-selected": {"background-color": "#365486"},
                },
            )
    with st.form(key='email_form'):

        st.markdown('''Hòm thư góp ý''')
        st.markdown('''Trước khi gửi thư, vào \'Google Account settings\', chọn \'Security\', 
                    và ấn chọn \'Less secure app access\'.''')

        email_sender = st.text_input('Email')
        password = st.text_input('Mật khẩu', type="password")
        title = st.text_input('Tiêu Đề')
        body = st.text_input('Nội Dung')
        founder = ['trong224466@gmail.com']

        submit_button = st.form_submit_button('Gửi')
        if submit_button:
            try:
                # Create the email
                msg = MIMEMultipart()
                msg['From'] = email_sender
                msg['To'] = ', '.join(founder)
                msg['Subject'] = 'LQDLE----------' + title
                msg.attach(MIMEText(body))

                #Create the SMTP server
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(email_sender, password)

                # Send the email
                s.send_message(msg)
                st.success('Gửi email thành công')

                s.quit()

            except Exception as error:
                st.error(f'Lỗi khi gửi thư: {error}')

if selected == "Trang Chính":
    main()
elif selected == "Giới Thiệu":
    about_us()
elif selected == "Cách Chơi":
    how_to_play()