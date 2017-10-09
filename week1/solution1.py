import sys
digit_string = sys.argv[1]

summa = 0
for c in digit_string:
    summa += int(c)

print(summa)
