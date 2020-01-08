genlist = []
anslist = [0]
N = int(input())

for i in range(N):
    gen = i
    while i > 0:
        gen += (i % 10)
        i //= 10
    genlist.append(gen)

for i in genlist:
    if N == i:
        anslist.append(genlist.index(i))
        break
print(anslist[-1])














#어떤 자연수 주어지고, N 까지 제너레이터 다 구해서 그 중

#216을 만드는 가장 작은 애를 찾아라 -> 애들의 제너레이터 다 구해서 만약 198에서 216이 처음 나오면 그거.