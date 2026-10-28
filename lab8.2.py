def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
        expected = set(range(1, n + 1))
        is_latin = True
    for i in range(n):
        if set(matrix[i]) != expected:
            is_latin = False
            break
            col = set(matrix[j][i] for j in range (n))
            if col != expected:
                is_latin = False
                break
                if is_latin:
                    print("Yes")
                else:
                    print("No")
                    if __name__ == "__main__":
                        main()


