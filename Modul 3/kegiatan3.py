random_list = [3.1, 2.7, 5.5, 19, 753, 412, 'Hello', 'Python', 'world', 'AI']

data_float = list(filter(lambda x: isinstance(x, float), random_list))
data_int = list(filter(lambda x: isinstance(x, int), random_list))
data_string = list(filter(lambda x: isinstance(x, str), random_list))


def map_to_digits(num):
    return {
        'ratusan': num // 100,
        'puluhan': (num % 100) // 10,
        'satuan': num % 10
    }

data_int_mapped = list(map(map_to_digits, data_int))


print("Data Float:", data_float)
print("Data Int:")
for item in data_int_mapped:
    print(item)
print("Data String:", data_string)
