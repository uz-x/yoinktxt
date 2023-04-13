class Yoinktxt:
	# def __init__(self, file, spl="==", line="\n"):
	# 	f = open(file, "r") # File open
	# 	fr = f.read() # Text in file
	# 	fs = fr.split(line) # Split text in file
	# 	for i in range(len(fs)):
	# 		fs[i] = fs[i].split(spl)
	
	# 	fd = {} # Dictionary of file

	# 	for i in range(len(fs)):
	# 		for j in range(2):
	# 			fd[fs[i][0]] = fs[i][j]

	# 	self.f = f
	# 	self.fr = fr
	# 	self.fs = fs
	# 	self.fd = fd

	def __init__(self):
		self.f = 0
		self.fr = 0
		self.fs = 0
		self.fd = 0
		self.fw = 0

	def data_file(self, file):
		self.f = open(file, "r") # File open
		self.fr = (self.f).read() # Text in file

	def data_line(self, line):
		self.fs = (self.fr).split(line) # Split text in file

	def data_spl(self, spl):
		self.fd = {}

		for i in range(len(self.fs)):
			self.fs[i] = (self.fs[i]).split(spl)

		for i in range(len(self.fs)):
			for j in range(2):
				self.fd[self.fs[i][0]] = self.fs[i][j]

	def yoink_text(self):
		return self.fr

	def yoink_list(self):
		return self.fs

	def yoink_dict(self):
		return self.fd

	def yoink(self, name):
		return self.fd[name]

	def edit_value(self, val, new):
		self.fd[val] = new

	def delete_value(self, val):
		(self.fd).pop(val)