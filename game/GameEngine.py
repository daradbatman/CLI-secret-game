from game.RiddleManager import RiddleManager
from game.PhraseRevealer import PhraseRevealer
import themes


def startGame():
    # Choose a topic
    topic = input("Choose a topic (nature, mythology): ").strip().lower()
    if topic not in themes:
        print("Invalid topic.")
        return

    # Initialize the game components
    riddleManager = RiddleManager(topic)
    phraseRevealer = PhraseRevealer(themes[topic]["secret_phrase"])

    # Solve 5 riddles
    for _ in range(5):
        riddle = riddleManager.getNextRiddle()
        if not riddle:
            break

        print(riddle["question"])
        attempts = 3

        while attempts > 0:
            answer = input("Your answer: ").strip().lower()
            if riddleManager.checkAnswer(riddle, answer):
                print("Correct!")
                revealed_letter = phraseRevealer.revealNextLetter()
                print(f"Revealed Letter: {revealed_letter}")
                break
            else:
                attempts -= 1
                print(f"Incorrect! Attempts left: {attempts}")

        if attempts == 0:
            print("No more attempts for this riddle.")

    # Guess the secret phrase
    print("All riddles solved! Now, guess the secret phrase.")
    for _ in range(5):
        guess = input("Your guess: ").strip().lower()
        if phraseRevealer.checkPhrase(guess):
            print("Congratulations, you've won!")
            return
        else:
            print("Incorrect guess.")

    print("Game Over. The secret phrase was:", phraseRevealer.secretPhrase)
