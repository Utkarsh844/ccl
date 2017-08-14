#!usr/bin/python
import wsgiref.handlers 
from google.appengine.ext import db
from google.appengine.ext import webapp
import webapp2
import template
import os
import urllib   
   
class product(db.Model):
<<<<<<< HEAD
     productm = db.StringProperty(required=True)
     description = db.StringProperty(required=True)
     when = db.DateTimeProperty(auto_now_add=True)
class MyHandler(webapp2.RequestHandler):
   def get(self):
     products = db.GQlQuery('SELECT * FROM Product ORDER BY when DESC')
     values = {'products': products}
     self.response.out.write(template.render('main.html', values))
   def post(self):
     product = Product(productm=self.request.get('productm'), description=self.request.get( 'description'))
     product.put()
     self.redirect('/')
app = webapp2.WSGIApplication([('/', MyHandler)], debug=True)  
=======
    firstname = db.StringProperty(
	                 required=True)
when = db.DateTimeProperty(
	              auto_now_add=True)
phone = db.IntegerProperty(
	                required=True)

class MyHandler(webapp.RequestHandler):
   def get(self):
     products = db.GQlQuery(
	   'SELECT * FROM Product '
	   'ORDER BY when DESC')
values = {
	     'products': products
	   }
self.response.out.write(
	 template.render('main.html', 
	                 values))
def post(self):
     product = Product(
	   firstname=self.request.get(
	   'firstname'),
	   phone=self.request.get(
	   'phone'))
	   
product.put()
self.redirect('/')

   
   
   
def main():
    app = webapp.WSGIApplication([
  (r'.*',MyHandler)], debug=True)
wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
    main()   
>>>>>>> origin/master
