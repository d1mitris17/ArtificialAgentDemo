from game import Game
import random


class QAgent:
    def __init__(
        self, alpha=0.5, gamma=0.9, epsilon=1.0, epsilon_min=0.05, epsilon_decay=0.995
    ):
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
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay

    def train(self, episodes):
        for episode in range(episodes):
            self.game.reset()
            done = False
            while not done:
                s = self.game.pos
                if random.random() < self.epsilon:
                    action = random.choice(self.actions)
                else:
                    maxQ = max(self.qTable[(s, _)] for _ in self.actions)
                    possibleActions = [
                        a for a in self.actions if self.qTable[(s, a)] == maxQ
                    ]
                    action = random.choice(possibleActions)

                s2, r, done = self.game.step(action)

                if done:
                    target = r
                else:
                    best_next = max(self.qTable[(s2, a2)] for a2 in self.actions)
                    target = r + self.gamma * best_next

                self.qTable[(s, action)] = (1 - self.alpha) * self.qTable[
                    (s, action)
                ] + self.alpha * target
                self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

    def getMove(self, pos):
        maxQ = max(self.qTable[(pos, a)] for a in self.actions)
        moves = [a for a in self.actions if self.qTable[(pos, a)] == maxQ]
        return random.choice(moves)
