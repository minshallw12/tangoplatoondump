class GuessingGame:

    def __init__(self, target):
        self.target = target
        self.solved = False

    def guess(self, number):
        if number == self.target:
            self.solved = True
            return f"{number} was correct!"
        if number > self.target:
            return f"{number} is too high. Try again."
        if number < self.target:
            return f"{number} is too low. Try again."
    
    def solved(self):
        return self.solved
        
        
game = GuessingGame(10)



print(game.solved)

print(game.guess(5))
print(game.guess(20))
print(game.solved)

print(game.guess(10))
print(game.solved)