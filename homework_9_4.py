# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

text = open("mbox-short.txt")

emails = list()

for lines in text:
    if not lines.startswith("From"): continue
    s_line = lines.split()
    emails.append(s_line[1])
    
count = dict()

for email in emails:
    count[email] = count.get(email, 0) + 1
    
amount = None
adresses = None

for key, val in count.items():
    if val > amount:
        amount = val
        adresses = key

print (adresses, amount)