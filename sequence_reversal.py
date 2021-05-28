def seq_rev(data, start, stop):
    if start < stop-1:
        data[start], data[stop-1] = data[stop-1], data[start]
        seq_rev(data, start+1, stop-1)
        return data


seq = [1, 3, 8, 9, 12, 16]
print(seq_rev(seq, 0, 6))