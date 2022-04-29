from tkinter import *
from settings import *
from cell import Cell
import utils

root = Tk()

# Override the settings of the window
root.configure(bg="black")
root.geometry("{}x{}".format(WIDTH, HEIGHT))
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root, 
    bg = "black",
    width = WIDTH,
    height = utils.frame_height(25)
)
top_frame.place(x = 0, y = 0)

game_title = Label(
    top_frame,
    bg="Black",
    fg="white",
    text="Minesweeper Game",
    font=("", 48)
)
game_title.place(
    x=utils.frame_width(30),
    y=utils.frame_height(7)
)

left_frame = Frame(
    root, 
    bg = "black",
    width = utils.frame_width(25), 
    height = utils.frame_height(75)
)
left_frame.place(x = 0, y = utils.frame_height(25))

center_frame = Frame(
    root, 
    bg = "black",
    width = utils.frame_width(75), 
    height = utils.frame_height(75)
)
center_frame.place(x = utils.frame_width(25), y = utils.frame_height(25))

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column = x, row = y)

# Call the label from cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()


# Run the window
root.mainloop()