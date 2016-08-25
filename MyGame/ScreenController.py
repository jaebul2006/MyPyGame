import os
import Player

class SC(object):
    width = 45
    height = 10

    def Clear(self, Player):
        os.system('cls')
        print('=============================================')

        x = Player.x
        y = Player.y
        strx = ' '
        for i in range(x):
            strx += strx
        print(strx)
        for y in range(y):
            print('\n')

        print(strx + '▲')

        #for i in range(10):
        #    print('=                                           =\n')
        print('=============================================')

    
