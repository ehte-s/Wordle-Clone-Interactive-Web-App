import streamlit as st
import random

# Word dictionary
WORDS = {
    4: ["tree", "bear", "wolf", "fish", "lion", "frog", "goat", "duck", "crab", "hawk", "mole", "deer", "seal", "eagle", "dove", "lamb", "kite", "tuna", "puma", "pony"],
    5: ["apple", "grape", "peach", "mango", "lemon", "berry", "melon", "plumb", "olive", "guava", "apric", "lychee", "pearl", "prune", "figgy", "elder", "honey", "cocoa", "candy", "creme"],
    6: ["orange", "banana", "cherry", "tomato", "potato", "pepper", "carrot", "radish", "beetle", "celery", "garlic", "onions", "turnip", "walnut", "almond", "cashew", "pistac", "hazeln", "avocad", "citrus"]
}

# Picking random word
def get_random_word(length):
    return random.choice(WORDS[length]) if length in WORDS else None

# Generate Wordle-style hint
def give_hint(word, guess):
    hint = []
    for i in range(len(word)):
        if guess[i] == word[i]:
            hint.append(f"🟩 {guess[i]}")
        elif guess[i] in word:
            hint.append(f"🟨 {guess[i]}")
        else:
            hint.append(f"⬛ {guess[i]}")
    return " ".join(hint)

# Reset game state
def reset_game():
    st.session_state.word = None
    st.session_state.attempts = 5
    st.session_state.history = []

# Streamlit app
def main():
    st.title("🔠 Wordle Clone with Streamlit")
    st.write("A mini project showcasing interactive gameplay with Python & Streamlit.")

    # Session state for persistence
    if "word" not in st.session_state:
        reset_game()

    # Game setup
    if st.session_state.word is None:
        word_length = st.selectbox("Choose word length:", [4, 5, 6])
        if st.button("Start Game"):
            st.session_state.word = get_random_word(word_length)
            st.session_state.attempts = 5
            st.session_state.history = []
            st.success(f"Game started! Guess the {word_length}-letter word.")

    # Game play
    if st.session_state.word:
        st.progress((5 - st.session_state.attempts) / 5)

        # Form allows Enter key to submit + clears input automatically
        with st.form("guess_form", clear_on_submit=True):
            guess = st.text_input(
                "Enter your guess (Press Enter to submit):",
                max_chars=len(st.session_state.word),
                key="guess_input"
            )
            submitted = st.form_submit_button("Submit Guess")

        if submitted:
            guess = guess.lower()
            if len(guess) != len(st.session_state.word):
                st.warning(f"Guess must be {len(st.session_state.word)} letters long.")
            else:
                if guess == st.session_state.word:
                    st.balloons()
                    st.success("🎉 Congratulations! You guessed the word!")
                    st.session_state.word = None
                else:
                    hint = give_hint(st.session_state.word, guess)
                    st.session_state.history.append((guess, hint))
                    st.session_state.attempts -= 1

                    if st.session_state.attempts == 0:
                        st.error(f"❌ Game over! The word was **{st.session_state.word}**.")
                        st.session_state.word = None

        # Display history
        st.subheader("Previous Attempts")
        for g, h in st.session_state.history:
            st.write(f"👉 {g.upper()} → {h}")

    # Play again option
    if st.session_state.word is None and st.button("🔄 Play Again"):
        reset_game()

if __name__ == "__main__":
    main()
