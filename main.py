#!usr/bin/python
import webapp2
from google.appengine.ext import ndb
   
   
html = """ 
             <html>
            <body>
			<h1>Enter Product Description</h1>
            <form action = "/confirm" method = "POST">
	     
 Product:<input type = "text" name = "productm" id="productm" />
 <br>
 Description:<textarea rows="4" cols="50" id="description" name="description"></textarea>
<input type = "submit"  value ="Save">
</form>
    <h1>Search Product</h1>
	        <form action="/search" method="POST">
Product:<input type="text" name="productm">
<br>
<input type="submit" value="Search">
</form>
            </body>
            </html>   
 """  
   
   
class Product(ndb.Model):
     producte = ndb.StringProperty(indexed=True)
     descriptions = ndb.TextProperty(indexed=True)
     when = ndb.DateTimeProperty(auto_now_add=True)
	 
	 
	 
class MyHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html)
		
		
		
		
class MainHandler(webapp2.RequestHandler):
   def post(self):
     product = self.request.get('productm')
     description = self.request.get('description')
     products = Product()
     products.producte=product
     products.descriptions=description
     products.put()
     self.response.out.write('Details enetered into the datastore are')

class MainHandlers(webapp2.RequestHandler):
     def post(self):
        product = self.request.get('productm')
        products = Product.query()
        searchquery = products.filter(Product.producte==product)
        for i in searchquery:
            self.response.out.write('<b>The product name is %s</b>' % i.producte)
	 
app = webapp2.WSGIApplication([('/', MyHandler),('/confirm', MainHandler),('/search', MainHandlers)], 
 debug=True)