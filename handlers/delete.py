import tornado.web
from methods import db
from imp import reload

class DeleteHandler(tornado.web.RequestHandler):
    def get(self):
        global origin_name
        origin_name = self.get_argument('name')
        data = db.edit_query(origin_name)
        reload(db)
        self.render('delete.html', data=data)
    def post(self):
        global origin_name
        deleteornot=self.get_argument('deleteornot')
        if deleteornot == '0':
            self.redirect('/')
        else:
            db.delete(origin_name)
            reload(db)
            self.render('delete_successful.html',name=origin_name)