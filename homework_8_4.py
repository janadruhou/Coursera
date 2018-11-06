romeo = open('romeo.txt')
final = list()
for line in romeo:
    lines = line.strip()
    s_lines = lines.split()
    
    for word in s_lines:
        if word is not in final:
            final.append(word)
        else: 
            continue

    print((final)gi
