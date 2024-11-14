import random as random


class PhraseRevealer:
    def __init__(self, secretPhrase):
        self.secretPhrase = secretPhrase
        self.revealedPhrase = ["_" if char.isalpha() else char for char in secretPhrase]

    def revealNextLetter(self):
        unrevealedIndexes = [i for i, char in enumerate(self.revealedPhrase) if char == "_"]

        if not unrevealedIndexes:
            return "".join(self.revealedPhrase)  # All letters revealed

        revealIndex = random.choice(unrevealedIndexes)
        self.revealedPhrase[revealIndex] = self.secretPhrase[revealIndex]
        return "".join(self.revealedPhrase)

    def checkPhrase(self, guess):
        return guess.lower() == self.secretPhrase.lower()
