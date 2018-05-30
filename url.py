#coding = utf-8
from handlers.index import IndexHandler
from handlers.add import AddHandler
from handlers.edit import EditHandler
from handlers.delete import DeleteHandler
url = [(r'/',IndexHandler),
       (r'/add',AddHandler),
       (r'/edit',EditHandler),
       (r'/delete',DeleteHandler)
]