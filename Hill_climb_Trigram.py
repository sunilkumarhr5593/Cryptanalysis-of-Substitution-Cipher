import time
start_time = time.time()

import pandas
import numpy as np
import random
import string
import sys
from fuzzywuzzy import fuzz




stdoutOrigin=sys.stdout 
sys.stdout = open("test1.txt", "w")

print()
print("     The below program restarts 10 times with random keys.")
print("     Two pairs of key will be swapped during key modification.")
print("     The algorithm runs for 200 samples with key modification")

df_trigram = pandas.read_csv('count3l.txt',index_col=None, delim_whitespace=True, names=('trigram', 'prob'))

new_sum_3 = df_trigram.sum(axis = 0, skipna = False)  # sums all prob of bigram
total_prob_3 = (new_sum_3[0]) 

avg_prob_3 = []

df1_3 = (df_trigram.iloc[:,1]) / (total_prob_3) #first row of data frame
avg_prob_3 = np.log2(df1_3)

trigram_prob = [] 
tprob= df_trigram.iloc[:,0]
trigram_prob = tprob                                                                 ##########

max_prob = max(avg_prob_3) 


dict_prob_3 = dict((trigram_prob[index], avg_prob_3[index]) for index in range(len(trigram_prob)))

nanK = 'nan'
nanV = -10.55620230489656

nanKl = []
nanVl = []


nanKl = np.append(nanKl, nanK)
nanVl = np.append(nanVl, nanV)


dict_test = dict((nanKl[i], nanVl[i]) for i in range(len(nanKl)))
dict_prob_3.update(dict_test)

#print(dict_prob_3)
###########################Cryptanalysis of Caesar Cipher#############################################

alphabets = 'abcdefghijklmnopqrstuvwxyz'


cipher_key = 'wzdqcvaonktghlfesxjbiymurp'
#cipher_key =   'XZTJWUMOBEPARIQKDLFSCHYGNV' # Alphabets in english language
#text = input('Enter the string :')
print()        # Input message
text = "defendtheeastwallofthecastle"
print()
text_list = []
text_list = text.lower()
print("The input text is : ",text_list)

print()
alphabets_list = alphabets
cipher_key_list = cipher_key.lower()
seq2 = cipher_key_list


dictionary = dict((alphabets_list[i], cipher_key_list[i]) for i in range(len(cipher_key_list)))
crypt = []
cipher_text_list = []    
for i in range(len(text_list)):
    res = dictionary.get(text_list[i])
    crypt = np.append(crypt, res)
    res_join = " ".join(str(x) for x in crypt)
    cipher_text = res_join.replace(" ", "")
    cipher_text_list = cipher_text
print("The cipher text is : ",cipher_text_list)
print()

print("The decryption key is: ", seq2) 
print()

dictionary1 = dict((cipher_key_list[i], alphabets_list[i] ) for i in range(len(alphabets_list)))

crypt1 = []
for i in range(len(crypt)):
    res = dictionary1.get(crypt[i])
    crypt1 = np.append(crypt1, res)
    res_join = " ".join(str(x) for x in crypt1)
    open_text = res_join.replace(" ", "") 
#print("The open text is : ",open_text)   
#print() 


n = 3
temp = []
out = [(open_text[i:i+n]) for i in range(len(open_text)+1 -n)]
temp = out

prob_k1 = 0
for i in range(len(temp)):
    res = dict_prob_3.get(temp[i])
    prob_k1 = res+  prob_k1

print("The prob value of open text is: ",prob_k1)

print()
print("========  The hill climbimg algorithm with random restart starts now  ======================")

print()

def key(stringLength=26):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, stringLength))

random_list = []
random_list = key()
global key_1
key_1 = random_list
print("The initial random key is: ",key_1)

def swap(key_1, i, j, s, t):
    key_1 = list(key_1)
    key_1[i], key_1[j], key_1[s], key_1[t] = key_1[j], key_1[i], key_1[t], key_1[s]
    return key_1

def swap_1(key_1, i, j, s, t, a, b, c, d):
    key_1 = list(key_1)
    key_1[i], key_1[j], key_1[s], key_1[t], key_1[a], key_1[b], key_1[c], key_1[d] = key_1[j], key_1[i], key_1[t], key_1[s], key_1[b], key_1[a], key_1[d], key_1[c]
    return key_1

global key_2
key_2 = swap_1(key_1,0,1, 24, 25,4,8, 6, 9)
key_2 = ''.join(str(x) for x in key_2)

def hill_climb(key_1):
    
    dictionary = dict((key_1[i], alphabets_list[i]) for i in range(len(key_1)))
    dic_ini = []
 
    for i in range(len(cipher_text_list)):       
        crypt2 = dictionary.get(cipher_text_list[i])
        dic_ini = np.append(dic_ini, crypt2)
        res_join = " ".join(str(x) for x in dic_ini)
    res_replace = res_join.replace(" ", "") 

    n = 3
    out = [(res_replace[i:i+n]) for i in range(len(res_replace)+1 -n)]
    temp = out
    prob_k = 0
    for i in range(len(temp)):
        res1 = dict_prob_3.get(temp[i])
        prob_k += np.sum(res1)
    return prob_k
    
k1 = []
y1 = [] 

def open_text(key_1):
    dictionary = dict((key_1[i], alphabets_list[i]) for i in range(len(key_1)))
    dic_ini = []
    for i in range(len(cipher_text)):
        
        crypt = dictionary.get(cipher_text[i])
        dic_ini = np.append(dic_ini, crypt)
    res_join = " ".join(str(x) for x in dic_ini)
    res_replace = res_join.replace(" ", "")  
    return res_replace  

def out_func(key_1):
    dictionary = dict((key_1[i], alphabets_list[i]) for i in range(len(key_1)))
    dic_ini = []
    for i in range(len(cipher_text)):
        
        crypt = dictionary.get(cipher_text[i])
        dic_ini = np.append(dic_ini, crypt)
    res_join = " ".join(str(x) for x in dic_ini)
    res_replace = res_join.replace(" ", "")  
    #file = open("Case_1_bi_open.txt","a")
    #file.write("The open text from the key having max prob {} is:" .format(z) +  res_replace + "\n")
    print("The original decryption key is: ",seq2)
    print("The selected key from this case is: ", seq1)
   # test = (levenshtein(seq1, seq2)) / ((len(seq1) + len(seq2)))
   # print("The normalized value is: ",test)
    #print(seq1)
    #Ratio = fuzz.ratio(seq1.lower(),seq2.lower())
    #print("The ratio compared between obtained key and original key is: ",Ratio/100)  

    #file.close() 

def key_try(key_1,i,j,s,t,a,b,c,d):
    new_key = ''.join(str(x) for x in swap_1(key_1,i,j, s, t,a,b,c,d))
    new_key_value = hill_climb(new_key)    
    return new_key, new_key_value

def test(key_1, value_1, n):
    main_key_value = 0
    main_key_list = []  
    k1 = []
    y1 = []
    for _ in range(n):
        m,n,o,p,q,r,s,t = np.random.choice(range(25), 8, replace=False)
        new_key, new_key_value = key_try(key_1,m,n,o,p,q,r,s,t)
        if(new_key_value > value_1):
            main_key_value = new_key_value
            main_key_list = new_key
            #print("The prob using next key is {} and the key is {}".format(main_key_value ,"".join(str(x) for x in main_key_list))) 
            #print(main_key_list, main_key_value)
            break
        #print("The number of best keys generated in each iteration are: ",n)
        main_key_list  = key_1
        main_key_value = value_1
        k1 = np.append(k1, main_key_list)
        y1 = np.append(y1, main_key_value)  
    return main_key_list, main_key_value

