def insertion-sort(arrr):
    for i in range(1,len(arrr)):

        j = i

        while j > 0 and arrr[j] < arrr[j-1]:
            arrr[j-1], arrr[j] = arrr[j], arrr[j-1]
            j -=1



arrr = [0,5,11,3,26,7,94,0,10]
insertion-s
