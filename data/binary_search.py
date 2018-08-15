import time
import datetime

# main()


def binary_search(somelist,target):

    somelist.sort()
    low=0
    high =len(somelist)-1

    while low < high:
        mid=int((low+high)/2)
        if somelist[mid]==target:
            return True
        elif somelist[mid]<target:
            low= mid+1
        else:
            high = mid-1
        # print("hi")
    return False

def pythonic_search(somelist,target):
    if target in somelist:
        return True
    else :
        return False


def binary_search_recursion(somelist,target,low,high):
    somelist.sort()
    high=high
    low=low
    mid = int((high+low)/2)
    if high<low or low >high:
        return False
    elif somelist[mid] ==target:
        return True
    elif somelist[mid] >target:
        return binary_search_recursion(somelist,target,low,mid-1)
    elif somelist[mid] <target:
        return binary_search_recursion(somelist,target,mid+1,high)
    

if __name__ == "__main__":
    target=102
    start_time = time.time()
    somelist = [1,3,7,2,10,13,2,17,51,100,4,6]
    # target = int(input())
    result = binary_search(somelist,target)
    print(result) 
    # print("--- {t} seconds ---".format(t=(time.time() - start_time))
    excecution_time = time.time() - start_time
    print("____{:.10f}______".format(excecution_time))
    # print('___{t}___'.format(t=datetime.datetime.fromtimestamp(time.time()-start_time)))


    start_time = time.time()
    result = pythonic_search(somelist,target)
    print(result)
    excecution_time = time.time() - start_time
    print("____{:.10f}______".format(excecution_time))



    start_time = time.time()
    result =binary_search_recursion(somelist,target,0,len(somelist)-1)
    print(result)
    excecution_time = time.time() - start_time
    print("____{:.10f}______".format(excecution_time))

    # print((2+3)//2)


