def main():
    n = int(input())
    arr = []
    while len(arr) < n:
        arr.extend(map(float, input().split()))
        arr = arr[:n]
        d = float(input())
        if n == 0:
            print(0)
            return
        mean = sum(arr) / n
        count = sum(1 for x in arr if abs(x - mean) <= d)
        print(count)
        if __name__ == "__main__":
            main()
