# most_frequent function
def most_frequent(string) :
    
    # to remove duplicates from a string
    str1 = "".join(dict.fromkeys(string))
    
    # check frequency of each alphabet and add the alphabet and count in dictonary
    for i in str1 :
        count = 0
        for k in string :
            if i == k :
                count = count + 1
        obj.add( i, count )
        
# class to create a dictonary        
class dictonary(dict) :
    def __init__ (self):
        self = dict()
    def add( self, key, value ) :
        self[key] = value
# input        
str1 = input("Please enter a string : ")
print(str1)
obj = dictonary()
print("Output :")

#calling the most_frequent function 
most_frequent(str1)

# sorting and printing the frequency of alphabet in decrasing order
sort = dict(sorted(obj.items(), key = lambda item: item[1], reverse = True))
for key, value in sort.items() :
    print( key , "=", value)
