import sys
steps = int(sys.argv[1])

i = 0
while i < steps:
    i += 1
    print(' ' * (steps - i) + '#' * i)
