import os

local = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(local, 'input')

def main ():
    with open(input) as f:
        lines = f.read().splitlines()
        plane = [None] * 2 ** 10
        # print(plane)

        for line in lines:
            data = line.split(" ")[0]

            ticket = int(\
                data[0:7].replace('B', '1').replace('F', '0') + \
                data[7:].replace('R', '1').replace('L', '0'), 2)
            # print(ticket)

            plane[ticket] = False
        
        # print(plane)

        for ticket in range(2 ** 10):
            try:
                if (plane[ticket] is None and plane[ticket - 1] is False and plane[ticket + 1] is False):
                    print(f"Empty seat id is {ticket}")

            except:
                pass
                # print(f"Used seat id is {ticket}")

        # print("implementation missing")

main()
