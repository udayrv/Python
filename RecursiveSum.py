def rec_sum(data, n):
    if n == 0:
        return 0
    else:
        return rec_sum(data, n-1) + data[n-1]



print(rec_sum([2, 3, 5, 8, 6, 9, 10, 12, 14, 20], 5))