def binarysearch(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            print("Target Found at location: {}".format(mid+1))
            return
        elif target < data[mid]:
            return binarysearch(data, target, low, mid-1)
        else:
            return binarysearch(data, target, mid+1, high)

sample = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

print(binarysearch(sample, 22, 0, len(sample)))