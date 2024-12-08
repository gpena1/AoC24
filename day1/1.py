file = open('../input','r')
arr1,arr2 = [],[]
for line in file:
    line = line.strip()
    a,b = map(int,line.split())
    arr1.append(a); arr2.append(b)

arr1.sort(); arr2.sort()
print(sum(abs(a-b) for a,b in zip(arr1,arr2)))