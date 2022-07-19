import random

def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)

my_arr = input().split() # заполнение массива
my_arr = list(map(lambda x: int(x),my_arr)) # преобразование к типy int
new_arr = QuickSort(my_arr)
print(f'unsorted list: {my_arr} AND sorted list:{new_arr}')