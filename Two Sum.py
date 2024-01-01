def twoSum(arr, target, n):
    arr.sort()
    a,l,r,found=[],0,len(arr)-1,False
    while l<r:
        sum=arr[l]+arr[r]
        if sum==target:
            found=True
            a.append([arr[l],arr[r]])
            l+=1
            r-=1
        elif sum<target: l+=1
        else: r-=1
    if not found: a.append([-1,-1])
    return a
    pass

def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr

def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))

t = int(input().strip())
for i in range(t) :

    n, target, arr = takeInput()

    ans = twoSum(arr, target, n)
    printAns(ans)
