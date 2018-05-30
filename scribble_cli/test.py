'''from login import Login

s = Login()
s.get_cred()
print (s.login())
'''
'''
from note import Note

s = Note()
s.set_params("tetsing title3", "testing body3", "", "")
print (s.save_note())
'''

'''
from view_all import View_all
s = View_all()
s.set_params()
print (s.view_all())
'''

'''
from view_by_id import View_by_id
s = View_by_id()
s.set_params(5)
print (s.view_by_id())
'''

'''
from search import Search
s = Search()
s.set_params("testing")
print (s.search())
'''

from delete import Delete
s = Delete()
s.set_params(100)
print (s.delete())



