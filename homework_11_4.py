# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing 
# and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_147848.txt (There are 79 values and the sum ends with 114)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. 
# Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

import re

text = open("sample.txt")
nums = list()
for lines in text:
    s_line = lines.split()
    stuff = re.findall('[0-9.]+', s_line)
    num = float(stuff)
    nums.append(num)

print(nums)
