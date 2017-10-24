
vowels=['a','e','i','o','u','A','E','I','O','U']
class sentence: 
	name = " " 
	def __init__(self,name):
		self.name = name
				
	def rev(self): 
		r=self.name.split();
		r=r[::-1]
		print "Reversed String: ",
		for i in r:
			print i,

	def countv(self):
		s=self.name
		c=0
		i=0
		while i<len(s):
			if s[i] in vowels:
				c=c+1
			i=i+1
		return c


inp=raw_input("Enter First Sentence: ")
s1=sentence(inp)
inp=raw_input("Enter Second Sentence: ")
s2=sentence(inp)
inp=raw_input("Enter Third Sentence: ")
s3=sentence(inp)

s=[s1,s2,s3]
s.sort(key=lambda x:x.countv(),reverse=True)
print "\nDisplaying Reverse of Sentence in Descending order of no. of Vowels:-"
for j in s:
	j.rev()
	print "\nNo. of Vowels=%d\n"%j.countv()
	
