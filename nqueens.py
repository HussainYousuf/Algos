
from numpy import append
import pyglet
from pyglet import shapes


def main():
    queens = []

    def get_all_queens(rows=[None]*4, cur_row=0):
        if(cur_row >= len(rows)):
            queens.append(rows)
        else:
            for col in range(len(rows)):
                legal = True
                for row in range(cur_row):
                    if(rows[row] == col or rows[row] == col - cur_row + row or rows[row] == col + cur_row - row):
                        legal = False
                        break
                if(legal):
                    rows[cur_row] = col
                    get_all_queens(rows[:], cur_row + 1)

    get_all_queens()
    return queens

# main()


def draw(rows):
    print(rows)
    size = 800
    window = pyglet.window.Window(size, size)
    batch = pyglet.graphics.Batch()
    size = size//len(rows)

    batches = []
    for row in range(len(rows)):
        for col in range(len(rows)):
            batches.append(
                shapes.BorderedRectangle(
                    col*size, row*size, size, size,
                    color=(255, 255, 255) if (
                        row + col) % 2 == 0 else (100, 100, 100),
                    batch=batch
                )
            )
            if(col == rows[row]):
                batches.append(shapes.Circle(
                    col*size+100, row*size+100, 50, color=(0,0,0), batch=batch))

    @window.event
    def on_draw():
        print("callwd")
        window.clear()
        batch.draw()

    # window.on_draw = on_draw
    pyglet.app.run()

draw(main()[1])
