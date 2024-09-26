import mouse # mouse library
import socket # TCP socket connection
# nc -l netcat listen

# server 
HOST = '192.168.1.165'  
PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def on_move(x, y):
    if x > 0:
        sock.send(b'r')  # r = right
    elif x < 0:
        sock.send(b'l')  # l = left
    if y > 0:
        sock.send(b'u')  # u = up
    elif y < 0:
        sock.send(b'd')  # d = down

def on_click(x, y, button, pressed):
    if pressed and button == mouse.RIGHT:
        sock.send(b'x')  

mouse.on_move(on_move)
mouse.on_click(on_click)

mouse.wait()