# 🔠 Wordle Clone Interactive Web App

A fun, interactive word-guessing game built with Python and Streamlit, inspired by the popular Wordle game. Test your vocabulary skills by guessing mystery words of different lengths!

## ✨ Features

- **Multiple word lengths**: Choose between 4, 5, or 6-letter words
- **Wordle-style feedback**: Visual hints with colored emojis
  - 🟩 Correct letter in correct position
  - 🟨 Correct letter in wrong position
  - ⬛ Letter not in the word
- **Progress tracking**: Visual progress bar and attempt counter
- **Game history**: View all your previous guesses and hints
- **Interactive UI**: Clean, responsive interface with form submissions
- **Celebratory effects**: Balloon animation when you win!

## 🎮 How to Play

1. **Start a Game**: Select your preferred word length (4, 5, or 6 letters) and click "Start Game"
2. **Make Guesses**: Type your guess in the input field and press Enter or click "Submit Guess"
3. **Read the Hints**: Use the colored feedback to guide your next guess
4. **Win or Lose**: You have 5 attempts to guess the correct word
5. **Play Again**: Click "🔄 Play Again" to start a new round

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Streamlit

### Installation

1. Clone this repository or download the script
2. Install the required dependency:
   ```bash
   pip install streamlit
   ```

### Running the Game

```bash
streamlit run app.py
```

The game will open in your default web browser at `http://localhost:8501`

## 📝 Code Structure

- **Word Dictionary**: Curated lists of words for each length category
- **Game Logic**: Core functions for word selection, hint generation, and game state management
- **Streamlit Interface**: Interactive web interface with session state management
- **Form Handling**: Clean input handling with automatic form clearing

## 🎯 Game Rules

- Each word length has its own curated word list
- You get exactly 5 attempts to guess the word
- Guesses must match the exact length of the target word
- All guesses are case-insensitive
- The game tracks your progress and shows all previous attempts

## 🔧 Customization

You can easily customize the game by:

- Adding more words to the `WORDS` dictionary
- Changing the number of allowed attempts
- Modifying the visual feedback emojis
- Adding new word length categories

## 📦 Dependencies

- `streamlit`: Web app framework for the interactive interface
- `random`: Built-in Python module for word selection

## 🎨 Interface Preview

The game features:
- Clean, modern interface with emoji decorations
- Progress bar showing completion percentage
- Form-based input with Enter key support
- Color-coded feedback system
- Game history display
- Responsive design that works on desktop and mobile

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional word categories
- Enhanced UI/UX features
- Performance optimizations
- Bug fixes

## 📄 License

This project is open source and available under the MIT License.

---

**Enjoy the game and happy word guessing!** 🎉
