'''
Permutation:
Alle möglichen Anordnungen von gegbenen Elementen (Reihenfolge spielt eine Rolle)

Variation: 
Alle möglichen Anordnungen von jeweils n Elementen aus der gesamten Menge (Reihenfolge spielt eine Rolle)

Kombination:
Alle möglichen Anordnungen von jeweils n Elementen aus einer geamten Menge (Reihenfolge spielt KEINE Rolle)
'''

from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement

numbers = [1, 2, 3]

print('KOMBINATORIK:\n')

# Permutation ohne Wiederholung
print('Permutation ohne Wiederholung:')
for perm in permutations(numbers):
    print(perm)

print()

# Variation ohne Wiederholung
print('Variation ohne Wiederholung:')

for perm in permutations(numbers, 2):
    print(perm)

print()

# Permutation mit Wiederholung
print('Permutation mit Wiederholung:')

for perm in product(numbers, repeat=3):
    print(perm)

print()

# Variation mit Wiederholung
print('Variation mit Wiederholung:')

for perm in product(numbers, repeat=2):
    print(perm)

print()

# Kombination ohne Wiederholung
print('Kombination ohne Wiederholung:')

for comb in combinations(numbers, 2):
    print(comb)

print()

# Kombination mit Wiederholung
print('Kombination mit Wiederholung:')

for comb in combinations_with_replacement(numbers, 2):
    print(comb)
