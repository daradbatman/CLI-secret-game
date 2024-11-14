from riddles.Riddles import riddles


class RiddleManager:
    def __init__(self, topic):
        self.riddles = iter(riddles.get(topic, []))
        self.currentRiddle = None

    def getNextRiddle(self):
        self.currentRiddle = next(self.riddles, None)
        return self.currentRiddle

    def checkAnswer(self, riddle, answer):
        return riddle["answer"] == answer
