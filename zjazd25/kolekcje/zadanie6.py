liczby = [5, 2, 1, 4, 3]

index_max = None
index_min = None

for i in range(len(liczby)):
    if index_min is None or liczby[i] > liczby[index_min]:
        i = index_min
    if i

    print(i, liczby[i])

# zamieniamy miejscami
temp = liczby[index_min]
liczby[index_min] = liczby[index_max]
liczby[index_max] = temp