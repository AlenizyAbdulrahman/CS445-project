class State:


    def __init__(self, alphabet, id_list, id, terminal_id):

        self.id_set = set(id_list)
        self.id = id
        self.transitions = dict()  # Dictionary to keep all the transitions to other states
        self.final = terminal_id in self.id_set  # True if this is a final state
        for a in alphabet:
            self.transitions[a] = {}  # Each transitions from this state by a char is stored in a set


class DFA:

    def __init__(self, alphabet, tree):

        self.states = []  # All the states in DFA containing State instances
        self.alphabet = alphabet
        self.id_counter = 1
        self.terminal = tree.id_counter - 1  # '#' leaf is the end of regex and the id of it is assigned to terminal
        self.compute_states(tree)  # constructs the DFA based on syntax tree

    def compute_states(self, t):

        D1 = State(self.alphabet, t.root.firstpos, self.give_next_id(), self.terminal)
        self.states.append(D1)
        queue = [D1]
        while len(queue) > 0:  # Finds the transitions to all states
            st = queue.pop(0)
            new_states = self.Dtran(st, t)
            for s in new_states:
                state = State(self.alphabet, s, self.give_next_id(), self.terminal)
                self.states.append(state)
                queue.append(state)
                
        return

    def Dtran(self, state, tree):

        new_states = []
        for i in state.id_set:
            if i == self.terminal:
                continue
            label = tree.leaves[i]
            if state.transitions[label] == {}:
                state.transitions[label] = tree.followpos[i]
            else:
                state.transitions[label] = state.transitions[label].union(tree.followpos[i])
        for a in self.alphabet:
            if state.transitions[a] != {}:
                new = True
                for s in self.states:
                    if s.id_set == state.transitions[a] or state.transitions[a] in new_states:
                        new = False
                if new:
                    new_states.append(state.transitions[a])
        return new_states

    def post_processing(self):

        has_none_state = False
        for state in self.states:
            for a in self.alphabet:
                if state.transitions[a] == {}:
                    has_none_state = True
                    state.transitions[a] = self.id_counter
                SET = state.transitions[a]
                for state2 in self.states:
                    if state2.id_set == SET:
                        state.transitions[a] = state2.id
        if has_none_state:
            self.states.append(State(self.alphabet, [], self.id_counter, self.terminal))
            for a in self.alphabet:
                self.states[-1].transitions[a] = self.states[-1].id

    def give_next_id(self):

        id = self.id_counter
        self.id_counter += 1
        return id

    def __str__(self):

        self.post_processing()
        s = ''

        # for state in self.states:
        #     if state.id == 1:
        #         s = s+'->\t'
        #     else:
        #         s = s+'\t'
        #     s= s+str(state.id)+' \t'
        #     for a in self.alphabet:
        #         s=s+str(a)+' : '+str(state.transitions[a])+' \t'
        #     if state.final:
        #         s=s+"Final State"
        #     s+='\n'
        # return s
        for a in self.alphabet:
            s=s+' \t'+str(a)
        s=s+'\n'
        for state in self.states:
            s= s+str(state.id)+' \t'
            for a in self.alphabet:
                s=s+str(state.transitions[a])+' \t'
            if state.final:
                s=s+"Final State "
            if state.id == 1:
               s = s+"Start State"
            s+='\n'
        return s


    def __repr__(self):
        return self.__str__()




class Node:

    def __init__(self, type, label, id=None, left_child=None, right_child=None):

        self.id = id  # Each non empty-char tree leaf should have an integer id
        self.type = type
        self.left_child = left_child
        self.right_child = right_child
        self.label = label
        self.nullable = False  # True if we can derive empty-char from this node
        self.firstpos = set()  # firstpos of node (refer to documentation.md for detail).
        self.lastpos = set()  # followpos of node (refer to documentation.md for detail).

    def __str__(self):
        '''Printing string'''
        childrenCount = int(self.right_child != None) + int(self.left_child != None)
        return '''Type\t\t:\t{0}
Label\t\t:\t{1}
Children\t:\t{2}
Nullable\t:\t{3}
Firstpos\t:\t{4}
Lastpos\t\t:\t{5}'''.format(self.type, self.label, childrenCount, self.nullable, self.firstpos, self.lastpos)

    def __repr__(self):
        '''In console string'''
        childrenCount = int(self.right_child != None) + int(self.left_child != None)
        s = "<" + "'{0}'".format(self.type) + ' Node with label ' + "'{0}'".format(self.label) + ' and ' + str(
            childrenCount) + [' child', ' children'][childrenCount != 1] + '>'
        return s

    def print_subtree(self, level=0, linelist=[], rightchild=False, instar=False):

        star = self.type == 'star'
        N = '\n'
        T = '\t'
        L = '|'
        if level == 0:
            ret = self.label + '\n'
        else:
            s = ''
            if not instar:
                for k in range(2):
                    for i in range(level):
                        if i in linelist:
                            s += T*(i!=0) + L
                        else:
                            s += T
                    if k == 0:
                        s += N

            ret = s + '___' + self.label + N * (not star)
        if rightchild:
            linelist.pop(-1)
        if self.left_child:
            ret += self.left_child.print_subtree(level + 1, linelist + [level] * (not star),
                                                 instar=star)
        if self.right_child:
            ret += self.right_child.print_subtree(level + 1, linelist + [level], rightchild=True)
        return ret


