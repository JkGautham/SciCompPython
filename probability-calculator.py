import copy
import random

import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn_balls = new_hat.draw(num_balls_drawn)
        
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1
        
        success = all(drawn_count.get(color, 0) >= count for color, count in expected_balls.items())
        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments