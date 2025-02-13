empty_list = []
print(empty_list)

num = [1,2,3,4]
print(num)

triples = [1,2,3,4]*3
print(triples)

alist = [100,200,300,400,500]
alist = alist[::-1]
print(alist)

#word matching 

def matching_words(Words):
    ctr = 0
    lst =[]
    for word in Words:
        if len(word)>1 and word[0] == word[-1]:
            ctr +=1 
            lst.append(word)
    print("List of words having same last and first word", lst)

    
count = matching_words(['aba','xyz','pop','edr','fdr'])
print("Words  having same first and last letter", count)

#sum and average

L = [4,6,2,4,5,7,36,]
countt = 0 
for i in L:
    
    countt = countt + i

    ave = countt/len(L)

print("The sum is " , countt)
print("The average is " , ave)

L.sort
print("The smallest one" , L[0])
print("The biggest one" , L[-1])