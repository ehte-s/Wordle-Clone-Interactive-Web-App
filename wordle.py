import random

words = {
    4: ["tree", "bear", "wolf", "fish", "lion", "frog", "goat", "duck", "crab", "hawk", "mole", "deer", "seal", "eagle", "dove", "lamb", "kite", "tuna", "puma", "pony"],
    5: ["apple", "grape", "peach", "mango", "lemon", "berry", "melon", "plumb", "olive", "guava", "apric", "lychee", "pearl", "prune", "figgy", "elder", "honey", "cocoa", "candy", "creme"],
    6: ["orange", "banana", "cherry", "tomato", "potato", "pepper", "carrot", "radish", "beetle", "celery", "garlic", "onions", "turnip", "walnut", "almond", "cashew", "pistac", "hazeln", "avocad", "citrus"]
}

def get_random_word(length):
    return random.choice(words[length]) if length in words else None

def give_hint(word, guess):
    hint = ['_' for _ in word]
    for i in range(len(word)):
        if guess[i] == word[i]:
            hint[i] = word[i]
        elif guess[i] in word:
            hint[i] = '?'
    return ' '.join(hint)

def wordle_game():
    print("Welcome to the Wordle Game!")
    word_length = int(input("Enter the number of letters in the word (4, 5, or 6): "))
    word = get_random_word(word_length)

    if word is None:
        print("Sorry, no words of that length are available.")
        return

    attempts = 5
    print(f"You have {attempts} attempts to guess the word.")
    
    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        
        if len(guess) != word_length:
            print(f"Please enter a word with exactly {word_length} letters.")
            continue
        
        if guess == word:
            print("Congratulations! You've guessed the word correctly!")
            return
        else:
            hint = give_hint(word, guess)
            print(f"Hint: {hint}")
            attempts -= 1
            print(f"Attempts remaining: {attempts}")
    
    print(f"Sorry, you've run out of attempts. The word was '{word}'.")

# Run the game
wordle_game()
