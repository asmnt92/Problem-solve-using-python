n,m=map(int,input().split())
cnt=0
for num in range(n,m+1):
    check=True
    tem=num
    while tem :
        if tem%10==4 or tem%10==7:
            check=True
            
        else:
            check=False
            break
        tem//=10

    if check :
        print(num,end=' ')
        cnt+=1

if not cnt :
 print(-1)

# problem link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/M