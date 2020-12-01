def main ():
    sum = 0;
    values = {}

    with open('./input/1') as f:
        lines = f.read().splitlines()
        numbs = [int(x) for x in lines]
        numbs.sort()

        for numb in numbs:
            values[numb] = True;

        for numb in numbs:
            flag = values.get(2020 - numb, False)
            if flag:
                print("Found value", numb, "With sum:", numb * (2020-numb))
                return;

    print("Not found :(")

main()
