import tornado.web
from methods import db
from imp import reload

class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('add.html')
    def post(self):
        name = self.get_argument('name')
        price = self.get_argument('price')
        rank = self.get_argument('rank')
        db.add(name,price,rank)
        reload(db)
        self.render('add_successful.html')