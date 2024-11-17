from game.RiddleManager import RiddleManager
from game.PhraseRevealer import PhraseRevealer
import os
import json

def runGame():
    # Load topics
    topics = loadThemes()

    # Choose a topic
    topic = getValidTopicInput(topics)

    # Initialize the game components
    riddleManager = RiddleManager(topic)
    phraseRevealer = PhraseRevealer(topics[topic]["secret_phrase"])

    # Solve 5 riddles
    for _ in range(5):
        riddle = riddleManager.getNextRiddle()
        if not riddle:
            break

        if not solveRiddle(riddle, riddleManager, phraseRevealer):
            break

    # Guess the secret phrase
    print("All riddles answered! Now, guess the secret phrase.")
    guessCount = 5
    while guessCount > 0:
        guess = input("Your guess: ").strip().lower()
        if phraseRevealer.checkPhrase(guess):
            print("Congratulations, you've won!")
            return
        else:
            guessCount -= 1
            print(f"Incorrect guess {guessCount} guesses left.")

    print("Game Over. The secret phrase was:", phraseRevealer.secretPhrase)

def getValidTopicInput(topics):
    topic = None
    while topic not in topics:
        print("Available topics:")
        for topic in topics.keys():
            print(f"- {topic.capitalize().replace('_', ' ')}")
        topic = input("Choose a topic: ").strip().lower().replace(' ', '_')
        if topic not in topics:
            print("Invalid topic. Please try again.")
    return topic

def solveRiddle(riddle, riddleManager, phraseRevealer):
    print(riddle["question"])
    attempts = 3

    while attempts > 0:
        answer = input("Your answer: ").strip().lower()
        if riddleManager.checkAnswer(riddle, answer):
            print("Correct!")
            revealed_letter = phraseRevealer.revealNextLetter()
            print(f"Revealed Letter: {revealed_letter}")
            return True
        else:
            attempts -= 1
            print(f"Incorrect! Attempts left: {attempts}")

    print("No more attempts for this riddle.")
    print(f"The correct answer was {riddle['answer'].strip().upper()}")
    return False

def loadThemes():
    themesPath = os.path.join(os.path.dirname(__file__), "themes", "themes.json")

    try:
        with open(themesPath, 'r') as file:
            topics = json.load(file)
            return topics

    except FileNotFoundError:
        print("Error: themes.json file not found")

    except json.JSONDecodeError:
        print("Error: Failed to parse themes.json")