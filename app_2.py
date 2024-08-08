import streamlit as st
import random

class Ran:
    def __init__(self):
        self.i = None
        self.r = None

    def guess(self, user_guess):
        self.i = int(user_guess)
        self.r = random.randint(0, 100)

        if self.r > self.i:
            st.write(f"System generated number: {self.r}")
            st.write("System wins!")
        elif self.r == self.i:
            st.write(f"System generated number: {self.r}")
            st.write("Match Tie")
        else:
            st.write(f"System generated number: {self.r}")
            st.write("You Win!")

# Create an instance of the game
game = Ran()

# Streamlit interface
st.title('Number Guessing Game')
user_input = st.number_input('Enter your guess (between 0 and 100):', min_value=0, max_value=100, step=1)
if st.button('Guess'):
    game.guess(user_input)
