'''
Created on Oct 25, 2014

@author: David
'''


import shelve


typesofpeople = ""

typesofpeople = shelve.open("typesofpeople")
typesofpeople["0"] = "test"

print(typesofpeople["0"])


print(range(5))

top = [range(0,5)]
print(top)



if __name__ == '__main__':
    for i in top:
        typesofpeople[str(i)] = 0
        print(typesofpeople[i])
        pass



typesofpeople.close()
