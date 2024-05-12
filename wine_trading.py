def solve():
    result: list[str] = []
    while(True):
        inhabitants: int = int(input())
        if (inhabitants == 0):
            break

        # Read all cases
        demands: list[int] = list(map(int, input().split()))

        work_amount: int = 0
        acc: int = 0
        
        for demand in demands:
            # For each demand, add the corresponding amount of work,
            # regardless of whether the inhabitant wants to buy or sell,
            # taking into account what has already been done.
            acc += demand
            work_amount += abs(acc)

        result.append(str(work_amount))

    print("\n".join(res for res in result))

        

if __name__ == '__main__':
    solve()