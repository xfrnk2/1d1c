import os
import threading
import keyboard
from copy import deepcopy
from random import randrange
import sys

class Block:
    def __init__(self):
        self.__block = "□"

    def set_block(self, shape):
        self.__block = shape

    def get_shape(self):
        return self.__block

    def clear_block(self):
        self.__block = "□"

    def __str__(self):
        return self.__block

lock = threading.Lock()
field_width, field_height = 6, 12
empty_field = [[Block() for _ in range(field_width)] for _ in range(field_height)]
field = deepcopy(empty_field)
cursorX, cursorY = 2, 0
subCursorX, subCursorY = cursorX, cursorY-1
another_block = "■"
shape_list = []
blocked_list = []

class AsyncTask:

    def __init__(self):
        self.__timer = None
    def TaskA(self):
        global cursorY, subCursorY
        cursorY += 1
        subCursorY += 1
        self.__timer = threading.Timer(1,self.TaskA)
        self.__timer.start()
        # threading.Timer(1,self.TaskA).start()
    def stopTaskA(self):
        self.__timer.cancel()


def checkField(x: int, y: int, shape:str):
    target = []
    visited = []
    stack = [(x, y)]

    while stack:
        node = stack.pop()

        if node not in visited:
            a, b = node
            if a < 0 or b < 0 or field_width - 1 < a or field_height - 1 < b:
                continue
            else:
                visited.append(node)

                if field[b][a].get_shape() == shape:
                    target.append(node)

                    stack = list(set(stack))
                    stack.extend([(a - 1, b), (a + 1, b), (a, b + 1), (a, b - 1)])

    return list(set(target))



def ignition(target_list, at):
    for target in target_list:
        if 4 <= len(target):
            row_info = {v:[0,0] for v in range(field_width)}#행 x에 해당하는 (y의 최저점, 블록의 양)

            for value in target:
                x, y = value
                field[y][x].clear_block()

                if row_info[x][0] < y:
                    row_info[x][0] = y
                row_info[x][1] += 1
            for x in range(field_width):
                lowest, quantity = row_info[x]

                for _ in range(quantity):

                    for i in range(lowest, 0, -1):
                        field[i][x], field[i-1][x] = field[i-1][x], field[i][x]


            rensa_target_list = []
            for i in range(field_width):
                if 0 < row_info[i][1]:
                    for j in range(row_info[i][0], -1, -1):
                        if field[j][i].get_shape() != "□":
                           rensa_target_list += [eval(f"checkField({i}, {j}, field[{j}][{i}].get_shape())")]
            ignition(rensa_target_list, at)



