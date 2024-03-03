from config import *

def how_to_play():
    background()
    circle_data = [
        {"color": "#01BC01", "description": "Thông tin trùng khớp"},
        {"color": "#FF8000", "description": "Thông tin trùng khớp một phần"},
        {"color": "#F01818", "description": "Thông tin sai"},
    ]

    # Function to create a styled circle with text description
    def create_circle(color, description):
        return f"""
        <div style="
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background-color: {color};
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            margin: 10px;
            font-family: {font_family};
        ">
            {description}
        </div>
        """

    # Create circles and display descriptions
    st.markdown(f"<div style='color:#FFF; font-size: 40px; font-weight: bold; font-family: {font_family}'> Cách Chơi </div>", unsafe_allow_html=True)
    for circle in circle_data:
        st.markdown(create_circle(circle["color"], circle["description"]), unsafe_allow_html=True)