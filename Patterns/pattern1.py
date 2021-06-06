a, b = map(int, input("ENter rows & columns").split())
for i in range(a):
    print("\n")
    for j in range(b):
        if i == 0 or i == a-1:
            print("*", end="")

        elif j == 0 or j == b-1:
            print("*", end="")
        else:
            print(" ", end="")
