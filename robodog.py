from gpiozero import Motor
from gpiozero import Robot
from multiprocessing.connection import Listener
import time
# motor1 = Motor(23,4)
# motor2 = Motor(16,20)
robot = Robot(left=(20,16), right=(4, 23))



class Switcher(object):
    def indirect(self,i):
        method_name=str(i)
        print method_name
        method = getattr(self,method_name, lambda:"Invalid")
        method()
    def forward(self):
        robot.forward(1)
        print 'forward'
        time.sleep(2)
        robot.stop()
    def left(self):
        robot.left(1)
        print 'left'
        time.sleep(0.5)
        robot.stop()
    def right(self):
        robot.right(1)
        print 'right'
        time.sleep(0.5)
        robot.stop()
    def backward(self):
        robot.backward(1)
        print 'backwards'
        time.sleep(2)
        robot.stop()
    def error(self):
        print "error"
    def empty(self):
        print "empty"

s = Switcher()
address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey='secret password')
conn = listener.accept()
print ('connection accepted from', listener.last_accepted)
while True:
    msg = conn.recv()
    # print (msg)

    for info in msg:
        s.indirect(info)    

    if msg == 'close':
        conn.close()
        break
listener.close()
