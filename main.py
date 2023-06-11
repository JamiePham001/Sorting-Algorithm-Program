import random
import time

def countingsort(array):  # countingsort function with a list parameter
    c = 0

    countlist = []  # create a list to keep track of count
    countlist2 = []  # create a hidden list to keep track of count

    for i in range(len(array)):  # for i in range the length of the list
        count = -1  # begin count at -1
        for x in range(len(array)):  # for x in range length of list
            if array[i] - array[x] >= 0:  # if the substraction of list i and list x is more or equal 0
                count += 1  # increment count by +1
                c += 1
        countlist.append(count)  # append count to countlist
        while count in countlist2: # if count exists in countlist
            count -= 1 # decrement count
        countlist2.append(count) # append count to countlist2

    glist = []
    # create a list filled with zeros same size as array
    for i in range(len(array)):
        glist.append(0)

    # use sorted index from countlist2 to add unsorted array values in order
    for i in range(len(array)):
        glist[countlist2[i]] = array[i]
        c += 1

    # convert array to sorted by appending ordered values from glist
    for i in range(len(array)):
        array[i] = glist[i]
        c += 1

    return c

def partition(array, low, high, count):
    # the rightmost element will be the pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    for j in range(low, high): # iterate through elements
        count += 1
        if array[j] <= pivot: # compare each element with pivot
            # pivot found if element smaller than pivot
            i = i + 1 # change pointer to a greater element

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1, count

def quicksort(array, low, high, count):
    if low < high:

        # find pivot element to make sure that elements smaller than the pivot are to the positioned to the left
        # and elements larger than the pivot are positioned to the right
        pi, count = partition(array, low, high, count)

        count = quicksort(array, low, pi - 1, count)

        # recursive call on the left of pivot
        count = quicksort(array, pi + 1, high, count)

    return count

def mergesort(array):
    count = 0
    if len(array) > 1:

        r = len(array)//2 # r is the point where the array is divided into two
        L = array[:r] # L is the left subarray
        M = array[r:] # M is the right subarray

        # halves sorting
        left_part = mergesort(L)
        right_part = mergesort(M)

        count += left_part + right_part

        i = j = k = 0 # set i, j, k to 0

        # when either end of l and m are reached, the larger elements in l and m
        # are placed into the correct position into the array
        while i < len(L) and j < len(M):
            count += 1
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # when elements in l run out pick up the remaining
        # elements and put into the array
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            count += 1

        # when elements in m run out pick up the remaining
        # elements and put into the array
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            count += 1

    return count

def insertionsort(array):

    count = 0

    # loops through array
    for step in range(1, len(array)):
        key = array[step] # track value of array
        j = step - 1 # track index of array

        # compare the key with each element on the left until a smaller element is found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            count += 1

        # key placed in array after an object smaller than it
        array[j + 1] = key

    return count

def selectionsort(array):

    count = 0

    # loop through array
    for step in range(len(array)):
        min_idx = step # track index of array

        # loop through array whilst incrementing step
        for i in range(step + 1, len(array)):
            count += 1
            if array[i] < array[min_idx]: # check if array value is smaller mid_idx value
                min_idx = i
                count += 1

        # swapping element at step with element at min_idx
        (array[step], array[min_idx]) = (array[min_idx], array[step])

    return count

