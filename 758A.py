

n = int(input())
    
burle = list(map(int, input().split()))
burle = sorted(burle)
maxi = burle[-1]
    
count = 0
for i in burle:
    count += maxi - i
    
print(count)