from functools import reduce
ganjil = [i*2+1 for i in range(25)]
div_by_3 = filter(lambda num : num%3 == 0, ganjil)
sum = reduce(lambda x,y: x+y, div_by_3)
print(f"jumlah = {sum}")

