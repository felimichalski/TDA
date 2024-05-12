from queue import Queue

def solve():
    n: int = int(input())

    s: list[str] = list(input())
    t: list[str] = list(input())

    if (len(s) != len(t)):
        return print(-1)

    diffA: Queue[int] = Queue()
    diffB: Queue[int] = Queue()

    for i in range(n):
        if s[i] != t[i]:
            if(s[i] == 'a'):
                diffA.put(i)
            else:
                diffB.put(i)

    if ((diffA.qsize() + diffB.qsize()) % 2 != 0):
        return print(-1)

    swaps: list[(int, int)] = []

    while(diffA.qsize() > 1):
        swaps.append((diffA.get() + 1, diffA.get() + 1))

    while(diffB.qsize() > 1):
        swaps.append((diffB.get() + 1, diffB.get() + 1))

    if(diffA.qsize() > 0):
        diffA_value: int = diffA.get()
        swaps.append((diffA_value + 1, diffA_value + 1))
        swaps.append((diffA_value + 1, diffB.get() + 1))


    print(str(len(swaps)))
    for swap in swaps:
        print(str(swap[0]) + " " + str(swap[1]))

if __name__ == '__main__':
    solve()