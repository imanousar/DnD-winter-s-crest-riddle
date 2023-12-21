import streamlit as st
import random
import os 

error_messages = [ "I'm sorry you rolled a 1. A dragon ate you alive for breakfast.",
    "Oops, looks like the goblins stole your correct letters.",
    "A wizard has cast a spell of confusion! That's the wrong word.",
    "The rogue sneaked in and changed the letters. Try again.",
    "The bard distracted you and you mistyped. Sing a tune and try again.",
    "A magical barrier blocks your path. The right word is the key."]

correct_word = os.environ.get('SOLUTION')


# Streamlit application layout
st.title("Winter Crest - DnD - Riddle No 2")
user_input = st.text_input("Enter the 16-letter word which solves the riddle here (capitals, spaces doesn't matter just correct vocabulary):", "")

user_input = user_input.strip().replace(" ", "").lower()

RIDLLE_2 = """
Now that you've solved riddle 1, you are on your way to the Freljords Peak Inn hotel. However, the road is not very safe, and you should be cautious.

Your task is to find a safe path for you (Wizard & Horse) to reach the Inn located inside the forest. This involves drawing a line to chart your course.

Be careful, though. Monsters are also traveling in the area, each following its specific path. Wolves, bats, trolls, and other creatures have their own routes and do not interfere with each other's paths.

Your goal is to draw lines connecting you to the inn and each monster to its kind without any lines overlapping.

If your path overlaps with a monster's path on your way to the inn, you will lose some points. Remember, monsters are familiar with their paths and never overlap. If you make a mistake in plotting their paths, it will be considered a poor strategy, and you will lose points.
"""

if st.button("Roll your D20"):
    if user_input == correct_word:
        st.success("Correct!")
        st.write(RIDLLE_2)
        # Display text and image
        st.image("dnd.png")  # Update with your image path
    else:
        st.error(random.choice(error_messages))
        st.image(random.choice(['death_'+i+'.png' for i in range(1,7)]))