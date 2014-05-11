class password_analyzer:
    def __init__(self):
        self.frequencies={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
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
     
            



            
            
        
password_analyzer = password_analyzer()




print(password_analyzer.parse())
print(password_analyzer.length_of_word)
print(password_analyzer.frequencies)
        
