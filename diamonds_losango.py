n = list(map(int, input().split()))
print(n)
while n[0] < 1 or n[1] < 1:
  n = list(map(int, input().split()))
k = list()

for i in range(n[0]):
  valor = int(input())
  while valor < 0 or valor > 10001:
    valor = int(input())
  k.append(valor)

k.sort()

contador = 0
for i in range(n[0]):
  contador_temp = 1
  for j in range(i+1, n[0]):
    if abs(k[i] - k[j]) <= n[1]:
      contador_temp += 1
    else:
      break
  contador = max(contador, contador_temp)

print(k,n, contador)
