import multiprocessing
import os
import sys
import tkinter
import pygame
import vars
from socket_implementation import in_game

__author__ = 'Markus Peterson'


# TODO Make some menu somehere in Tk

class Main(vars.Variables):
    def __init__(self):
        """
            Main class that hooks everything up and runs the game.
        """
        # setting things up
        # tkinter frame
        self.root = tkinter.Tk()
        self.PygameFrame = tkinter.Frame(self.root, width=self.screen_width, height=self.screen_height)
        self.PygameFrame.pack(side='left')
        os.environ['SDL_WINDOWID'] = str(self.PygameFrame.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        # pygame
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption('The Game')
        self.PygameFrame.focus_set()
        self.screen.fill((80, 80, 80))
        self.clock = pygame.time.Clock()
        self.ms = self.clock.tick(50)

        # The Game
        self.game = in_game.Game(self.screen, self.ms, master=self.root)

    def run(self):
        """
            The main game loop. Has event calling inside and draws everything onto screen using the map_draw function from in_game.
            Also updates pygame.display and root tkinter.Frame.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # self.root.destroy()
                    sys.exit()
                else:
                    self.game.get_vars()
                    self.game.on_event(event)

            self.ms = self.clock.tick(200)
            self.screen.fill((80, 80, 80))
            self.game.map_draw(self.screen, self.ms)
            pygame.display.flip()
            self.root.update()


if __name__ == '__main__':
    # Start worker processes
    num_consumers = multiprocessing.cpu_count() * 1
    workers = [in_game.Worker(vars.Variables.tasks, vars.Variables.results) for i in range(num_consumers)]
    for worker in workers: worker.start()
    for worker in workers: print(worker.is_alive())

    game = Main()
    game.run()
