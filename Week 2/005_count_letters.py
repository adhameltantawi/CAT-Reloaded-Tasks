s = input()
count = {}
for ch in s:
    if ch in count:
        count[ch] +=1
    else:
        count[ch] = 1
for ch in sorted(count):
    print(f"{ch} : {count[ch]}")
        