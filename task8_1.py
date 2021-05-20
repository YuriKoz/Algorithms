import hashlib

S = input("Введите строку из маленьких латинских букв: ")
N = len(S)
array = set()

for i in range(N):
    if i == 0:
        N = len(S) - 1
    else:
        N = len(S)
    for j in range(N, i, -1):
        print(S[i:j])
        array.add(hashlib.sha1(S[i:j].encode('utf-8')).hexdigest())
print(array)

print(f"Количество различных подстрок в строке '{S}' равно {len(array)}.")
