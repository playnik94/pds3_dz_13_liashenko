import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0,5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())


print(f'int_list',int_list)
print(f'float_list', float_list)
print(f'word_list', str_list)