def multi():
    print('<Multiple Algorithm Test>')
    while True:

        try:
            array_size = int(input('enter array size: '))

            print('Average Number of Comparisons')
            print(
                '-------------------------------------------------------------------------------------------------------')
            print(
                'Sorting Algorithm |      Array      |       Num. of Comparisons       |       Run time (in ms.)       |')

            # create lists to be used by algorithms
            list1 = []
            list2 = []
            list3 = []
            list4 = []
            list5 = []

            for y in range(0, array_size):  # for i in range of 0 and 20
                x = random.randint(-100, 100)  # generated random integer
                # append to lists
                list1.append(x)
                list2.append(x)
                list3.append(x)
                list4.append(x)
                list5.append(x)

            for i in range(0, 5): # loop 5 times

                if i == 0:
                    s = time.time()
                    c = selectionsort(list1) # call function
                    e = time.time()
                    t = (e - s)*1000 # total time
                    print('|    Selection    |    ', array_size, '       |               ', c, '             |      ', t) # print data

                if i == 1:
                    s = time.time()
                    c = insertionsort(list2) # call function
                    e = time.time()
                    t = (e - s) * 1000 # total time
                    print('|    Insertion    |    ', array_size, '       |               ', c, '             |      ', t) # print data

                if i == 2:
                    s = time.time()
                    c = mergesort(list3) # call function
                    e = time.time()
                    t = (e - s) * 1000 # total time
                    print('|    Merge        |    ', array_size, '       |               ', c, '             |      ', t) # print data

                if i == 3:
                    s = time.time()
                    c = quicksort(list4, 0, len(list4) - 1, 0) # call function
                    e = time.time()
                    t = (e - s) * 1000 # total time
                    print('|    Quick        |    ', array_size, '       |               ', c, '             |      ', t) # print data

                if i == 4:
                    s = time.time()
                    c = countingsort(list5) # call function
                    e = time.time()
                    t = (e - s) * 1000 # total time
                    print('|  CountingSort2  |    ', array_size, '       |               ', c, '             |      ', t) # print data

        except ValueError:
            print('invalid value')
        mainmenu()


def indiv():
    print('\n1. selection sort')
    print('2. insertion sort')
    print('3. merge sort')
    print('4. quick sort')
    print('5. counting sort')

    # test if input is either 1, 2, 3, 4, 5
    while True:
        try:
            print('\n select an algorithm')
            select = int(input('> ')) # algorithm select input
            array_size = int(input('enter array size: ')) # array size input

            randlist = []  # create a list called randlist

            for i in range(0, array_size):  # for i in range of 0 and 20
                x = random.randint(-100, 100)  # generated random integer
                randlist.append(x)  # append integer to randlist

            if select == 1: # selection sort selection
                print('\n <selection sort>')
                start = time.perf_counter()
                count = selectionsort(randlist) # call function to c_t variable
                end = time.perf_counter()
                print('comparisons: ', count) # show comparisons
                print('time: ', (end - start) * 1000, 'ms') # show time
                print(randlist, '\n') # show list
                mainmenu()
            if select == 2: # insertion sort selection
                print('\n <insertion sort>')
                start = time.perf_counter()
                count = insertionsort(randlist) # call function to c_t variable
                end = time.perf_counter()
                print('comparisons: ', count) # show comparisons
                print('time: ', (end - start) * 1000, 'ms') # show time
                print(randlist, '\n') # show list
                mainmenu()
            if select == 3: # merge sort selection
                print('\n <merge sort>')
                start = time.perf_counter()
                count = mergesort(randlist) # call function to count variable
                end = time.perf_counter()
                print('time: ', (end - start) * 1000, 'ms') # show time
                print('comparisons: ', count) # show comparison
                print(randlist,'\n') # show list
                mainmenu()
            if select == 4: # quick sort selection
                print('\n <quick sort>')
                size = len(randlist) # length of list to size variable
                start = time.perf_counter()
                count = quicksort(randlist, 0, size - 1, 0) # call function to count variable
                end = time.perf_counter()
                print('time: ',(end - start) * 1000, 'ms') # show time
                print('comparisons: ', count) # show comparisons
                print(randlist) # show list
                mainmenu()
            if select == 5: # counting sort selection
                print('\n <counting sort>')
                start = time.perf_counter()
                count = countingsort(randlist) # call function to c_t variable
                end = time.perf_counter()
                print('comparisons: ', count) # show comparisons
                print('time: ',(end - start) * 1000, 'ms') # show time
                print(randlist,'\n') # show list
                mainmenu()
            else:
                print('invalid selection')

        except ValueError:
            print('invalid value')

def mainmenu():
    print('========================================')
    print('                 Main Menu')
    print('========================================')
    print('1. Test an individual sorting algorithm')
    print('2. Test multiple sorting algorithms')

    # test if input is either 1 or 2
    while True:
        try:
            select = int((input('> ')))
            if select == 1:
                indiv()
            elif select == 2:
                multi()
            else:
                print('invalid selection')

        except ValueError:
            print('invalid value')

mainmenu() # begin program



