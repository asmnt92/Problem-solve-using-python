n=int(input())
l=n
new=0

while l:
    dig=l%10
    new=new*10+dig
    l//=10

print(new)
print('YES' if n==new else 'NO')


# Problem link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/I