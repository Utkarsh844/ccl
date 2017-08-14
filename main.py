#!usr/bin/python
import wsgiref.handlers 
from google.appengine.ext import db
from google.appengine.ext import webapp
import template
import os
import urllib   
   
class product(db.Model):
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
