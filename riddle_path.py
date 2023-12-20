import streamlit as st
import random


error_messages = [ "I'm sorry you rolled a 1. A dragon ate you alive for breakfast.",
    "Oops, looks like the goblins stole your correct letters.",
    "A wizard has cast a spell of confusion! That's the wrong word.",
    "The rogue sneaked in and changed the letters. Try again.",
    "The bard distracted you and you mistyped. Sing a tune and try again.",
    "A magical barrier blocks your path. The right word is the key."]

# Define the correct word
correct_word = "freljordspeakinn"  # Replace with your correct 16-letter word


# Streamlit application layout
st.title("Winter Crest - DnD - Riddle No 2")
user_input = st.text_input("Enter the 16-letter word which solves the riddle here (capitals, spaces doesn't matter just correct vocabulary):", "")

user_input = user_input.strip().replace(" ", "").lower()

if st.button("Roll your D20"):
    if user_input == correct_word:
        st.success("Correct!")
        st.write("Here's your text and image.")
        # Display text and image
        st.image("dnd.png")  # Update with your image path
    else:
        st.error(random.choice(error_messages))

        