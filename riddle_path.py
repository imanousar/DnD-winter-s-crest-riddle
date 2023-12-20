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
Now that you solve riddle 1 you are on your way to the Freljords Peak Inn hotel.
The road though it's not very safe and you should be cautious. 

You should find a for you (Wizard & Horse) to reach the Inn inside the forest
by drawing a line. 

Be careful though. Monsters are also travelling in the area from point to point.
Wolves, bats, trolls are following specific paths every day. Every monster has 
each own path and doesn't mess with other's paths. 

Your goal is to find a way to draw lines connecting you with the inn, each
monster with the same monster and not a single line to overlap with another.

If you overlap with a monster's path on your way to the inn...well you will 
lose some points...

Monsters know their paths very well and they never overlap. If you make a mistake on their paths, well you will still lose points since your strategy was poor.
"""

if st.button("Roll your D20"):
    if user_input == correct_word:
        st.success("Correct!")
        st.write(RIDLLE_2)
        # Display text and image
        st.image("dnd.png")  # Update with your image path
    else:
        st.error(random.choice(error_messages))
        st.image(random.choice(['death_1.png', 'death_2.png', 'death_3.png']))