tupl1 = ('pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)
list1 = []
list2 = []
for x in tupl1:
    if (type(x) in (int)):
        list1 = x
    else:
        x = list2

for x in list1:
    print(x)
for x in list2:
    print(x)