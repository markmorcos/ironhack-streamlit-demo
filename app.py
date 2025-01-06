import streamlit as st
from utils import COLORS, ANIMALS, SUPERPOWERS, MOTTOS, get_power_description, generate_random_name
import random

# Set up the page
st.set_page_config(
    page_title="Superhero Name Generator",
    layout="centered",
    page_icon="🦸‍♂️",
)

# Set page title and description
st.title("🦸‍♂️ Superhero Name Generator")
st.write("Create your unique superhero identity!")

# Create input components
favorite_color = st.text_input("What's your favorite color?", "Blue", help="Try one of these: " + ", ".join(COLORS))
favorite_animal = st.text_input("What's your favorite animal?", "Wolf", help="Try one of these: " + ", ".join(ANIMALS))
lucky_number = st.number_input("Choose your lucky number", min_value=1, max_value=100, value=7)
superpower = st.selectbox(
    "Select your superpower",
    SUPERPOWERS,
    help="Each power comes with unique abilities!"
)

# Show power description
st.info(get_power_description(superpower))

# Generate superhero name and profile
if st.button("Generate Superhero Profile"):
    # Generate superhero name
    superhero_name = f"The {favorite_color} {favorite_animal} of {lucky_number}"
    
    # Display superhero profile in a cool box
    st.markdown("---")
    st.markdown("### 🦸‍♂️ Your Superhero Profile")
    st.markdown(f"**Superhero Name:** {superhero_name}")
    st.markdown(f"**Superpower:** {superpower}")
    
    # Generate random motto
    motto = random.choice(MOTTOS)
    st.markdown(f"**Motto:** _{motto}_")
    
    # Add some flair
    st.balloons()
