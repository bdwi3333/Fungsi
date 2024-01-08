ganjil = [i*2+1 for i in range(25)]
div_by_3 = filter(lambda num : num%3 == 0, ganjil)
tambah = map(lambda x: x + 'kelipatan 3', div_by_3)
print(list(tambah))
