from game import Game


class QAgent:
    def __init__(self, alpha=0.5, gamma=0.9):
        self.game = Game()
        self.states = []
        for i in range(len(self.game.grid)):
            for j in range(len(self.game.grid[0])):
                if self.game.grid[i][j] == 0:
                    self.states.append((i, j))
        self.actions = ["N", "S", "E", "W", "EXIT"]
        self.qTable = {}
        for state in self.states:
            for action in self.actions:
                self.qTable[(state, action)] = 0.0
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        # self.epsilon = 0.1  # exploration rate, for epsilon-greedy policy
