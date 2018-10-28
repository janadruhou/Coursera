#email = input("Enter file name:")
text = open("mbox-short.txt") 
count = 0
tot = 0
ans = 0
for line in text:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    count = count + 1
    num = float(line[21:])
    tot = num + tot

ans = tot / count        
 
print("Average spam confidence:", ans)
    