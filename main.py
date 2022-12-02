#funckja zczytuje z klawiatury w a s d i przesuwa 'glowe' weza
#potrzeba to zatwiedzic
print("blad")
import os
X=20
Y=20
try:
    import pynput
except ImportError:
    print("brak biblioteki")
    os.system('python -m pip install pynput')
    import pynput
x=10
y=10
print("blad")
def on_press(key):
    global x
    global y
    try:
        if key.char=='w':
            y+=1
            y%=Y
        elif key.char=='s':
            y-=1
            y%=Y
        elif key.char=='a':
            x-=1
            x%=X
        elif key.char=='d':
            x+=1
            x%=X
        print(x,y)

    except AttributeError:
        pass
print("blad")
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False
with pynput.keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

print("tylko dla bledu")
print("bladddd")

