size=int(input("Enter number of elements: "))
arr = []

for i in range(size):
    num = int(input("Enter number: "))
    arr.append(num)

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] == 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)