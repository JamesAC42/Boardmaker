class makeBoard(object):
	def __init__(self,rows,columns):
		hold = []
		for i in range(rows):
			hold.append([""]*columns)
		self.board = hold
		self.rows = rows
		self.columns = columns
		self.maxentry = 0
		self.append = 2
		self.methods = { "getList": "Returns the 2D List.",
					"importList": "Import a custom 2D list instead of using constructer.",
					"printBoard": "Prints out a formatted board containing entries.",
					"changeIndex": "Edit the value of specific location: .changeIndex([x,y], change)",
					"printIndex": "Prints the value of specific location: .printIndex([x,y])",
					"getIndex": "Returns the value of specific location: .getIndex([x,y])",
					"clearBoard": "Clears the entire board",
					"helpAll": "List all methods contained in makeBoard class.",
					"helpMethod": "Print function of specific method within makeBoard class: .helpMethod(method)"}
					
	def getList(self):
		return(self.board)
	def importList(self,new_list):
		if isinstance(new_list, list):
			pass
		else:
			print("Argument must be 2 dimensional list")
			return
		for row in new_list:
			if isinstance(row,list):
				continue
			else:
				print("Argument must be a 2 dimensional list")
				return
		check = len(new_list[0])
		for row in new_list:
			if len(row) != check:
				print("Argument must not be jagged")
				return
			else:
				continue
		self.rows = len(new_list)
		self.columns = len(new_list[0])
		self.append = 2
		self.board = new_list
	def printBoard(self):
		columns = self.columns
		rows = self.rows
		hold = self.board
		
		maxlength = 0
		for row in range(0,len(hold)):
			for space in range(0, len(hold[row])):
				current_length = len(str(hold[row][space]))
				if current_length > maxlength:
					maxlength = current_length
				else:
					continue
					
		maxlength = maxlength + 4
		
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
					append = maxlength - len(str(hold[row][space]))
					if append % 2 == 0:
						append1 = int(append/2)
						append2 = int(append/2)
					else:
						convert = append+1
						append1 = int((convert/2)-1)
						append2 = int(convert/2)
					l = (("|") + (" "*append1) + ("{}".format(hold[row][space])) + (" "*append2) + ("|"))
					print(l)
					if (row+1) == rows:
						linebottom()
						continue
					else:
						linebottom()
						linetop()
				else:
					append = maxlength - len(str(hold[row][space]))
					if append % 2 == 0:
						append1 = int(append/2)
						append2 = int(append/2)
					else:
						convert = append+1
						append1 = int((convert/2)-1)
						append2 = int(convert/2)
					l = (("|") + (" "*append1) + ("{}".format(hold[row][space])) + (" "*append2) + ("|"))
					print(l,end="")
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
	def clearBoard(self):
		hold = self.board
		for row in range(0,len(hold)):
			for space in range(0,len(hold[row])):
				hold[row][space] = ""
		self.board = hold
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
		

def toBoard(new_list):
	if isinstance(new_list, list):
		pass
	else:
		print("Argument must be 2 dimensional list")
		return
	for row in new_list:
		if isinstance(row,list):
			continue
		else:
			print("Argument must be a 2 dimensional list")
			return
	check = len(new_list[0])
	for row in new_list:
		if len(row) != check:
			print("Argument must not be jagged")
			return
		else:
			continue
	rows = len(new_list)
	columns = len(new_list[0])
	new_board = makeBoard(rows,columns)
	new_board.importList(new_list)
	return new_board
		
		
		
		
		
		
