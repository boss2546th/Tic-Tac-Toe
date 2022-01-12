import numpy as np
import random as rd


class Game:
    players = ['O', 'X']
    turn = rd.randint(0, 1)

    tb = [
        '-', '-', '-',
        '-', '-', '-',
        '-', '-', '-'
    ]

    boolO = np.array([
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ])

    boolX = np.array([
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ])

    poslst = [
        7, 8, 9,
        4, 5, 6,
        1, 2, 3
    ]

    win = False
    full = False

    def col():
        for i in range(3):
            winX = Game.boolX[i] * Game.boolX[i + 3] * Game.boolX[i + 6]
            winO = Game.boolO[i] * Game.boolO[i + 3] * Game.boolO[i + 6]
            if bool(winX) or bool(winO):
                Game.win = True
                break

    def row():
        for i in range(0, 7, 3):
            winX = min(Game.boolX[i:i + 3])
            winO = min(Game.boolO[i:i + 3])
            if bool(winX) or bool(winO):
                Game.win = True
                break

    def dgn():
        for i in range(0, 3, 2):
            Id = (4 - i)
            winX = min([Game.boolX[j] for j in range(i, i + (Id * 2) + 1, Id)])
            winO = min([Game.boolO[j] for j in range(i, i + (Id * 2) + 1, Id)])
            if bool(winX) or bool(winO):
                Game.win = True
                break

    def showTable(tb):
        print(",---,---,---,")
        for i in range(0, 7, 3):
            lst2join = list(map(str, tb[i:i + 3]))
            print(f"| {' | '.join(lst2join)} |")
            if i < 6: print('|---|---|---|')
        print("'---'---'---'")

    def Run():
        while True:
            Game.showTable(Game.tb)
            opt = Game.players[Game.turn]
            pos = input(f'_____________\ntrun {opt} \nposition : ')
            cnt = True
            msg = ''

            try:
                pos = int(pos)
            except:
                if pos == 'END': break

            if not (pos in Game.poslst):
                msg = 'Error: Enter just 1-9 or END please!'
            elif (Game.boolX + Game.boolO)[Game.poslst.index(pos)]:
                msg = '\n" This field is used "'
            else:
                cnt = False

            if cnt:
                print(msg);continue

            cmd = 'Game.bool' + opt + '[Game.poslst.index(pos)] = 1'
            Game.tb[Game.poslst.index(pos)] = opt
            exec(cmd)
            Game.full = min(Game.boolX + Game.boolO)
            Game.col();Game.row();Game.dgn()
            showWin = opt + ' is winner' if Game.win else 'Draw' if Game.full else 'NEXT'
            Game.turn = int(not Game.turn)
            print(f'\n" {showWin} "')
            if Game.win or Game.full: break

if __name__ == '__main__':
    Game.Run()
    Game.showTable(Game.tb)
