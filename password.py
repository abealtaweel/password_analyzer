class password_analyzer:
    def __init__(self):
        self.frequencies={}
        self.length_of_word ={}
        
    def parse(self):
        with open('passwords.txt') as f:
            for line in f:
                print (line)
                #rstrip 
                length = len(line.rstrip())
                
                #  if lengh already in lengh_of_word
                # add count(the value) to 1
                if (length in self.length_of_word):
                    self.length_of_word[length]+=1
                #  add length in length of word and make it count to 1
                else:
                    self.length_of_word[length]=1
                
                #for each char in line 
                for c in line.rstrip():
                #if char in frequencies
                    if (c in self.frequencies):
                    #increase char's count by 1 
                        self.frequencies[c]+=1
                    #else
                    else:
                    #add char to frequences, set its count to 1
                        self.frequencies[c]=1
            return
              
#creating an object       
password_analyzer = password_analyzer()

#console output
#print the passwords
print("print the passwords:")
print(password_analyzer.parse())

#Print length of words
print("The length of passwords:")
print(password_analyzer.length_of_word)

#Print frequencies of characters
print("Frequencies:")
print(password_analyzer.frequencies)