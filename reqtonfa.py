class reqtonfa():

	def __init__(self):
		self.states=0

	def checkformat(self,y):
		if (y<48 or y>57) and (y<97 or y>122) and (y<65 or y>90):
			return False
		return True

	def get_pre(self,ch):
		if ch in ['+']:
			return 1
		if ch in ['*']:
			return 2
		if ch in ['.']:
			return 3
		if ch in ['(']:
			return 4

	def shunt(self,x):
		self.stack=[]
		self.outstring=""
		for i in x:
			ch=i
			if self.checkformat(ord(ch)):
				self.outstring=self.outstring+ch
			elif ch == '(':
				self.stack.insert(len(self.stack),ch)
			elif ch == ')':
				while len(self.stack)>0 and self.stack[len(self.stack)-1]!='(':
					self.outstring=self.outstring+self.stack[len(self.stack)-1]
					self.stack.pop(len(self.stack)-1)
				self.stack.pop(len(self.stack)-1)
			else:
				while len(self.stack)>0 and self.get_pre(ch)>=self.get_pre(self.stack[len(self.stack)-1]):
					self.outstring=self.outstring+self.stack[len(self.stack)-1]
					self.stack.pop(len(self.stack)-1)
				self.stack.insert(len(self.stack),ch)
		while len(self.stack)>0:
			self.outstring=self.outstring+self.stack[len(self.stack)-1]
			self.stack.pop(len(self.stack)-1)
		return self.outstring

	def pars_str(self,x):
		self.res=[]
		for i in range(len(x)-1):
			self.res.insert(len(self.res),x[i])
			if self.checkformat(ord(x[i])) and self.checkformat(ord(x[i+1])):
				self.res.insert(len(self.res),'.')
			elif x[i]==')' and x[i+1] == '(':
				self.res.insert(len(self.res),'.')
			elif self.checkformat(ord(x[i+1])) and x[i]==')':
				self.res.insert(len(self.res),'.')
			elif x[i+1]=='(' and self.checkformat(ord(x[i])):
				self.res.insert(len(self.res),'.')
			elif x[i] == '*' and (self.checkformat(ord(x[i+1]) or x[i+1] == '(')):
				self.res.insert(len(self.res),'.')
		check = x[len(x)-1]
		if( check != self.res[len(self.res)-1]):
			self.res += check
		return ''.join(self.res)

	def NFA_sym(self,ch):
		self.letters
		self.letters.update(set({ch}))
		self.states
		val = ["Q{}".format(self.states),ch,"Q{}".format(self.states+1)]
		self.nfa["transition_function"].insert(len(self.nfa["transition_function"]),val)
		self.states=self.states+2
		ret = list(["Q{}".format(self.states-2),"Q{}".format(self.states-1)])
		return ret

	def nfa_unio(self,nfa1,nfa2):
		self.states
		val = ["Q{}".format(self.states),'$',nfa1[0]]
		self.nfa["transition_function"].insert(len(self.nfa["transition_function"]),val)
		val = ["Q{}".format(self.states),'$',nfa2[0]]
		self.nfa["transition_function"].insert(len(self.nfa["transition_function"]),val)
		val = [nfa1[1],'$',"Q{}".format(self.states+1)]
		self.nfa["transition_function"].insert(len(self.nfa["transition_function"]),val)
		val = [nfa2[1],'$',"Q{}".format(self.states+1)]
		self.nfa["transition_function"].insert(len(self.nfa["transition_function"]),val)
		self.states=self.states+2
		return ["Q{}".format(self.states-2),"Q{}".format(self.states-1)]

	def loop(self,nfa1):
		self.states
		val = [nfa1[1],'$',nfa1[0]]
		self.nfa["transition_function"].insert(len(self.nfa["transition_function"]),val)
		val = ["Q{}".format(self.states),'$',nfa1[0]]
		self.nfa["transition_function"].insert(len(self.nfa["transition_function"]),val)
		val = [nfa1[1],'$',"Q{}".format(self.states+1)]
		self.nfa["transition_function"].insert(len(self.nfa["transition_function"]),val)
		val = ["Q{}".format(self.states),'$',"Q{}".format(self.states+1)]
		self.nfa["transition_function"].insert(len(self.nfa["transition_function"]),val)
		self.states=self.states+2
		return ["Q{}".format(self.states-2),"Q{}".format(self.states-1)]

	def concatenation(self,nfa1,nfa2):
		self.states
		indx = len(self.nfa['transition_function'])
		val = [nfa1[1],'$',nfa2[0]]
		self.nfa['transition_function'].insert(indx,val)
		return [nfa1[0],nfa2[1]]	

	def re2nfa(self,x):
		self.stack=list([])
		xt=""
		for i in x:
			if self.checkformat(ord(i)):
				self.stack.insert(len(self.stack),self.NFA_sym(i))
			elif i == '+':
				xt=self.nfa_unio(self.stack[len(self.stack)-2],self.stack[len(self.stack)-1])
				self.stack.pop(len(self.stack)-1)
				self.stack.pop(len(self.stack)-1)
				self.stack.insert(len(self.stack),xt)
			elif i == "*":
				xt=self.loop(self.stack[len(self.stack)-1])
				self.stack.pop(len(self.stack)-1)
				self.stack.insert(len(self.stack),xt)
			else:
				xt=self.concatenation(self.stack[len(self.stack)-2],self.stack[len(self.stack)-1])
				self.stack.pop(len(self.stack)-1)
				self.stack.pop(len(self.stack)-1)
				self.stack.insert(len(self.stack),xt)
		# nfa["start_self.states"]=[xt[0]]
		self.nfa["initial_state"]=[xt[0]]
		self.nfa["final_self.states"]=[xt[1]]



	def getresult(self,x):

		self.letters=set({})

		self.nfa={}
		self.nfa["self.states"]=[]
		self.nfa["letters"]=[]
		self.nfa["transition_function"]=[]
		x=self.pars_str(x)
		x=self.shunt(x)
		self.re2nfa(x)

		s=set({})
		for x in range(len(self.nfa["transition_function"])):
			s.update(set({self.nfa["transition_function"][x][0]}))
			s.update(set({self.nfa["transition_function"][x][2]}))

		templis = list(self.letters)
		self.nfa["letters"]=templis
		s=list(s)
		s.sort(key=lambda a:int(a[1:]))
		self.nfa["self.states"]=s

		self.resulttonfa=""
		# print(self.nfa['transition_function'])
		for i in range(len(self.nfa['transition_function'])):
			x=self.nfa['transition_function'][i]
			self.resulttonfa += str(x) + "\n"
		tempstart = self.nfa["initial_state"]
		tempend = self.nfa["final_self.states"]
		self.resulttonfa +='Start State: '+ str(tempstart)+ "\n"+"End State: "+ str(tempend)

		return self.resulttonfa

# if __name__ == "__main__":
# 	x = reqtonfa()
# 	x.getresult('a+b')