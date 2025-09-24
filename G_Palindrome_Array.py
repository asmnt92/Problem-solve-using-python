n=int(input())
lst=list(map(int,input().split()))

# lst2=[lst[i] for i in range(n-1,-1,-1)]
# lst2=lst[::-1]
lst2=[]
for i in range(len(lst)-1,-1,-1):
    lst2.append(lst[i])

print('YES' if lst==lst2 else 'NO')


# problem link:https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G