num = [1,2,0,0]
k = 34 
sum_nk = num[0]
for i in range(1, len(num)):
    sum_nk = sum_nk*10 + num[i]

sum_nk = sum_nk + k
sum_nk = str(sum_nk)
arr = []
for i in sum_nk:
    arr.append(int(i))
print(arr)
