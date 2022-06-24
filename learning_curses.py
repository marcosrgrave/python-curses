import curses

txt: str = "text"
s: list = [txt for i in range(5)]
print(s)

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.getch()

print("preparing to initialize screen")
screen = curses.initscr()

screen.addstr(0, 0, "texto 1")
screen.addstr(1, 2, "texto 1")
screen.addstr(3, 1, "X")
screen.addch(5, 5, "Y")


print("screen initialized")
screen.refresh()

curses.napms(2000)
curses.endwin()

print('window ended.')
