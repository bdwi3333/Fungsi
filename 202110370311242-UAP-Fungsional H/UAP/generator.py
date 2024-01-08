def count(start=0, stop=24):
    for i in range(start,stop+1):
        x= i*2+1
        yield x

ganjil = count(0,24)
for n in ganjil:
    print(n, end=" ")

