def mm(data, n):
    num = 0
    for x in data:
        num += x
    return num/n

def mmp(data, ponds, n):
    num = 0
    for i in range(0, len(data)):
        num += data[i]*ponds[i]
    den = 0
    for i in ponds:
        den += i
    return num/den
