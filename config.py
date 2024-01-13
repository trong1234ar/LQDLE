page_layout = 'wide'
app_name = 'LQdle'

font_family = 'Calibri'
font_subheader_size = 20

box_false_color = '#F01818'
box_true_color = '#01BC01'
box_half_true_color = '#FF8000'

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
        }}
    </style>
    """
