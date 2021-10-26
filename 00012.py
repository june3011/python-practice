# 1 kim 2 hong 3 lee
hash={}
for _ in range(3):
    key, value=input().split()
    hash[int(key)]=value
# hash = dict.fromkeys(key, value)
print(hash)