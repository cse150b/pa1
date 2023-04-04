import sys, random
from ai import AI
from game import Grid, WHITE, BLACK, NODE_W, OFFSET
from test import test
import argparse
random.seed(0)

class GridWorld():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Grid World")
        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()
        self.screen_res = [400, 470]
        self.font = pygame.font.SysFont("Calibri", 12)
        self.screen = pygame.display.set_mode(self.screen_res, pygame.HWSURFACE, 32)
        self.show_checked = True
        self.quit = False
        self.type = "dfs"
        self.grid = Grid(True)
        self.ai = AI(self.grid, self.type)
        self.run = False
        self.pause = False

    def loop(self):
        while True:
            self.draw()
            self.clock.tick(60)
            self.mpos = pygame.mouse.get_pos()
            if self.run and not self.pause:
                if self.ai.finished:
                    if not self.ai.failed:
                        self.ai.get_result()
                    self.run = False
                else:
                    self.ai.make_step()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_c:
                        self.ai.set_search()
                        self.run = False
                    if event.key == K_RETURN:
                        if not self.run:
                            self.ai.set_search()
                            self.run = True
                            self.pause = False
                        else:
                            self.pause = not self.pause
                    if event.key == K_1:
                        if self.type != 'dfs':
                            self.grid.clear_path()
                            self.run = False
                            self.pause = False
                        self.type = "dfs"
                        self.ai.set_type(self.type)
                    if event.key == K_2:
                        if self.type != 'bfs':
                            self.grid.clear_path()
                            self.run = False
                            self.pause = False
                        self.type = "bfs"
                        self.ai.set_type(self.type)
                    if event.key == K_3:
                        if self.type != 'ucs':
                            self.grid.clear_path()
                            self.run = False
                            self.pause = False
                        self.type = "ucs"
                        self.ai.set_type(self.type)
                    if event.key == K_4:
                        if self.type != 'astar':
                            self.grid.clear_path()
                            self.run = False
                            self.pause = False
                        self.type = "astar"
                        self.ai.set_type(self.type)
                    if not self.run:
                        if event.key == K_w:
                            self.grid.save("saved_grid")
                        if event.key == K_l:
                            try:
                                with open("saved_grid") as file:
                                    self.grid.load(file.read())
                            except:
                                print("no saved file present")
                        if event.key == K_m:
                            self.grid.random()
                        if event.key == K_n:
                            self.grid.random_clear()
                        for node in self.grid.nodes.values():
                            if node.get_rect(pygame)[1].collidepoint(game.mpos):
                                if event.key == K_p:
                                    self.grid.reset()
                                    node.make_puddle()
                                if event.key == K_r:
                                    self.grid.reset()
                                    node.make_grass()
                                if event.key == K_x:
                                    self.grid.reset()
                                    node.clear()
                                if event.key == K_s:
                                    self.grid.reset()
                                    self.grid.set_start(node.pos)
                                if event.key == K_g:
                                    self.grid.reset()
                                    self.grid.set_goal(node.pos)

    def blitInfo(self):
        line1 = self.font.render("Esc: exit; Enter: search/pause; c: clear path; m: random board (clear first)", 1, WHITE, BLACK)
        line2 = self.font.render("s: place start; g: place goal; p: place puddle; r: place grass; x: clear node", 1, WHITE, BLACK)
        line3 = self.font.render("w: save board; l: load board, n: no obstacles", 1, WHITE, BLACK)
        line4 = self.font.render("1: DFS, 2: BFS, 3: UCS, 4: A*", 1, WHITE, BLACK)
        if self.ai.finished and not self.ai.failed:
            score = str(self.ai.final_cost)
        elif self.ai.finished and self.ai.failed:
            score = "[no path]"
        else:
            score = "..."
        line5 = self.font.render("Mode: {}; Score: {}".format(self.type, score), 1, WHITE, BLACK)
        self.screen.blit(line1, (5, 5))
        self.screen.blit(line2, (5, 20))
        self.screen.blit(line3, (5, 35))
        self.screen.blit(line4, (5, 50))
        self.screen.blit(line5, (5, NODE_W * self.grid.height + OFFSET[1] + 5))
    def draw(self):
        self.screen.fill(0)
        self.grid.update(self, pygame)
        self.blitInfo()
        pygame.display.update()

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true', help='test');
parser.add_argument('--load', '-l', dest='load_num', type = int, default=-1, help='test map number to load')
args = parser.parse_args()

if __name__ == '__main__':
    if args.t:
        test()
    else:
        import pygame
        from pygame.locals import *

        game = GridWorld()

        with open("tests") as file:
            lines = file.readlines()
            if args.load_num in range(len(lines)):
                print("loading test case {}...".format(args.load_num))
                game.grid.load(" ".join(lines[args.load_num].split()[4:]))

        game.loop()
