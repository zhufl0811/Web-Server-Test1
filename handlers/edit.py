import tornado.web
from methods import db
from imp import reload

class EditHandler(tornado.web.RequestHandler):
    def get(self):
        global origin_name
        origin_name= self.get_argument('name')
        data = db.edit_query(origin_name)
        reload(db)
        self.render('edit.html',data=data)
    def post(self):
        global origin_name
        name = self.get_argument('name')
        price = self.get_argument('price')
        rank = self.get_argument('rank')
        db.edit(origin_name,name,price,rank)
        reload(db)
        self.render('edit_successful.html')
