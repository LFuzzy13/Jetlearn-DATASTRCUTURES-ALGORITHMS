class Queue:
    def __init__(self,size):
        self.queue = [None]*size#put None in the [] if you want alt output
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size
    
    def enqueue(self,item):
        if self.rear == self.size:
            print("Queue Overflow")
        else:
            self.queue[self.rear]=item
            #self.rear=(self.rear+1) % self.size
            self.rear +=1
            self.available -= 1

    def dequeue(self, item2):
        if item2 > self.rear:
            print("Not enough elements in the queue")
        else:
            for j in range(item2):
                item = self.queue[0]

                for i in range(self.rear - 1):
                    self.queue[i] = self.queue[i+1]

                self.rear -= 1
                self.queue[self.rear] = None
                self.available += 1
                print("Removed element", item)
            #self.queue[self.front]=None
            #self.front=(self.front+1) % self.size
            #self.available +=1
    def peek(self):
        if self.rear == 0:
          print("Queue is empty")
        else:
            print("Front element: ", self.queue[0])

    def getRear(self):
        if self.rear == 0:
            print("Queueue is empty")
        else:
            print("Rear element: ", self.queue[self.rear - 1])

    def print_queue(self):
        print(self.queue)


n = int(input("how many elements do you want to add: "))
queue1 = Queue(n)
for i in range ( n ):
    item = int(input("Enter an element: "))
    queue1.enqueue(item)

item2 = int(input("How Many Elements Would You Like To Remove?"))
queue1.dequeue(item2)

queue1.print_queue()

queue1.peek()
queue1.getRear()


queue1.print_queue()