def func():
    global cursorX, cursorY, subCursorX, subCursorY, field, shape_list, blocked_list

    at = AsyncTask()
    at.TaskA()

    blocks = ["♥", "◆", "●", "♣"]
    current_block = (blocks[randrange(4)], blocks[randrange(4)])
    while True:
        os.system('cls')

        for y in range(field_height):
            for x in range(field_width):
                if x == cursorX and y == cursorY:
                    print(current_block[0], end='')
                elif x == subCursorX and y == subCursorY:
                    print(current_block[1], end='')
                else:
                    print(field[y][x], end='')
            print('')








        if cursorY == 11 or subCursorY == 11 or field[subCursorY+1][subCursorX].get_shape() in blocks or field[cursorY+1][cursorX].get_shape() in blocks:

            if cursorY == 11:
                field[cursorY][cursorX].set_block(current_block[0])
                field[subCursorY][subCursorX].set_block(current_block[1])

            elif subCursorY == 11:
                field[subCursorY][subCursorX].set_block(current_block[1])
                field[cursorY][cursorX].set_block(current_block[0])

            elif abs(subCursorY-cursorY) == 1:
                field[cursorY][cursorX].set_block(current_block[0])
                field[subCursorY][subCursorX].set_block(current_block[1])

            elif field[cursorY+1][cursorX].get_shape() in blocks and field[subCursorY+1][subCursorX].get_shape() in blocks:
                field[cursorY][cursorX].set_block(current_block[0])
                field[subCursorY][subCursorX].set_block(current_block[1])

            elif field[cursorY+1][cursorX].get_shape() in blocks and field[subCursorY+1][subCursorX].get_shape() not in blocks:
                field[cursorY][cursorX].set_block(current_block[0])

                for v in range(field_height-1, subCursorY, -1):

                    if field[v][subCursorX].get_shape() not in blocks:
                        field[v][subCursorX].set_block(current_block[1])
                        subCursorY = v

                        break
            elif field[subCursorY+1][subCursorX].get_shape() in blocks and field[cursorY+1][cursorX].get_shape() not in blocks:
                field[subCursorY][subCursorX].set_block(current_block[1])

                for v in range(field_height - 1, cursorY, -1):
                    if field[v][cursorX].get_shape() not in blocks:
                        field[v][cursorX].set_block(current_block[0])
                        cursorY = v

                        break


            cursor_list =  [("cursorX", "cursorY"), ("subCursorX", "subCursorY")]
            target_list = []
            if not field[cursorY][cursorX].get_shape() == field[subCursorY][subCursorX].get_shape():
                if cursorY < subCursorY:
                    cursor_list[0], cursor_list[1] = cursor_list[1], cursor_list[0]
            else:
                cursor_list.pop()

            for pair in cursor_list:
                x, y = pair
                target_list += [eval(f"checkField({x}, {y}, field[{y}][{x}].get_shape())")]
            ignition(target_list, at)

            cursorX, cursorY = 2, -1
            subCursorX, subCursorY = cursorX, cursorY+1
            current_block = (blocks[randrange(4)], blocks[randrange(4)])


        if "□" not in [field[x][2].get_shape() for x in range(field_height)]:

                while True:
                    flag = input("game over. Retry? (Y/N)")
                    if flag == "N":
                        at.stopTaskA()
                        sys.exit()
                    elif flag == "Y":
                        field = deepcopy(empty_field)
                        cursorX, cursorY = 2, -1
                        subCursorX, subCursorY = cursorX, cursorY + 1
                        break
                    else:
                        print("You should input Y or N")




        if keyboard.is_pressed('RIGHT'):
            if abs(cursorY - subCursorY) == 1:

                if cursorX != field_width-1 and field[cursorY][cursorX+1].get_shape() not in blocks:
                    cursorX += 1
                    subCursorX += 1
            else:
                if cursorX > subCursorX:
                    if cursorX != field_width - 1 and field[cursorY][cursorX+1].get_shape() not in blocks:
                        cursorX += 1
                        subCursorX += 1
                elif cursorX < subCursorX:
                    if subCursorX != field_width - 1 and field[subCursorY][subCursorX + 1].get_shape() not in blocks:
                        cursorX += 1
                        subCursorX += 1


        elif keyboard.is_pressed('LEFT'):



            if abs(cursorY - subCursorY) == 1:

                if cursorX != 0 and field[cursorY][cursorX-1].get_shape() not in blocks:
                    cursorX -= 1
                    subCursorX -= 1
            else:
                if cursorX > subCursorX:
                    if subCursorX != 0 and field[subCursorY][subCursorX - 1].get_shape() not in blocks:
                        cursorX -= 1
                        subCursorX -= 1
                elif cursorX < subCursorX:
                    if cursorX != 0 and field[cursorY][cursorX - 1].get_shape() not in blocks:
                        cursorX -= 1
                        subCursorX -= 1




        elif keyboard.is_pressed('DOWN'):
            cursorY += 1
            subCursorY += 1

        if keyboard.is_pressed('z'):
            if cursorY > subCursorY:
                if 0 < cursorX and field[cursorY][cursorX - 1].get_shape() not in blocks:
                    subCursorX, subCursorY = subCursorX - 1, subCursorY + 1
            elif cursorY < subCursorY:
                if cursorX < field_width-1  and field[cursorY][cursorX + 1].get_shape() not in blocks:
                    subCursorX, subCursorY = subCursorX + 1, subCursorY - 1
            elif cursorY == subCursorY:

                if subCursorX < cursorX:
                    if cursorY != field_height-1 and field[cursorY+1][cursorX].get_shape() not in blocks:
                        subCursorX, subCursorY = subCursorX +1, subCursorY +1

                elif subCursorX > cursorX:
                        subCursorX, subCursorY = subCursorX - 1, subCursorY - 1

        if keyboard.is_pressed('x'):
            if cursorY > subCursorY:
                if cursorX < field_width-1 and field[cursorY][cursorX + 1].get_shape() not in blocks:
                    subCursorX, subCursorY = subCursorX + 1, subCursorY + 1
            elif cursorY < subCursorY:
                if 0 <cursorX and field[cursorY][cursorX - 1].get_shape() not in blocks:
                    subCursorX, subCursorY = subCursorX - 1, subCursorY - 1
            elif cursorY == subCursorY:

                if subCursorX < cursorX:
                    subCursorX, subCursorY = subCursorX +1, subCursorY -1

                elif subCursorX > cursorX:
                    if cursorY != field_height - 1 and field[cursorY + 1][cursorX].get_shape() not in blocks:
                        subCursorX, subCursorY = subCursorX - 1, subCursorY + 1

if __name__ == '__main__':
    func()
