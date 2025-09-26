i = int(input("введите целое число,длину последовательности "))
count_otric = 0
for x in range(i):
    if int(input()) < 0:
        count_otric +=1
print(count_otric)
