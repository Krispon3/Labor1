n = int(input(""))
mas = []
max = [0,0]
proverk_sovp = []
for i in range(n):
    cou = input("")
    mas.append(cou)
    proverk_sovp.append(int(cou[:1]))
proverk_sovp.sort()
proverk_sovp.append(0)
num1 = 0
for i in range(len(proverk_sovp)-1):
    if proverk_sovp[i] == proverk_sovp[i+1]:
        num1 += 1
    else:
        if num1 + 1 > max[1]:
            max[0] = proverk_sovp[i]
            max[1] = num1 + 1
            num1 = 0

print(max,mas)
