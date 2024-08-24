arr = [1,1,1,2,2,2,2,3,3,4]

update = arr[0]
counter = 1
pcounter = 0

for i in range(0 , len(arr),counter):
    if pcounter<counter:
        update = arr[i]
        pcounter = counter
    for j in range(i+1,len(arr)):
        counter = 1
        if arr[i] == arr[j]:
            counter+=1

print(update)
