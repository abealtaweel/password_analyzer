class password_analyzer:
    def __init__(self):
        self.frequencies={}
        self.length_of_word ={}
        
        # a dictionary to store user password
        self.user_password ={}
        
    def parse(self):
        with open('passwords.txt') as f:
            for line in f:
                #print (line)
                #rstrip 
                length = len(line.rstrip())
                
                #if lengh is already in lengh_of_word
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
                    
        #store user password to dictionary self.user_password{}                
        password=input('Input a password to check against the database: ')
        self.user_password['User Password:']=password          
               
#creating an object       
password_analyzer = password_analyzer()

#console output
(password_analyzer.parse())

#Print length of words
print("The lengths of passwords stored in the database:")
print(password_analyzer.length_of_word)

#Print frequencies of characters
print("Frequencies of characters stored in the database:")
print(password_analyzer.frequencies)
print(password_analyzer.user_password)