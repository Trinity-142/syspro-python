import copy
import time
import threading
TASKS_COUNT = 50
SIZE = 20
VALUE = 3
TIMES = 5
tasks_queue = []
lock = threading.Lock()

def matrix_multiply(A, B, size):
        res = [[0]*size for i in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    res[i][j] += A[i][k] * B[k][j]
        return res

class Producer(threading.Thread):
    def __init__(self, tasks_count, size, value, times):
        super().__init__()
        self.tasks_count = tasks_count
        self.size = size
        self.value = value
        self.times = times

    def run(self):
        for i in range(self.tasks_count):
            task = (self.size, self.value, self.times)
            with lock:
                tasks_queue.append(task)
            self.size += 1



class Consumer(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            with lock:
                if not len(tasks_queue):
                    break
                size, value, times = tasks_queue.pop(0)
            matrix = [[(lambda i, j: value ** (i + j))(i, j) for j in range(size)] for i in range(size)]
            buf = copy.deepcopy(matrix)
            for i in range(times):
                matrix = matrix_multiply(matrix, buf, size)




def main(consumers_count):
    producer = Producer(TASKS_COUNT, SIZE, VALUE, TIMES)
    consumers = [Consumer() for i in range(consumers_count)]

    start_time = time.time()
    producer.start()
    for consumer in consumers:
        consumer.start()

    producer.join()
    for consumer in consumers:
        consumer.join()
    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    for threads in range(2, 13):
        timing = round(main(threads), 3)
        print(f"Task was completed in {timing} seconds with {threads} threads", sep='\n')