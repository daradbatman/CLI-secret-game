from riddles.Riddles import riddles

'''
This class takes in a topic the player inputs and initializes a list of riddles related to the topic.
The list of riddles is a list of maps each map containing a question and an answer.
When a riddles is answered it retrieves the next riddle. It is also responsible for checking answers to riddles.
'''
class RiddleManager:
    def __init__(self, topic):
        self.riddles = iter(riddles.get(topic, []))
        self.currentRiddle = None

    def getNextRiddle(self):
        self.currentRiddle = next(self.riddles, None)
        return self.currentRiddle

    def checkAnswer(self, riddle, answer):
        return riddle["answer"] == answer
