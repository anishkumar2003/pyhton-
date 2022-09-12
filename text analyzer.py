def count_char(text, char):
  count = 0
  for e in text:
    if e == char:
      count += 1
  return count
c=input("enter a file name: ")
b=input("Enter a word you want to search how many times it apper in this file:")
with open(c) as f:
    text=f.read
print(count_char("text",b))
