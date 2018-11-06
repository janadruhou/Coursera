romeo = open('romeo.txt')
lst = list()
for line in romeo:
    lines = line.rstrip().split()
    for word in lines:
        if word in lst: continue
        else:
            lst.append(word)
lst.sort()      
print(lst)
