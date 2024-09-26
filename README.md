# Understanding-Network

## Controller

- Python Library: [pynput](https://pypi.org/project/pynput/)

### Prerequisite

1. Install pynput library using pip.
2. Go to Setting -> Security & Privacy -> Accessibility -> + -> select Terminal.app

### Step-by-Step

1. Python library **pynput** allows the program to monitor mouse position.
2. I used the following line of code to measure my screen.

```python
print('Pointer moved to {0}'.format((x, y)))
```

```terminal
Pointer moved to (427.15069580078125, 552.6111450195312)
Pointer moved to (427.15069580078125, 552.3785400390625)
Pointer moved to (427.15069580078125, 552.1339721679688)
Pointer moved to (427.15069580078125, 551.8894653320312)
Pointer moved to (427.15069580078125, 551.6322021484375)
Pointer moved to (427.15069580078125, 551.3740844726562)
Pointer moved to (427.15069580078125, 551.115966796875)
Pointer moved to (427.15069580078125, 550.85791015625)
Pointer moved to (426.8648681640625, 550.2861938476562)
Pointer moved to (426.8648681640625, 550.0291137695312)
Pointer moved to (426.60675048828125, 549.77099609375)
Pointer moved to (426.3486633300781, 549.5128784179688)
Pointer moved to (426.3486633300781, 549.2551879882812)
Pointer moved to (426.090576171875, 548.9970703125)
Pointer moved to (425.8460693359375, 548.7525634765625)
Pressed at (425.8460693359375, 548.7525634765625)
Pointer moved to (425.8460693359375, 548.6338500976562)
Released at (425.8460693359375, 548.6338500976562)
```

3. I divide width and height of my screen by half, and then program the commands to send via netcat

```python
if x > 720:
    sock.send(b'r')  # r = right
elif x <= 720:
    sock.send(b'l')  # l = left
if y > 450:
    sock.send(b'd')  # d = down (inverted y-axis)
elif y <= 450:
    sock.send(b'u')  # u = up (inverted y-axis)
```

4.To run the controller, go to where main.py is, and enter the following command in the terminal:

```terminal
python3 main.py
```
