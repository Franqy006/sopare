from multiprocessing.connection import Listener

class Switcher(object):
    def indirect(self,i):
        method_name=str(i)
        print method_name
        method = getattr(self,method_name, lambda:"Invalid")
        method()
    def stay(self):
        print "got command to stay"
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
