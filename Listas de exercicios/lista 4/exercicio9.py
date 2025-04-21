N = int(input()) 

for _ in range(N):
    X, Y = map(int, input().split())
    
    if Y == 0:
        print("divisao impossivel")
    else:
        resultado = X / Y
        print(f"{resultado:.1f}")