class Tree:

    def __init__(self, post):

        self.root = Node('con', '.')  # Root is always concatenation of the regex with '#' mark.
        self.leaves = dict()  # Keeping track of the labels of the leaves for convenience
        self.id_counter = 1  # This variable is used to assign id to leaves.
        # 1. Creating tree:
        self.create_tree(post)
        # 2. Finding the followpos of the tree and Nullable,Firstpos and Lastpos for each node:
        self.followpos = [set() for i in range(self.id_counter)]
        self.postorder_nullable_firstpos_lastpos_followpos(self.root)

    def create_tree(self, post):

        stack = []
        for token in post:
            if token == '.':
                left = stack.pop()
                right = stack.pop()
                temp = Node('con', token, left_child=left, right_child=right)
                stack.append(temp)
            elif token == '+':
                left = stack.pop()
                right = stack.pop()
                temp = Node('or', token, left_child=left, right_child=right)
                stack.append(temp)
            elif token == '*':
                left = stack.pop()  # Star node has only one child.
                temp = Node('star', token, left_child=left)
                stack.append(temp)
            else:  # identifier
                temp = Node('identifier', token, id=self.give_next_id())
                self.leaves[temp.id] = temp.label
                stack.append(temp)

        temp = Node('identifier', '#', id=self.give_next_id())
        self.leaves[temp.id] = temp.label
        self.root.left_child = stack.pop()
        self.root.right_child = temp
        return

    def give_next_id(self):

        id = self.id_counter
        self.id_counter += 1
        return id

    def postorder_nullable_firstpos_lastpos_followpos(self, node):

        if not node:  # Recursion terminator
            return
        # 1. Left
        self.postorder_nullable_firstpos_lastpos_followpos(node.left_child)
        # 2. Right
        self.postorder_nullable_firstpos_lastpos_followpos(node.right_child)
        # 3. Root
        if node.type == 'identifier':
            if node.label == '@':  # empty char
                node.nullable = True
            else:
                node.firstpos.add(node.id)
                node.lastpos.add(node.id)
        elif node.type == 'or':
            node.nullable = node.left_child.nullable or node.right_child.nullable
            node.firstpos = node.left_child.firstpos.union(node.right_child.firstpos)
            node.lastpos = node.left_child.lastpos.union(node.right_child.lastpos)
        elif node.type == 'star':
            node.nullable = True
            node.firstpos = node.left_child.firstpos
            node.lastpos = node.left_child.lastpos
            self.compute_follows(node)  # Follows is only computed for star and cat nodes
        elif node.type == 'con':
            node.nullable = node.left_child.nullable and node.right_child.nullable
            if node.left_child.nullable:
                node.firstpos = node.left_child.firstpos.union(node.right_child.firstpos)
            else:
                node.firstpos = node.left_child.firstpos
            if node.right_child.nullable:
                node.lastpos = node.left_child.lastpos.union(node.right_child.lastpos)
            else:
                node.lastpos = node.right_child.lastpos
            self.compute_follows(node)  # Follows is only computed for star and cat nodes
        return

    def compute_follows(self, n):

        if n.type == 'con':
            for i in n.left_child.lastpos:
                self.followpos[i] = self.followpos[i].union(n.right_child.firstpos)
        elif n.type == 'star':
            for i in n.left_child.lastpos:
                self.followpos[i] = self.followpos[i].union(n.left_child.firstpos)

    def __str__(self):
        '''Printing string'''
        return self.root.print_subtree()
    def __repr__(self):
        '''In console string'''
        return self.root.print_subtree()


