import pandas as pd
import random 
import streamlit as st
import traceback
import time
from streamlit_option_menu import option_menu
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import base64

# https://wall.alphacoders.com/big.php?i=1103575
page_layout = 'wide'
app_name = 'LQuizz'
app_icon = 'image/logo.png'
font_family = 'Calibri'
font_subheader_size = 20
font_header_size = 40
font_color = '#fffaf0 '

box_false_color = '#F01818'
box_true_color = '#01BC01'
box_half_true_color = '#FF8000'

def local_css(file_name):#func to read css file -> create flake
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode()

def background():
    bg_img = get_img_as_base64("image/bg2.jpg")
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{bg_img}");
    background-size: 100%;
    background-repeat: no-repeat;
    background-attachment: fixed;
    
    }}
    [data-testid="stAppViewContainer"] > .main::before {{
        content: "";
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background-color: rgba(0, 0, 0, 0.75);
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
def background2():
    color = '#04293A'
    page_bg_color = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-color: {color};
    }}
    """
    st.markdown(page_bg_color, unsafe_allow_html=True)


css_box_false = f"""
    <style>
        .false-box {{
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: {box_false_color};
            height: 100px;
            padding: 20px;
            border-radius: 10px;
            color: white;
            font-family: {font_family};
            font-size: 20px;
        }}
    </style>
    """
css_box_true = f"""
    <style>
        .true-box {{
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: {box_true_color};
            height: 100px;
            padding: 20px;
            border-radius: 10px;
            color: white;
            font-family: {font_family};
            font-size: 20px;
            text-align: center;
        }}
    </style>
    """
css_box_half_true = f"""
    <style>
        .half-true-box {{
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: {box_half_true_color};
            height: 100px;
            padding: 20px;
            border-radius: 10px;
            color: white;
            font-family: {font_family};
            font-size: 20px;
            text-align: center;
        }}
    </style>
    """

css_text_subheader = f"""
    <style>
        .subheader {{
            font-family: {font_family};
            font-size: {font_subheader_size}px;
            font-weight: bold;
            color: {font_color};
            text-align: center
        }}
        .subheader_not_center {{
            font-family: {font_family};
            font-size: {font_subheader_size}px;
            font-weight: light;
            color: {font_color};
        }}
    </style>
    """
css_text_header = f"""
    <style>
        .header {{
            font-family: {font_family};
            font-size: {font_header_size}px;
            font-weight: bold;
            color: {font_color};
            text-align: center
        }}
    </style>
    """

css_button = f"""
    <style>
        .st-emotion-cache-7ym5gk:disabled, .st-emotion-cache-7ym5gk:disabled:hover, .st-emotion-cache-7ym5gk:disabled:active {{
        border-color: rgba(255, 255, 255, 0.4);
        background-color: transparent;
        color: rgba(255, 255, 255, 0.4);
        cursor: not-allowed;
    
        }}
    </style>
"""
