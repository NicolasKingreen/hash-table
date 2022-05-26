import random
import string

from helpers import make_pi


PI_DIGITS = [digit for digit in make_pi()]  # first 20 digits of pi
PERMUTATION_TABLE_SIZE = 20
PERMUTATION_TABLE = [random.sample(PI_DIGITS, PERMUTATION_TABLE_SIZE)
                     for _ in range(PERMUTATION_TABLE_SIZE)]


class HashTable:

    def __init__(self, size=2**7):
        self._hash_table_size = size
        self._init_core_array()

    def __repr__(self):
        return f'<HashTable' \
               f'(size: {self._hash_table_size}, ' \
               f'total_items: {self.total_items}, ' \
               f'density: {self.density})>'

    @property
    def total_items(self):
        total_items = 0
        for element in self._hash_table:
            if element is not None:
                total_items += 1
        return total_items

    @property
    def density(self):
        return self.total_items / self._hash_table_size

    def add(self, line):
        collisions = 0
        hash_value = self._hash(line)
        if self._hash_table[hash_value] and self._hash_table[hash_value][0] == line:
            return
        while self._hash_table[hash_value] is not None:
            collisions += 1
            if collisions == 20:
                print("[Add] Couldn't add", line)
                self.print_short()
                self._bubble_hash_table()
                collisions = 0
            hash_value = self._hash(line, collisions)
        self._hash_table[hash_value] = (line, collisions)

    def print_short(self):
        print(f'Total items: {self.total_items}/{self._hash_table_size}')
        print(f'Density is {self.density:.2%}')

    def print(self):
        """
        Prints out hash table size, non-empty elements and its density
        """
        print(f'\nHash table (size {self._hash_table_size})')
        if self.total_items:
            print('-' * 16)
            total_items = 0
            for i, item in enumerate(self._hash_table):
                if item is not None:
                    total_items += 1
                    print(i + 1, item)
            print('-' * 16)
        self.print_short()

    def _init_core_array(self):
        self._hash_table = [None for _ in range(self._hash_table_size)]

    def _hash(self, line, pti=0):
        return (sum(ord(c) * PERMUTATION_TABLE[pti][i % PERMUTATION_TABLE_SIZE]
                    for i, c in enumerate(line))
                // len(line)) % self._hash_table_size

    def _bubble_hash_table(self):
        print("[BubbleHashTable] Expanding hash...")
        self._hash_table_size *= 2
        old_hash_table = self._hash_table[:]
        self._init_core_array()
        for item in old_hash_table:
            if item is not None:
                self.add(item[0])


# tests
hash_table = HashTable()

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec maximus elit nec urna vulputate vehicula. Vivamus ac convallis lorem. Etiam interdum enim id erat accumsan aliquet. Curabitur imperdiet, ligula et hendrerit scelerisque, nisl enim auctor massa, rhoncus consequat nibh ex quis ipsum. Vivamus dignissim mi sed dui bibendum, sit amet blandit orci volutpat. Etiam ac justo sed sapien accumsan interdum nec ut arcu. Pellentesque dapibus erat orci, non consectetur tortor tincidunt ac. Donec posuere eu ipsum vel ornare. Nulla nisl massa, molestie tempor tincidunt eu, pharetra quis quam.
Phasellus lacinia felis sit amet erat blandit porttitor. Aenean et urna finibus, euismod ipsum et, dapibus metus. Quisque bibendum fermentum elit sit amet pharetra. Praesent eros quam, euismod eu sem at, ornare viverra nisi. Pellentesque pretium fermentum nibh, scelerisque laoreet lectus tincidunt id. Aliquam erat volutpat. Proin porttitor, purus cursus efficitur tempus, mauris massa dignissim metus, vel condimentum neque dui id tortor.
Etiam suscipit in mauris at interdum. Etiam tempus dui in rutrum egestas. Nunc quis magna et ex ornare ornare. Sed non tellus sit amet ex consequat efficitur. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse potenti. Sed nec porta ex. Phasellus convallis nunc justo, viverra pharetra ante venenatis sed. Fusce facilisis metus nibh, eu porttitor ipsum eleifend ut. Curabitur tincidunt urna nec urna scelerisque suscipit eget sed velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
Donec dignissim felis a sem bibendum, vitae tempor magna convallis. Vivamus sit amet nisl laoreet, molestie lorem vulputate, molestie velit. Nullam venenatis aliquet erat sit amet euismod. Donec lacinia quis tortor vitae sagittis. Ut nisi mauris, gravida nec egestas vel, rutrum quis enim. Maecenas porttitor egestas ornare. Phasellus lobortis velit erat. Suspendisse molestie gravida ipsum id elementum. Phasellus quis dolor pharetra, varius justo sit amet, eleifend nibh. Praesent quis laoreet dolor.
Proin condimentum fermentum sapien. Pellentesque in commodo nibh, non commodo justo. Duis gravida egestas nisl, vel malesuada est facilisis vitae. Nulla sapien sem, aliquam non ante vel, malesuada pulvinar turpis. In maximus porttitor tristique. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut lacus ex, consectetur vitae magna sed, pulvinar varius nulla. Proin vitae accumsan arcu. Pellentesque tristique vestibulum tristique. Aenean ullamcorper ornare lacus, sed ornare eros sodales ut. Donec vitae felis nulla. Etiam vestibulum scelerisque metus, at tempor sem placerat vitae. Integer volutpat tortor eget dolor rutrum viverra. 
"""
words = ["".join([c for c in word if c in string.ascii_letters]) for word in text.split()]
print("Total words:", len(words))
print(hash_table)
for word in words:
    hash_table.add(word)
hash_table.print()
