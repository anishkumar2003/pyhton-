def find_longest_word(word_list):  
    longest_word = ''  
    for word in word_list:    
          print(word, len(word))  


words = input('Please enter a few words')  
word_list = words.split()  
find_longest_word(word_list)

def infinite_sevens():
  while True:
    yield 7
        
for i in infinite_sevens():
  print(i)
  
