# -*- coding: UTF-8 -*-

# Filename : helloworld.py
# Author by : Vance
# 
class Book:

	def __init__(self, name, author, comment, state=0):
		self.name = name
		self.author = author
		self.comment = comment
		self.state = state

# 创建一个 Book 类的子类 FictionBook

class FictionBook(Book):
	def __init__(self, name, author, comment, state=0,typye='虚构类'):
		Book.__init__(self, name, author, comment, state=0)
		self.type = type

	def __str__(self):
		status = '未借出'
		if self.state ==1:
			status = '已借出'
		return '类型：%s 名称：《%s》 作者：%s 推荐语：%s\n状态：%s'%(self.type,self.name,self.author,self.comment,status)

# book 应该和类是一个级别
book = FictionBook('囚鸟','冯内古特','我们都是受困于时代的囚鸟')
print(book)
