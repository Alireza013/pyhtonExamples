MAXIMUM_TRIERS = 1000

def multiples(item = 10, sum = 23) -> int:
    while item < MAXIMUM_TRIERS:
        if (item % 3 == 0) or (item % 5 == 0):
            sum += item
        item += 1
    print(sum)

multiples()
