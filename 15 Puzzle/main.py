from Board import Board
from time import sleep
from pynput import keyboard

b = Board()


def main():
    b.shuffle()
    b.refresh()

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()



def on_press(key):
    # every time press the key, refresh the page
    b.refresh()


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener by esc key
        return False

    elif key == keyboard.Key.up:
        b.board, b.e_loc = b.move_up(b.board, b.e_loc)
    elif key == keyboard.Key.down:
        b.board, b.e_loc = b.move_down(b.board, b.e_loc)
    elif key == keyboard.Key.left:
        b.board, b.e_loc = b.move_left(b.board, b.e_loc)
    elif key == keyboard.Key.right:
        b.board, b.e_loc = b.move_right(b.board, b.e_loc)
    elif key == keyboard.Key.shift:
        print("Thinking...")
        moves = b.solve()
        for m in moves:
            b.moves[m](b.board, b.e_loc)
            b.refresh()
            sleep(1)


    # every time release the key, clear the screen and print the board
    return b.refresh()




if __name__ == "__main__":
    main()

