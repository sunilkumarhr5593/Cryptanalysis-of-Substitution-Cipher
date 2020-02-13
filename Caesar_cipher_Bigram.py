import time
start_time = time.time()

import pandas
import itertools
from math import log
import math
import numpy as np

df = pandas.read_csv('count2l.txt',index_col=None, delim_whitespace=True, names=('bigram', 'prob'))
#print(df)

new_sum = df.sum(axis = 0, skipna = False)  # sums all prob of bigram
total_prob = (new_sum[1]) 
#print("The log value total occurence from the bigram data is: ",np.log2(total_prob))           # total prob of all bigram
#print()

avg_prob = []

df1 = ((df.iloc[:,1]) / (total_prob)) #first row of data frame
avg_prob = np.log2(df1)
#print("The log of avgerage probabiliy of each bigram is: ",avg_prob)
#print()
#print(total_prob)  

bigram_prob = [] 
bprob= df.iloc[:,0]
bigram_prob = bprob                                                                 ##########
#print(bigram_prob)  

max_prob = max(avg_prob) 
#print("The log value of max prob is: ",max_prob)


dict_prob = dict((bigram_prob[index], avg_prob[index]) for index in range(len(bigram_prob)))
#print("The bigram:",dict_prob, sep = " ")

### testing purpose
#print(list(dict_prob.keys())[2])   # output >>> Key2
#print(list(dict_prob.values())[2])  # output >>> Value2

###########################Cryptanalysis of Caesar Cipher#############################################

alphabets = 'abcdefghijklmnopqrstuvwxyz'   # Alphabets in english language
text = input('Enter the string :')
print()        # Input message
#text = "hello hell"
shift = 22 

shift1 = shift


def encrypt(n, plaintext):                 # Function used for encryption to get cipher text
    result = ''

# Since lower case alphabets is used as the plain text.
# Here index of the input string will be considered and shift value will be added,
# and performs modulo operation for encryption
    for l in plaintext.lower():   
# =============================================================================
#         if (alphabets == " "):
#             result = result+ " "
# =============================================================================
        try:
            i = (alphabets.index(l) + shift) % 26   
            result += alphabets[i]
        except ValueError:
            result += l

    return result.lower()

encrypted = encrypt(shift, text)         #Encrypts the text message using shift value
print('The encrypted text is:', encrypted)
#print()

#==================below is to calculate prob of encrypted text===================================

string = encrypted
#string = string.replace(" ", "")
#print(string)
n = 2
temp = []
out = [(string[i:i+n]) for i in range(len(string)+1- n)]
temp = out
#print("The encrypted text is split as bigram: ",temp)
#print()

prob_list = []
for i in range(len(temp)):
    prob = dict_prob.get(temp[i])
    prob_list = prob
    #print(prob_list)
    prob_max = np.max(prob_list)
    
#print("the candidate with max prob is '{}' and the candidate is '{}' ".format(prob_max, temp[i]))
#print()

add = 0
for i in range(len(temp)):
    #res = float(dict_prob.get(temp[i]))
    res = dict_prob.get(temp[i])
    add = res+add 
    
#print("The total prob of encrypted text is: ",add)   
#print()
    
##### Need to get the last element from add and print in output ??????????????##############
#######################################################################################################
    
def decrypt(n, encrypted):                 # Function used for decryption to get back plain text
    result = ''

    for l in encrypted:
# =============================================================================
#         if (alphabets == " "):
#             result = result+ " "
# =============================================================================
        try:
            i = (alphabets.index(l) - shift) % 26
            result += alphabets[i]
        except ValueError:
            result += l

    return result    

decrypted = decrypt(shift, encrypted)    #Decrypts the encrypted message to get back plain text

print()
print('The text decrypted from cipher text is:', decrypted)
print()

#==================below is to calculate prob of decrypted text===================================

string1_list = []
string1 = decrypted

string1 = string1.split()
#print(string1)
#string1 = string1.replace(" ", "")
#string1 = string1.split()
string1_list = string1
#print("The candidates of decrypted text are: ",string1_list)
#print()
#print(len(string1_list[1]))
#add_list_dec_prob = []

n = 2
out1_add = []

for x in range(len(string1_list)):
    #print(len(string1_list))    
    out1 = [(string1_list[x][i:i+n]) for i in range(len(string1_list[x])+1 -n)]
    #print("Candidates split as bigram for prob calculation: ",out1)
    res1 = [dict_prob.get(out1[i]) for i in range(len(out1))]
    #print(res1)
    res2 = np.sum(res1)
    #print(res2)
    out1_add = np.append(out1_add,res2)

out1_sum_list = []
out1_sum = np.sum(out1_add)
out1_sum_list = out1_sum    
#print(out1_sum_list)
   
dictionary = dict(zip(string1_list, out1_add))   
#print()
#print("The candidate and prob values are: ",dictionary) 
#print()

maximum = max(dictionary, key=dictionary.get)
#11print("the candidate with max prob is '{}' and the candidate is '{}' ".format(dictionary[maximum], maximum))

###################### Brute force attack ###################################################

#print()
print("The brute force attack tells that the text was encrypted at key: ",shift)  
print()

for shift in range(0, len(alphabets)):    
    brute_force = ''
    for char in encrypted:           
        if char in alphabets:
            num = alphabets.find(char)    
            num = num - shift                 
            if num < 0:
                num = num + len(alphabets)
            brute_force = brute_force + alphabets[num]
        else:
                brute_force = brute_force + char         
    #print("<Brute force attack for Shift> #%s is : %s "%(shift,brute_force))
    
     
    bf_list = []
    bf_string = brute_force
    #bf_string = bf_string.replace(" ", "")
    bf_string = bf_string.split()
    bf_list = bf_string
        
    n = 2
    out2_add = []
    
    for x in range(len(bf_list)):
        #print(len(string1_list))    
        out2 = [(bf_list[x][i:i+n]) for i in range(len(bf_list[x])+1 -n)]
        #print("Candidates split as bigram for prob calculation: ",out1)
        res3 = [dict_prob.get(out2[i]) for i in range(len(out2))]
        #print(res1)
        res4 = np.sum(res3)
        #print(res2)
        out2_add = np.append(out2_add,res4)
    
    out2_sum_list = []
    out2_sum = np.sum(out2_add)
    out2_sum_list = out2_sum    
    #print(out2_sum_list)
# =============================================================================
#     out2_add = []        
#     add3 = 0
#     for i in range(len(bf_out)):
#          #res = float(dict_prob.get(temp[i]))
#          res3 = dict_prob.get(bf_out[i]) 
#          res4 = np.sum(res3)
#          out2_add = np.append(out2_add,res4)
#          out2_sum_list = []
#          out2_sum = np.sum(out2_add)
#          out2_sum_list = out2_sum  
#          print(out2_sum_list)
#          #add3 = res3 + add3 
# =============================================================================
                 
    print(brute_force)   
         
    #print("The total prob of open text candidate is: ",add)   


#print(shift1)
print()
print("After Bruteforce attack max prob is {} , at shift {}  ".format(out1_sum_list, shift1))
print()    

print("This runtime of the program is %s seconds ---" % (time.time() - start_time))
print()       #print(brute_force)
