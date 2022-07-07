
import random, string

# def dict_generator():
#     size = 10
#     keys = random.sample(string.ascii_lowercase, size)
#     value = [random.randint(1, 30) for _ in range(size)]
#     result = dict(zip(keys, value))
#     return result

# print(dict_generator())

def dict_generator():
    my_dictionary = {}
    for _ in range (0, 11):
        random_letter = random.choice(string.ascii_lowercase)
        random_number = random.randint(1, 30)
        my_dictionary[random_letter] = random_number
    print(my_dictionary)

print(dict_generator())