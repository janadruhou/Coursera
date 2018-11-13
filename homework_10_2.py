# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

text = open("mbox-short.txt")

counts = dict()

for lines in text:
    if not lines.startswith("From "): continue
    time = lines.split()[5].split(":")
    counts [time[0]] = counts.get(time[0],0) + 1

lst = list ()

for key, value in counts.items():
    lst.append( (key,value) )

lst.sort()

for hour, amount in lst:
    print (hour, amount)