def create_token_queue(INPUT):

    tokens = []
    id = ''
    for c in INPUT:
        if c in ['(', ')', '.', '*', '+']:
            if id != '':
                tokens.append(id)
                id = ''
            tokens.append(c)
        else:
            id = id + c
    if id != '':
        tokens.append(id)
    return tokens


def create_postfix_token_queue(tokens):

    output_queue = []
    stack = []
    for token in tokens:
        if token == '(':
            stack.append('(')
        elif token == ')':
            while (len(stack) > 0 and stack[-1] != '('):
                output_queue.append(stack.pop())
            stack.pop()
        elif token == '*':
            stack.append(token)
        elif token == '.':
            while len(stack) > 0 and stack[-1] == '*':
                output_queue.append(stack.pop())
            stack.append(token)
        elif token == '+':
            while len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '.'):
                output_queue.append(stack.pop())
            stack.append(token)
        else:
            output_queue.append(token)
    while (len(stack) > 0):
        output_queue.append(stack.pop())
    return output_queue


def read_input(path):

    alph = []
    file = open(path)
    lines = file.readlines()
    file.close()
    for i in range(int(lines[0])):
        alph.append(lines[1 + i].strip())
    return alph, lines[int(lines[0]) + 1].strip()



    
def getresult(x):

        a=''
        withline = ""
        for i in x :  
            if i.isalpha():
                a+=i
        reqchar =  "".join(dict.fromkeys(a))
        lenreqchar = len(reqchar)
        for i in reqchar:
            if i == reqchar[-1]:
                withline+=i
            else:
                withline+=i+"\n"
        str1 = ""


        lst = list()
        for i in x :
            if i == "." or i == "+":
                lst.append(i)



        a = x.replace("."," ")
        z = a.replace("+"," ")

        lst2 = z.split(" ")
        lst2.reverse()

        lst.reverse()
        last = ""

        for i in lst2:
            for j in lst:
                last = last+ i + j
                lst.remove(j)

        last = last + lst2[len(lst2) - 1]

        # print(last)

        lstxx = list()
        xx=""
        for i in last :
            lstxx.append(i)

        for i in range(len(lstxx)):
            if lstxx[i] == "(":
                lstxx[i]=")"
                i+=1
            if lstxx[i] == ")":
                lstxx[i]="("
            
        for i in lstxx:
            xx+=i

        lsttobe = list(xx)
        # print(lsttobe)
        hh = ""
        istrue = False
        for i in range (len(lsttobe)-1):
            if lsttobe[i] == "(" and lsttobe[i+1] == "*":
                del lsttobe[i+1]
                istrue = True
                curr = lsttobe[i-1]
                lsttobe[i-1] = lsttobe[i]
                lsttobe[i] = curr
            if lsttobe[i] == "(":
                curr = lsttobe[i-1]
                lsttobe[i-1] = lsttobe[i]
                lsttobe[i] = curr
            if lsttobe[i] == ")":
                if istrue == True:
                    curr = lsttobe[i+1]
                    lsttobe[i+1] = str(lsttobe[i]+"*")
                    lsttobe[i] = curr
                else:
                    curr = lsttobe[i+1]
                    lsttobe[i+1] = lsttobe[i]
                    lsttobe[i] = curr
                
        lasttext = ""
        for i in lsttobe:
            lasttext+=i

        file_object = open('sample.txt', 'a')
        file_object.truncate(0)
        file_object.write(f'{lenreqchar}\n{withline}\n{lasttext}')
        file_object.close()    

        # 1. Reading the input
        ALPH, INPUT = read_input("sample.txt")
        # 2. Getting the tokens
        tokens = create_token_queue(INPUT)
        # print(tokens)
        # 3. Converting the tokens to post-order format
        post = create_postfix_token_queue(tokens)
        # print("post",post)
        # 4. Creating the tree
        t = Tree(post)
        # 5. Creating the DFA
        d = DFA(ALPH, t)
        # 6. Printing the results
        # print(INPUT)
        # print(t)
        return d


# x = "a*bc123"
# a = ""
# for i in x:
#     if i.isalpha():
#         a += i
# print(len(a))
# print(a)
# # Open a file with access mode 'a'
# file_object = open('sample.txt', 'a')
# file_object.truncate(0)
# # Append 'hello' at the end of file
# file_object.write(f'3\na\nd\nc\nadc')
# # Close the file
# file_object.close()
