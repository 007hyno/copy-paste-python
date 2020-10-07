from pynput.keyboard import Controller, Key
import time
k=Controller()
x=0
a,c,v='a','c','v'
noneofyourbusiness=a
incryptedmsg=c
bantibachibanae=v
time.sleep(2.5)
k.press(Key.ctrl)
while x<10:
    print(x)
    k.type(noneofyourbusiness)
    k.type(incryptedmsg)
    k.press(Key.right)
    k.release(Key.right)
    k.type(bantibachibanae)
    x+=1
k.release(Key.ctrl)