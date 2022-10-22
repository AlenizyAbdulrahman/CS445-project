










# dic = {}
# x = '[A,a,AB],[A,b,A],[B,a,C],[B,b,C],[C,a,D],[C,b,D],[D,a,],[D,b,]'
# ls = list()
# char=''
# for i in range(len(x)):
#     if x[i] == "[":
#         char += x[i+1]
#         dic[x[i+1]]={}
        
# for i in range(len(x)):
#     try:
#         if x[i] == "[" and x[i+6]!= ']':
#             dic[x[i+1]][x[i+3]]= [x[i+5],x[i+6]]
#         elif x[i] == "[":
#                 dic[x[i+1]][x[i+3]]= [x[i+5]]
#     except IndexError:
#         if x[i] == "[":
#                 dic[x[i+1]][x[i+3]]= [x[i+5]]

# for i in dic["D"]:
#     dic["D"][i]=[]

# char = "".join(dict.fromkeys(char))



# nfa = {'A': {'a': ['A', 'B'], 'b': ['A']},

#  'B': {'a': ['C'], 'b': ['C']},
 
#   'C': {'a': ['D'], 'b': ['D']},
  
#    'D': {'a': [], 'b': []}} 
ll = ''

dic = {'A': {'a': 'AB', 'b': 'A'}, 'AB': {'a': 'ABC', 'b': 'AC'}, 'ABC': {'a': 'ABCD', 'b': 'ACD'}, 'AC': {'a': 'ABD', 'b': 'AD'}, 'ABCD': {'a': 'ABCD', 'b': 'ACD'}, 'ACD': {'a': 'ABD', 'b': 'AD'}, 'ABD': {'a': 'ABC', 'b': 'AC'}, 'AD': {'a': 'AB', 'b': 'A'}}

for i in dic :
    ll+=i+" "+str(dic[i])+'\n'


