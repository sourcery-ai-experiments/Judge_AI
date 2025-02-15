import os
import streamlit as st
import cv2
import mediapipe as mp
from PIL import Image, ImageDraw
import numpy as np
import cv2
import base64

from utils import load_img
from VideoProcessor import PhotoProcessor

st.set_page_config(
    page_title="Judge AI",
    page_icon=":weight_lifter:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.judgeai.com/help",  # ejemplo de como sería una vez montado
        "Report a bug": "https://www.judgeai.com/bug",  # ejemplo de como sería una vez montado
        "About": "# This is JudgeAi. This is our Data Science Final Proyect !",
    },
)


def main_page():
    # st.markdown("# 🏠Home")
    st.sidebar.markdown("# 🏠Home")


def page2():
    # st.markdown("# 🕺Our model")
    st.sidebar.markdown("# 🕺Our model")


def page3():
    # st.markdown("# ⚖️Pre-trained model")
    st.sidebar.markdown("# ⚖️Pre-trained model")


def page4():
    # st.markdown("# 🕵️‍♂️About us")
    st.sidebar.markdown("# 🕵️‍♂️About us")


page_names_to_funcs = {
    "🏠Home": main_page,
    "🕺Our model": page2,
    "⚖️Pre-trained model": page3,
    "🕵️‍♂️About us": page4,
}

# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()

st.markdown(
    "<h1 style='text-align: center; '>Our mission AI</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<hr style='border:2px solid #f3b323; margin-bottom: 0px; margin-top: 0px'>",
    unsafe_allow_html=True,
)
# st.header("Our mission")

st.markdown(
    "<h2 style='text-align: center; '>The origins of Judge AI</h2>",
    unsafe_allow_html=True,
)

st.markdown(
    """<h7 style='text-align: center; '>Introducing our innovative fitness application, Judge AI. This cutting-edge tool is designed to revolutionize your workout routine by providing real-time feedback on your physical training.  
In its current initial phase, Judge AI focuses on perfecting one of the fundamental exercises - the squat. Our advanced technology analyzes your form and awards you points for each successful squat, 
turning your workout into a rewarding experience. But that’s just the beginning! We have ambitious plans for the future. We’re developing a competitive section to bring a new level of excitement and motivation to your fitness journey. 
Imagine challenging yourself against friends, family, or even global users - the possibilities are endless!
Moreover, we’re working on a feature to monitor your daily performance, providing you with valuable insights to help you understand your progress 
and achieve your fitness goals faster.
Join us on this exciting journey and let Judge AI be your personal digital fitness coach!</h7>""",
    unsafe_allow_html=True,
)


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
paths = [
    "data/dataset_train/IMG_5687(2)_008.jpg",
    "data/dataset_train/IMG_5693(1)_005.jpg",
]
processed_images = []


# image = cv2.imread("data/dataset_train/IMG_5687_015.jpg")


# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
for path in paths:
    image = load_img(path)
    new_image = PhotoProcessor().process(image)
    image_rgb = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    processed_images.append(image_rgb)

print(image_rgb.shape)
new_width = 235
new_height = 410
resized_image = cv2.resize(src=image_rgb, dsize=(new_width, new_height))
print(resized_image.shape)

col1, col2, col3, col4 = st.columns([1.5, 1, 1, 1.5])
with col1:
    st.image(processed_images[0], caption="Mark pose created with our model")
with col4:
    st.image(processed_images[1], caption="Mark pose created with a pretrained model")


st.markdown(
    "<h1 style='text-align: center; '>Our next steps</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<hr style='border:1px solid #f3b323; margin-bottom: 0px; margin-top: 0px'>",
    unsafe_allow_html=True,
)


st.markdown(
    "<h2 style='text-align: center; '>The Future of Judge AI</h2>",
    unsafe_allow_html=True,
)


st.markdown(
    """<h7 style='text-align: center; '>As we continue to innovate and expand, Judge AI is set to redefine the landscape of fitness apps. 
Our future plans include the development of a robust competition system connected through the tournament mode and will serve as the judge,
ensuring a fair and objective competition.
This feature will match you with competitors who have similar personal records in the exercises you're competing in, 
adding a thrilling dimension to your fitness journey.
But that's not all! We're also integrating a comprehensive social platform into Judge AI. 
This will include forums for discussion, clubs for shared interests, and even the option to hire a professional coach. 
A friend system will also be in place, fostering a supportive and motivating fitness community.
One of the standout features we're excited about is our competition system where Judge AI itself will be the judge. 
We are introducing two types of competitions: matchmaking competitions and official competitions. 
In matchmaking competitions, competitors can compete online from anywhere. 
In official competitions, such as a powerlifter squat tournament, competitors will gather at a physical location. 
Our AI will include 1 vs 1 mode  that will allow you to compete online with a refined matchmaking considering all the stored data. 
Your personal profile will be a hub of information. 
It will display your all-time stats in a visually appealing and easy-to-understand format. 
Want to see how you stack up against your friends? You'll have the option to compare your stats with theirs, adding a friendly competitive edge
to your workout routine.
Join us as we take fitness to the next level with Judge AI, your ultimate fitness companion!</h7>""",
    unsafe_allow_html=True,
)


st.markdown(
    "<h1 style='text-align: center; '>Our team</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<hr style='border:1px solid #f3b323; margin-bottom: 0px; margin-top: 0px'>",
    unsafe_allow_html=True,
)


