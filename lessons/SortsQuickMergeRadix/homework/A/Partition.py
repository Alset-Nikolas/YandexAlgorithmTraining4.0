def partition(N: int, a: str, x: int) -> [int, int]:
    numbers = list(map(int, a.split()))
    l = 0
    for ni in numbers:
        if ni < x:
            l += 1
    return l, N - l


if __name__ == "__main__":
    N = int(input())
    a = input()
    x = int(input())
    result = partition(N, a, x)
    print("\n".join(str(x) for x in result))
