from pynput import mouse
import socket 

# server 
HOST = '192.168.1.165'  
PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
    if x > 720:
        sock.send(b'r')  # r = right
    elif x <= 720:
        sock.send(b'l')  # l = left
    if y > 450:
        sock.send(b'd')  # d = down (inverted y-axis)
    elif y <= 450:
        sock.send(b'u')  # u = up (inverted y-axis)

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        ) as listener:
    listener.join()

