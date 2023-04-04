import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 82, 33)
GREY = (220, 220, 220)
DARKGREY = (128, 128, 128)
GREENGREY = (125, 164, 120)
RED = (160, 27, 16)
REDGREY = (182, 128, 109)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
GOLD = (230, 230, 138)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

OFFSET = (10, 65)

NODE_W = 15

class Grid:
    def __init__(self, ui=False):
        self.width = 25
        self.height = 25
        self.nodes = {(i, j): Node((i, j)) for i in range(self.height) for j in range(self.width)}
        self.row_range = self.height
        self.col_range = self.width
        self.reset_full()
        self.random()

    def save(self, filename):
        grid_str = ""
        for row in range(self.height):
            for col in range(self.width):
                node = self.nodes[(row, col)]
                if node.puddle:
                    grid_str += "P"
                elif node.grass:
                    grid_str += "G"
                elif node.start:
                    grid_str += "S"
                elif node.goal:
                    grid_str += "E"
                else:
                    grid_str += "."

                grid_str += " "

        with open(filename, "w") as file:
            file.write(grid_str)

    def load(self, grid_str):
        for i, s in enumerate(grid_str.split()):
            row = i // self.width
            col = i - (row * self.width)
            coord = (row, col)

            node = self.nodes[coord]
            node.reset_full()

            if s == "P":
                node.make_puddle()
            elif s == "G":
                node.make_grass()
            elif s == "S":
                self.set_start(coord)
            elif s == "E":
                self.set_goal(coord)

    def reset(self):
        for coord in self.nodes:
            self.nodes[coord].reset()

    def reset_full(self):
        for coord in self.nodes:
            self.nodes[coord].reset_full()

    def random_clear(self):
        self.reset_full()

        start = random.choice(list(self.nodes.keys()))
        goal = random.choice(list(self.nodes.keys()))
        while goal == start:
            goal = random.choice(list(self.nodes.keys()))

        self.set_start(start)
        self.set_goal(goal)

    def set_start(self, start):
        new_start = self.nodes[start]
        if not new_start.goal:
            for node in self.nodes.values():
                if node.start:
                    node.reset_full()
            new_start.reset_full()
            new_start.start = True
            self.start = start

    def set_goal(self, goal):
        new_goal = self.nodes[goal]
        if not new_goal.start:
            for node in self.nodes.values():
                if node.goal:
                    node.reset_full()
            new_goal.reset_full()
            new_goal.goal = True
            self.goal = goal

    def random(self):
        self.random_clear()

        for node in self.nodes.values():
            node.random_puddle()
            node.random_grass()

    def update(self, game, pygame):
        self.nodes[self.start].start = True
        self.nodes[self.goal].goal = True
        for node in self.nodes.values():
            node.update(game,pygame)
        for i in range(self.width + 1):
            pygame.draw.line(game.screen, [100]*3, (NODE_W*i + OFFSET[0], OFFSET[1]), (NODE_W*i + OFFSET[0], OFFSET[1] + NODE_W * self.height))
        for i in range(self.height + 1):
            pygame.draw.line(game.screen, [100]*3, (OFFSET[0], (NODE_W*i)+OFFSET[1]), (OFFSET[0] + NODE_W * self.width, (NODE_W*i)+OFFSET[1]))

    def clear_path(self):
        for node in self.nodes.values():
            node.reset()

class Node():
    def __init__(self, pos):
        self.pos = pos
        self.reset_full()

    def reset_full(self):
        self.reset()
        self.puddle = False
        self.grass = False
        self.start = False
        self.goal = False

    def reset(self):
        self.color_in_path = False
        self.color_checked = False
        self.color_frontier = False

    def get_rect(self, pygame):
        blit_pos = [self.pos[1]*NODE_W + OFFSET[0], self.pos[0]*NODE_W + OFFSET[1]]
        image = pygame.Surface((NODE_W, NODE_W))
        return image, image.get_rect(topleft=blit_pos)

    def update(self, game, pygame):
        image, rect = self.get_rect(pygame)

        color = BLACK
        #The order of these lines is important
        if self.puddle:
            color = BLUE
        elif self.start:
            color = YELLOW
        elif self.goal:
            color = ORANGE
        elif self.color_in_path:
            color = RED
            if self.grass:
                color = REDGREY
        elif self.color_frontier:
            color = GREY
        elif self.color_checked:
            color = DARKGREY
            if self.grass:
                color = GREENGREY
        elif self.grass:
            color = GREEN
        else:
            color = BLACK

        image.fill(color)

        game.screen.blit(image, rect)

    def make_puddle(self):
        if not self.goal and not self.start:
            self.reset_full()
            self.puddle = True

    def make_grass(self):
        if not self.goal and not self.start:
            self.reset_full()
            self.grass = True

    def clear(self):
        if not self.goal and not self.start:
            self.reset_full()

    def random_puddle(self):
        if not random.randint(0,8): 
            self.make_puddle()

    def random_grass(self):
        if not random.randint(0,3):
            self.make_grass()

    def cost(self):
        if self.grass:
            return 10
        else:
            return 1
