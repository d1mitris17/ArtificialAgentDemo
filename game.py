import random


class Game:
    def __init__(self):
        self.grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.pos = (0, 1)  # A
        self.exited = False
        self.score = 0

    def reset(self):
        self.pos = (0, 1)
        self.exited = False
        self.score = 0
        return self.pos

    def _move(self, direction):
        """Internal: update pos, return reward (usually -1) or 0 if no move."""
        if (
            direction == "N"
            and self.pos[0] > 0
            and self.grid[self.pos[0] - 1][self.pos[1]] == 0
        ):
            if random.random() < 0.1:
                # 10% chance to slip and not move
                return 0
            self.pos = (self.pos[0] - 1, self.pos[1])
            return -1
        elif (
            direction == "S"
            and self.pos[0] < len(self.grid) - 1
            and self.grid[self.pos[0] + 1][self.pos[1]] == 0
        ):
            if random.random() < 0.1:
                # 10% chance to slip and not move
                return 0
            self.pos = (self.pos[0] + 1, self.pos[1])
            return -1
        elif (
            direction == "E"
            and self.pos[1] < len(self.grid[0]) - 1
            and self.grid[self.pos[0]][self.pos[1] + 1] == 0
        ):
            if random.random() < 0.1:
                # 10% chance to slip and not move
                return 0
            self.pos = (self.pos[0], self.pos[1] + 1)
            return -1
        elif (
            direction == "W"
            and self.pos[1] > 0
            and self.grid[self.pos[0]][self.pos[1] - 1] == 0
        ):
            if random.random() < 0.1:
                # 10% chance to slip and not move
                return 0
            self.pos = (self.pos[0], self.pos[1] - 1)
            return -1
        else:
            # invalid move: either 0 or a small penalty
            return 0

    def step(self, action):
        """
        action: "N", "S", "E", "W", or "EXIT"
        returns: (next_state, reward, done)
        """
        if action == "EXIT":
            if self.pos == (1, 2):  # D
                reward = -10
            elif self.pos == (2, 1):  # E
                reward = +10
            else:
                reward = 0  # invalid exit, up to you
            self.score += reward
            self.exited = True
            done = True
        else:
            reward = self._move(action)
            self.score += reward
            done = False

        return self.pos, reward, done
