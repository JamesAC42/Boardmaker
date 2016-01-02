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
		self.append = 2
		self.entryLengths = [1]
		self.methods = { "getList": "Returns the 2D List.",
					"importList": "Import a custom 2D list instead of using constructer.",
					"printBoard": "Prints out a formatted board containing entries.",
					"changeIndex": "Edit the value of specific location: .changeIndex([x,y], change)",
					"printIndex": "Prints the value of specific location: .printIndex([x,y])",
					"getIndex": "Returns the value of specific location.",
					"changeMaxLength": "Edit the maximum length of each subdivision. (For Formatting the printBoard method)",
					"helpAll": "List all methods contained in makeBoard class.",
					"helpMethod": "Print function of specific method within makeBoard class: .helpMethod(method)"}
	def getList(self):
		return(self.board)
	def importList(self,list):
		self.board = list
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
					append = self.append
					append = maxlength - (2 + (len(hold[row][space])))
					print("|  {}".format(hold[row][space]) + " "*append + "|")
					if (row+1) == rows:
						linebottom()
						continue
					else:
						linebottom()
						linetop()
				else:
					append = self.append
					append = maxlength - (2 + len(hold[row][space]))
					print("|  {}".format(hold[row][space]) + " "*append + "|", end="")
		print("")
		
	def printIndex(self, xylist):
		hold = self.board
		x = xylist[0]
		y = xylist[1]
		re = hold[x][y]
		print(re)
	def getIndex(self, xylist):
		hold = self.board
		x = xylist[0]
		y = xylist[1]
		re = hold[x][y]
		return(re)
	def changeIndex(self,xylist,change):
		hold = self.board
		x = xylist[0]
		y = xylist[1]
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
						self.append += place
		self.board = hold
		
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
		