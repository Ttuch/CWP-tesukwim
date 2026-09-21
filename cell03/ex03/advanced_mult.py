row = 0

while row < 11 :
    column = 0
    start = 0
    print(f"Table de {row}:", end=" ")
    while column <= 10:
        print(start, end=" ")
        start += row
        column += 1
    print("")
    row += 1