# st.markdown(
#     "<h2 style='text-align: left; '>Luis Carretero</h2>",
#     unsafe_allow_html=True,
# )
with open(
    "data/stored_pictures/linkedin-logo-free-download-free-png.webp", "rb"
) as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

with open("data/stored_pictures/github_PNG40.png", "rb") as image_file:
    encoded_string2 = base64.b64encode(image_file.read()).decode()

st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: flex-start;">
        <h2 style='margin-right: 20px;'>Luis Carretero</h2>
        <a href="https://www.linkedin.com/in/luis-carretero-lopez/">
            <img src="data:image/png;base64,{encoded_string}" width="60">
        </a>
        <a href="https://github.com/luiscarlop">
            <img src="data:image/png;base64,{encoded_string2}" width="40" style='margin-left: 20px;'>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)


luis_path = "data/stored_pictures/IMG_4446.jpeg"
luis_image = cv2.imread(luis_path)
lu_rgb = cv2.cvtColor(luis_image, cv2.COLOR_BGR2RGB)
new_width = 265
new_height = 410
resized_image = cv2.resize(src=lu_rgb, dsize=(new_width, new_height))
col5, col6, col7, col8 = st.columns([1.5, 10, 1, 1.5])
with col5:
    st.image(
        resized_image,
    )
with col6:
    st.markdown(
        """<h7 style='text-align: center; '>My name is Luis Carretero, and I am a telecommunications systems technician currently pursuing a degree in
        Telecommunications Systems Engineering at the Polytechnic University of Cartagena (UPCT).
        In addition to my studies, I have extensively trained in Data Science, acquiring skills in data analysis, machine learning, and statistical modeling.
        I am passionate about developing projects in data science and artificial intelligence like Judge AI.
        My comprehensive background in telecommunications and data science equips me with the skills to contribute to innovative solutions and advancements in technology.</h7>""",
        unsafe_allow_html=True,
    )

col9, col10 = st.columns([1, 1])
with col9:
    st.markdown(":e-mail: luiscarretero.tech@gmail.com")


with open(
    "data/stored_pictures/linkedin-logo-free-download-free-png.webp", "rb"
) as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()


st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <h2 style='margin-right: 20px;'>Claudio Desco</h2>
        <a href="https://www.linkedin.com/in/claudio-desco-serrano-b787991a8/">
            <img src="data:image/png;base64,{encoded_string}" width="60">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

claudio_path = "data/stored_pictures/photo.jpg"
cl_image = cv2.imread(claudio_path)
cl_rgb = cv2.cvtColor(cl_image, cv2.COLOR_BGR2RGB)
new_width = 265
new_height = 410
resized_image = cv2.resize(src=cl_rgb, dsize=(new_width, new_height))
col5, col6, col7, col8 = st.columns([1.5, 10, 1, 1.5])
with col5:
    st.image(
        resized_image,
    )

with col6:
    st.markdown(
        """<h7 style='text-align: center; '>I’m Claudio Desco, a professional with a diverse skill set spanning Marketing, Tourism, and Data Science. My solid foundation in marketing,
        enriched by my academic background in Tourism and a bootcamp in Data Science, empowers me to devise strategies that are both innovative and globally relevant. At Judge AI, I leverage my varied expertise,
        using data-driven insights to shape marketing decisions and harnessing the power of artificial intelligence to optimize results. My work is marked by a deep understanding of global trends, an ability to glean meaningful insights from data,
        and the knack to transform these insights into effective marketing strategies. In essence, I embody the power of interdisciplinary proficiency. My unique blend of expertise in Marketing, Tourism, and Data Science, combined with my steadfast
        commitment to innovation at Judge AI, positions me as a trailblazer in my field.</h7>""",
        unsafe_allow_html=True,
    )

col9, col10 = st.columns([1, 1])
with col9:
    st.markdown(":e-mail: claudiodescopersonal@gmail.com")
# st.image(resized_image)

# st.markdown(
#     "<h2 style='text-align: left; '>Noelia Vergara</h2>",
#     unsafe_allow_html=True,
# )
with open(
    "data/stored_pictures/linkedin-logo-free-download-free-png.webp", "rb"
) as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()


st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <h2 style='margin-right: 20px;'>Noelia Vergara</h2>
        <a href="https://www.linkedin.com/in/claudio-desco-serrano-b787991a8/">
            <img src="data:image/png;base64,{encoded_string}" width="60">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)


noe_path = "data/stored_pictures/foto carnet noelia.jpg"
noe_image = cv2.imread(noe_path)
noe_rgb = cv2.cvtColor(noe_image, cv2.COLOR_BGR2RGB)
new_width = 265
new_height = 410
resized_image = cv2.resize(src=noe_rgb, dsize=(new_width, new_height))
col5, col6, col7, col8 = st.columns([1.5, 10, 1, 1.5])
with col5:
    st.image(
        resized_image,
    )

with col6:
    st.markdown(
        """<h7 style='text-align: center; '>As a dynamic and forward-thinking professional, I’ve spent the last 5 years making waves in the marketing and sales industry. Now, I’m channeling my energy into the exciting world of data science.
        This new venture allows me to stretch my skills and set ambitious new targets. Currently, I’m actively updating my networks with the latest developments in my data analysis projects. I’m always open for a chat, so feel free to reach out
        if you have any questions or if there’s anything you’d like to discuss.</h7>""",
        unsafe_allow_html=True,
    )

col9, col10 = st.columns([1, 1])
with col9:
    st.markdown(":e-mail: noeliavergaran@gmail.com")
