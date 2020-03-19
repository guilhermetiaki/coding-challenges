def run():
    diff = int(input())
    line = list(input())

    women = 0
    men = 0 

    while len(line) > 0:
        if abs(men - women) > diff:
            print(men+women-1)
            return
        if men - women > 0:
            if line[0] == 'W':
                women += 1
            elif len(line) > 1 and line[1] == 'W':
                women += 1
                line[1] = 'M'
            else:
                men += 1
        elif men - women < 0:
            if line[0] == 'M':
                men += 1
            elif len(line) > 1 and line[1] == 'M':
                men += 1
                line[1] = 'W'
            else:
                women += 1
        else:
            if line[0] == 'M':
                men += 1
            else:
                women += 1
        del line[0]
    print(men+women)    

if __name__ == "__main__":
    run()