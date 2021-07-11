import random
import curses
import locale

locale.setlocale(locale.LC_ALL, '')

screen = curses.initscr()
curses.curs_set(0)
win_height, win_width = screen.getmaxyx()
window = curses.newwin(win_height, win_width, 0, 0)
window.keypad(1)
window.timeout(100)

snake_xpos = win_width/4
snake_ypos = win_height/2

snake_beginning_length = 20
snake = [[snake_ypos, snake_xpos - i] for i in range(snake_beginning_length)]

food = [win_height/2, win_width/2]
window.addch(int(food[0]), int(food[1]), '0')#curses.ACS_PI)

key = curses.KEY_RIGHT
score = 0

while True:
	window.addstr(0, 0, "Score: " + str(score))

	next_key = window.getch()
	key = key if next_key == -1 else next_key

	if snake[0][0] in [0, win_height] or snake[0][1]  in [0, win_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        score += 1
        while food is None:
            new_food = [
                random.randint(1, win_height-1),
                random.randint(1, win_width-1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], '0')#curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(int(tail[0]), int(tail[1]), ' ')

    window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
