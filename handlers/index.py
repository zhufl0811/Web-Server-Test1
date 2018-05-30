#coding = utf-8
import tornado.web
from methods import db
from imp import reload

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html',name=None,price_min=None,price_max=None,rank=None, data=[])

    def post(self):
        name_like = self.get_argument('name')
        price_min = self.get_argument('price_min')
        price_max = self.get_argument('price_max')
        rank = self.get_argument('rank')
        data=db.query(name_like,price_min,price_max,rank)
        reload(db)
        self.render('index.html',name=name_like,price_min=price_min,price_max=price_max,rank=rank,data=data)