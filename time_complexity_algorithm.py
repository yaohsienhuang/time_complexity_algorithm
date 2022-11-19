import time

def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')

def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')


def merge_sort(data):
    if len(data) <= 1:
        return
    
    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    
    merge_sort(left_data)
    merge_sort(right_data)
    
    left_index = 0
    right_index = 0
    data_index = 0
    
    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1
    
    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]
    return data

def bubble_sort(data):
    data=data.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
    return data

if __name__ == '__main__':

    data_random = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    data_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target=8

    algorithm_list=[
        ('linear_search',linear_search(data_sorted, target)),
        ('binary_search',binary_search(data_sorted, target)),
        ('merge_sort',merge_sort(data_random)),
        ('bubble_sort',bubble_sort(data_random)),
    ]
    
    for name,algorithm in algorithm_list:
        starttime=time.time()
        print('answer =',algorithm)
        endtime=time.time()
        print(f'{name} =',round((endtime-starttime)*1000,5),' ms')