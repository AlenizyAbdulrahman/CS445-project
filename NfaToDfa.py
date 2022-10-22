class nfatodfa():


    def __init__(self) -> None:
        pass


    def result(self,x,final):
        dic = {}
        ls = list()
        char=''
        for i in range(len(x)):
            if x[i] == "[":
                char += x[i+1]
                dic[x[i+1]]={}
                
        for i in range(len(x)):
            try:
                if x[i] == "[" and x[i+6]!= ']':
                    dic[x[i+1]][x[i+3]]= [x[i+5],x[i+6]]
                elif x[i] == "[":
                        dic[x[i+1]][x[i+3]]= [x[i+5]]
            except IndexError:
                if x[i] == "[":
                        dic[x[i+1]][x[i+3]]= [x[i+5]]

        for i in dic[final]:
            dic[final][i]=[]

        nfa = dic                         

        t = 2  

        nfa_final_state = final                       
            
        new_states_list = []                          
        dfa = {}                                      
        keys_list = list(list(nfa.keys())[0])                  
        path_list = list(nfa[keys_list[0]].keys())    



        dfa[keys_list[0]] = {}                        
        for y in range(t):
            var = "".join(nfa[keys_list[0]][path_list[y]])   
            dfa[keys_list[0]][path_list[y]] = var            
            if var not in keys_list:                        
                new_states_list.append(var)                  
                keys_list.append(var)                        
                


        while len(new_states_list) != 0:                     
            dfa[new_states_list[0]] = {}                     
            for _ in range(len(new_states_list[0])):
                for i in range(len(path_list)):
                    temp = []                               
                    for j in range(len(new_states_list[0])):
                        temp += nfa[new_states_list[0][j]][path_list[i]]  
                    s = ""
                    s = s.join(temp)                        
                    if s not in keys_list:                  
                        new_states_list.append(s)            
                        keys_list.append(s)                  
                    dfa[new_states_list[0]][path_list[i]] = s   
                
            new_states_list.remove(new_states_list[0])      


        dfa_states_list = list(dfa.keys())
        dfa_final_states = []
        for x in dfa_states_list:
            for i in x:
                if i in nfa_final_state:
                    dfa_final_states.append(x)
                    break
        ll=""
        for i in dfa :
            ll+=i+" "+str(dfa[i])+'\n'
        ll+="Final states of the DFA are : " + str(dfa_final_states)
        return ll



# if __name__=="__main__":
#     s = nfatodfa()
#     x = s.result("[A,a,AB],[A,b,A],[B,a,C],[B,b,C],[C,a,D],[C,b,D],[D,a,],[D,b,]","D")
#     print(x)