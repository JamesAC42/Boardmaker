class makeBoard(object):
	def __init__(self,rows,columns):
		hold = []
		for i in range(rows):
			hold.append([" "]*columns)
		self.board = hold
		self.rows = rows
		self.columns = columns
		self.maxlength = 5
		self.maxentry = 1
		self.entryLengths = [1]
		self.methods = { "getList": "Returns the gameboard 2D List.",
					"printBoard": "Prints out a formatted board container entries.",
					"changeIndex": "Edit the value of specific location: .changeIndex(x,y, change)",
					"printIndex": "Prints the value of specific location: .printIndex(x,y)",
					"getIndex": "Returns the value of specific location.",
					"changeMaxLength": "Edit the maximum length of each subdivision. (For Formatting printBoard method)",
					"helpAll": "List all methods contained in makeBoard class.",
					"helpMethod": "Print function of specific method within makeBoard class: .helpMethod(method)"}
	def getList(self):
		return(self.board)
		
	def printBoard(self):
		columns = self.columns
		rows = self.rows
		maxlength = self.maxlength
		hold = self.board
		
		def linetop():
			for space in range(columns-1):
				print(" "+"_"*maxlength+" ",end=""),
			print(" "+"_"*maxlength)
			for space in range(columns-1):
				print("|" + " "*maxlength + "|",end=""),
			print("|" + " "*maxlength + "|")
			
		def linebottom():
			for space in range(columns-1):
				print("|" + "_"*maxlength + "|",end=""),
			print("|" + "_"*maxlength + "|")
				
		print("")
		linetop()
		
		for row in range(0,len(hold)):
			for space in range(0,len(hold[row])):
				if (space+1) % columns == 0:
					print("|  {}  |".format(hold[row][space]))
					if (row+1) == rows:
						linebottom()
						continue
					else:
						linebottom()
						linetop()
				else:
					print("|  {}  |".format(hold[row][space]),end="")
		print("")
		
	def printIndex(self,x,y):
		hold = self.board
		re = hold[x][y]
		place = ""
		for i in range(len(re)):
			if re[i] == " ":
				re[i] = ""
		print("Index[{0}][{1}]: {2}".format(x,y,re))
	def getIndex(self, x,y):
		hold = self.board
		re = hold[x][y]
		for i in range(len(re)):
			if re[i] == " ":
				re[i] = ""
		return(re)
	def changeIndex(self,x,y,change):
		hold = self.board
		hold[x][y] = change
		if len(change) > self.maxentry:
			place = len(change) - self.maxentry
			self.maxentry = len(change)
			self.maxlength = 4+self.maxentry
			for row in range(0,len(hold)):
				for col in range(0,len(hold[row])):
					if x == row and y == col:
						continue
					else:
						hold[row][col] += ' '*place
		self.board = hold
		print("Index[{0}][{1}] changed to ..{2}..".format(x,y,change))
		
	def changeMaxLength(self):
		while True:
			length = input("$: ")
			try:
				length = int(length)
				break
			except ValueError:
				print("Length entry must be type (Int)")
				
		self.maxlength = length
		print("Max Length changed to ..{}..".format(length))
	def helpAll(self):
		methods = self.methods
		print("")
		for method in methods:
			print("{}: {}".format(method,methods[method]))
			print("")
	def helpMethod(self, specific):
		methods = self.methods
		print("")
		for method in methods:
			if method == specific:
				print("{}: {}".format(method,methods[method]))
				break
			else:
				continue
		else:
			print("Method not found")
		print("")
		
		
		
		
		
		
		
		
		
		
		