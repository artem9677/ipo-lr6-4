string = str(input("Введите строку: "))
i = 0
arr = list()

with open('text.txt',encoding="utf-8") as file:
    for line in file:
        if string in line:
            arr.append(line)
            i+=1

print("Количество строк, содержащих",string,"=",i)
arr.sort()
for i in range(len(arr)):
    print(arr[i])
