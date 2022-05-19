import random
import string

from helpers import make_pi


PI_DIGITS = [digit for digit in make_pi()]  # first 20 digits of pi

PERMUTATION_TABLE_SIZE = 20
PERMUTATION_TABLE = [random.sample(PI_DIGITS, PERMUTATION_TABLE_SIZE)
                     for _ in range(PERMUTATION_TABLE_SIZE)]


def my_hash(line, pti=0):
    return (sum(ord(c) * PERMUTATION_TABLE[pti][i % PERMUTATION_TABLE_SIZE] for i, c in enumerate(line))
            // len(line)) % hash_table_size


def hash_add(hash_table, line):
    collisions = 0
    hash_value = my_hash(line)
    while hash_table[hash_value] is not None:
        hash_value = my_hash(line, collisions)
        collisions += 1
        if collisions == 20:
            print("Couldn't add", line)
            break
    hash_table[hash_value] = (line, collisions)


def bubble_hash(hash_table):
    global hash_table_size
    hash_table_size *= 2
    new_hash_table = [None for _ in range(hash_table_size)]
    for item in hash_table:
        if item is not None:
            hash_add(new_hash_table, item[0])
    return new_hash_table


def print_hash_table(hash_table):
    hash_table_size = len(hash_table)
    print(f'\nPrinting hash table (size {hash_table_size})')
    print('-' * 16)
    total_items = 0
    for i, item in enumerate(hash_table):
        if item is not None:
            total_items += 1
            print(i+1, item)
    print('-' * 16)
    print(f'Total items: {total_items}/{hash_table_size}\nDensity is {total_items / hash_table_size * 100:.2f}%\n')


# tests
hash_table_size = 2 ** 7
hash_table = [None for _ in range(hash_table_size)]

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec maximus elit nec urna vulputate vehicula. Vivamus ac convallis lorem. Etiam interdum enim id erat accumsan aliquet. Curabitur imperdiet, ligula et hendrerit scelerisque, nisl enim auctor massa, rhoncus consequat nibh ex quis ipsum. Vivamus dignissim mi sed dui bibendum, sit amet blandit orci volutpat. Etiam ac justo sed sapien accumsan interdum nec ut arcu. Pellentesque dapibus erat orci, non consectetur tortor tincidunt ac. Donec posuere eu ipsum vel ornare. Nulla nisl massa, molestie tempor tincidunt eu, pharetra quis quam.
Phasellus lacinia felis sit amet erat blandit porttitor. Aenean et urna finibus, euismod ipsum et, dapibus metus. Quisque bibendum fermentum elit sit amet pharetra. Praesent eros quam, euismod eu sem at, ornare viverra nisi. Pellentesque pretium fermentum nibh, scelerisque laoreet lectus tincidunt id. Aliquam erat volutpat. Proin porttitor, purus cursus efficitur tempus, mauris massa dignissim metus, vel condimentum neque dui id tortor.
Etiam suscipit in mauris at interdum. Etiam tempus dui in rutrum egestas. Nunc quis magna et ex ornare ornare. Sed non tellus sit amet ex consequat efficitur. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse potenti. Sed nec porta ex. Phasellus convallis nunc justo, viverra pharetra ante venenatis sed. Fusce facilisis metus nibh, eu porttitor ipsum eleifend ut. Curabitur tincidunt urna nec urna scelerisque suscipit eget sed velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
Donec dignissim felis a sem bibendum, vitae tempor magna convallis. Vivamus sit amet nisl laoreet, molestie lorem vulputate, molestie velit. Nullam venenatis aliquet erat sit amet euismod. Donec lacinia quis tortor vitae sagittis. Ut nisi mauris, gravida nec egestas vel, rutrum quis enim. Maecenas porttitor egestas ornare. Phasellus lobortis velit erat. Suspendisse molestie gravida ipsum id elementum. Phasellus quis dolor pharetra, varius justo sit amet, eleifend nibh. Praesent quis laoreet dolor.
Proin condimentum fermentum sapien. Pellentesque in commodo nibh, non commodo justo. Duis gravida egestas nisl, vel malesuada est facilisis vitae. Nulla sapien sem, aliquam non ante vel, malesuada pulvinar turpis. In maximus porttitor tristique. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut lacus ex, consectetur vitae magna sed, pulvinar varius nulla. Proin vitae accumsan arcu. Pellentesque tristique vestibulum tristique. Aenean ullamcorper ornare lacus, sed ornare eros sodales ut. Donec vitae felis nulla. Etiam vestibulum scelerisque metus, at tempor sem placerat vitae. Integer volutpat tortor eget dolor rutrum viverra. 
"""
words = ["".join([c for c in word if c in string.ascii_letters]) for word in text.split()]
print(len(words))
for word in words:
    hash_add(hash_table, word)


print_hash_table(hash_table)
hash_table = bubble_hash(hash_table)
print_hash_table(hash_table)
