

class GuessingGame:

    def __init__(self, answer, solved=False):
        self._answer = answer
        self._solved = solved

    def solved(self):
        return self._solved

    def guess(self, number):
        if number >self._answer:
            return 'high'
        elif number < self._answer:
            return 'low'
        else:
            self._solved = True
            return 'correct'
            
game5 = GuessingGame('a')
game1 = GuessingGame(10)
game2 = GuessingGame(1)
game3 = GuessingGame(-30)
game4 = GuessingGame(100)
game4 = GuessingGame(0)

print(game1.solved())
print(game1.guess(5))
print(game1.guess(23))
print(game1.guess(9))
print(game1.guess(10))
print(game1.solved())
print(game2.solved())
print(game2.guess(1))
print(game2.solved())