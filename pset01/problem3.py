subs = ''
prev = ''
l = ""
for i in s:
    if l <= i:
        subs += i
        l = i
    else:
        l = i
        if len(subs) > len(prev):
            prev = subs
        subs = i

if len(subs) > len(prev):
    print("Longest substring in alphabetical order is:" ,subs)
else:
    print("Longest substring in alphabetical order is:" ,prev)
