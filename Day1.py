input = [int(x) for x in open('input').read().strip('\n').splitlines()]

#Part1
def find(target, data):
    inv = set()
    for x in data:
        if x in inv:
            return x * (target - x)
        inv.add(target - x)
    return None

print(find(2020, input))

#Part2
index = 0
while True:
    first = input[index]
    result = find(2020-first, input[index+1:])
    if result is not None:
        print(result * first)
        break
    index = index + 1