#FDesign a food ordering system where your python program will run two threads,Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
#Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.Use this video to get yourself familiar with multithreading in python Pass following list as an argument to place order thread,
#orders = ['pizza','samosa','pasta','biryani','burger']
#This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.

from collections import deque
import time
import threading


class  Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()
    def isEmpty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)
q = Queue()

def orderPlace(orders):
    
    for order in orders:
        print('Place order for', order)
        q.enqueue(order)
        time.sleep(0.5)

def serveOrders():
    time.sleep(1)
    while len(q.buffer)!=0:
        order = q.dequeue()
        print("Now serving: ",order)
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=orderPlace, args=(orders,))
    t2 = threading.Thread(target=serveOrders)
    t1.start()
    t2.start()
    