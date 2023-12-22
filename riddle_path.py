import streamlit as st
import random
import os 
from constants import RIDLLE_2, error_messages, TITLE, QUESTION, DEATH_CAPTION

correct_word = os.environ.get('SOLUTIOn')


# Streamlit application layout
st.title(TITLE)
user_input = st.text_input(QUESTION, "")

user_input = user_input.strip().replace(" ", "").lower()

st.image("img/dnd_dice.png", width=120)
if st.button("Roll your D20"):
    if user_input == correct_word:
        st.success("Correct!")

        st.write("Please watch the video first")

        st.video("freljord_video.mp4")

        st.write(RIDLLE_2)
        # Display text and image
        st.image("img/dnd_riddle.png")  # Update with your image path
    else:
        st.error(random.choice(error_messages))
        st.image(random.choice(['img/death_'+str(i)+'.png' for i in range(1,7)]), caption=DEATH_CAPTION, use_column_width=True)
