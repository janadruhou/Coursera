#email = input("Enter file name:")
text = open("mbox-short.txt") 
count = 0

for line in text:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    position = line.find(":")
    number = line[position + 1 :]
    value = number.strip()

    print(value)

    