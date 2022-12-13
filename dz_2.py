import random
import time

int_list = []

for i in range(0,5000):
    int_list.append(random.randint(0,1000))
print('int_list', int_list)


def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
               data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
               swapped = True
        if not swapped:
            break
    print("Bubble Sort: ", data)

bubble_sort(int_list)

def time_list(x,q):
    while q<10:
        count = 0
        stat_time = time.time()
        end_time = time.time()
        evered = end_time - stat_time
        int_list.append(evered)
        q = q + 1
        summa = sum(int_list) / q
        count += 1
        print(f'Average sorting time', summa)
        print(count)

time_list(int_list, 0)











