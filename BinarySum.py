def binary_sum(data, start, stop):
    if start >= stop:
        return 0
    elif start == stop-1:
        return data[start]
    else:
        mid = (start+stop)//2
        return binary_sum(data, start, mid) + binary_sum(data, mid, stop)


seq = [2, 3, 5, 8, 6, 9, 10, 12, 14, 20]
print(binary_sum(seq, 0, len(seq)))