def multiple():
    global key_final
    global value_final
    global max_key
    global max_value
    global test1_key, test_key
    global test_value
    global seq1, seq2
    global y
    global z, a, b
    global k1, y1, dictionary_f1

    key_1 = random_list
    value_1 = hill_climb(key_1)
    print("The initial key has a prob value of {} and the key is {} : ".format(value_1, "".join(str(x) for x in key_1)))
    k1 = np.append(k1, key_1)
    y1 = np.append(y1, value_1)

    for _ in range(2000000):
        main_key_list, main_key_value = test(key_1, value_1, 250)
        k1 = np.append(k1, main_key_list)
        y1 = np.append(y1, main_key_value)              
        if(value_1 != main_key_value):
            main_key_list, main_key_value = test(key_1, value_1, 200)
        k1 = np.append(k1, main_key_list)
        y1 = np.append(y1, main_key_value)
    #print("The number of best keys generated in each iteration are: ",n)
        #print("The prob using next key is {} and the key is {}".format(main_key_value ,"".join(str(x) for x in main_key_list)))
    dictionary_f1 = dict((k1[i], y1[i]) for i in range(len(k1)))
    #for key, value in sorted(dictionary_f1.items(), key=lambda item: item[1]):
        #print("%s: %s" % (key, value))
        #print("The prob using next key is {} and the key is {}".format(value ,"".join(str(x) for x in key)))
    y = max(dictionary_f1, key=dictionary_f1.get)
    #seq3 = y
    #res = sum(x == y for x, y in zip(seq3, seq2)) 
    #print("Summation of Identical elements : " + str(res))
    z = max([i for i in dictionary_f1.values()])
    return dictionary_f1
    return k1, y1       
            
multiple()

print("The prob using best key is {} and the key is {}".format(z ,"".join(str(x) for x in y)))
print()

finalKey = []
finalValue = []

finalKey = np.append(finalKey, y)
finalValue = np.append(finalValue, z)

for _ in range(0):   
    def key(stringLength=26):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.sample(letters, stringLength))
        #print("The prob using next key is {} and the key is {}".format(main_key_value ,"".join( 
        #print("The prob using next key is {} and the key is {}".format(main_key_value ,"".join(
     
    random_list = []
    random_list = key()
    key_1 = random_list
    print("The initial random key is: ",key_1)
    
    k1 = []
    y1 = [] 
    
    multiple()
     
    finalKey = np.append(finalKey, y)
    finalValue = np.append(finalValue, z)
    print("The prob using best key is {} and the key is {}".format(z ,"".join(str(x) for x in y)))
    print()

print("==================  The hill climbing algorihm with random restart ends here    ====================")
print()

print()
print("     ==============  Final prob and key  ========================    ")
print()

# =============================================================================
# finalKey = np.append(finalKey, cipher_key_list)
# finalValue = np.append(finalValue, prob_k1)
# =============================================================================

dictionary_max = dict((finalKey[i], finalValue[i]) for i in range(len(finalKey)))
y_max = max(dictionary_max, key=dictionary_max.get)
seq1 = y_max
z_max = max([i for i in dictionary_max.values()])
 
print("The max prob among the all the iteration is {} and the key is {}".format(z_max,y_max))
print()
print(out_func(y_max))
print()

res = sum(x == y for x, y in zip(seq1, seq2)) 

print("Summation of Identical elements : " + str(res)) 
print("The similarity percentage between original key and selected key is: ",res/26)

print("open text from the key {}  having max prob  {}  is  {}  " .format(y_max, z_max ,open_text(y_max)))
print()

print("This runtime of the program is %s seconds ---" % (time.time() - start_time))
print()
import logging
import platform,socket,re,uuid,json,psutil
import pprint

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

pprint.pprint(getSystemInfo())

sys.stdout.close()
sys.stdout=stdoutOrigin


print()