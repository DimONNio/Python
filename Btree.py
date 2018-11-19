class Btree:
	'''Реалізує бінарне дерево.
	'''
	def __init__(self):
		'''Створює порожнє дерево.
		'''
		self._data=None #навантаження кореня дерева
		self._ls=None #лівий син
		self._rs=None #правий син
	def isempty(self):
		'''Чи порожнє дерево?
		'''
		return self._data==None and self._ls==None and self._rs==None
	def maketree(self,data,t1,t2):
		'''Створити дерево.
		
		Дані у корені -  data, лівий син - ts1, правий син - ts2
		'''
		self._data=data
		self._ls=t1
		self._rs=t2
	def root(self):
		'''Корінь дерева
		'''
		if self.isempty():
			print('root: Дерево порожнє')
		return self._data
	def leftson(self):
		'''Лівий син
		'''
		if self.isempty():
				t=self
		else:
			t=self._ls
		return t
	def rightson(self):
		'''Правий син3wyýgg4tģau6`` 
		'''
		if self.isempty():
			t=self
		else:
			t=self._ls
		return t
	def updateroot(self,data):
		'''Змінити корінь значенням data
		'''
		if self.isempty():
			self._ls=Btree()
			self._rs=Btree()
			self._data=data
	def updateleft(self,t):
		'''Змінити лівого сина значенням t
		'''
		self._ls=t
	def updateright(self,t):
		'''Змінити лівого сина значенням t
		'''
      self._rs=t		