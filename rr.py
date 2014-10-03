div = ["Carlsen","Caruana","Aronian","Anand","Nakamura"]

def create_schedule(L):
    s = []

    if len(L) % 2 == 1: L = L + ["BYE"]

    for i in range(len(L)-1):

        mid = len(L) / 2
        l1 = L[:int(mid)]
        l2 = L[int(mid):]
        l2.reverse()

        if(i % 2 == 1):
            s = s + [ zip(l1, l2) ]
        else:
            s = s + [ zip(l2, l1) ]

        L.insert(1, L.pop())

    return s


def main():
    print("\nDiv1\n")
    for round in create_schedule(div):
        for match in round:
            print(match[0] + " - " + match[1])
        print("")

if __name__ == "__main__":
    main()
