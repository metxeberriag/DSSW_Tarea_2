#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import webapp2
 
class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("<html><body>")
        self.response.write("<head><script src='scripts/validator.js' type='text/javascript'></script></head>")
        # inicio de formulario
        self.response.write("<form method='POST' id='tarea2' onsubmit=return validate()>")
        # campo de texto
        self.response.write("<label>Nombre de usuario:</label> "
                            "<input name='nombre' placeholder='Nombre' required='true'> <br>")
        
        # campos de password
        self.response.write("<label>Password:</label> "
                            "<input name='password1' placeholder='Password'> <br>")
        self.response.write("<label>Repetir Password:</label> "
                            "<input name='password2' placeholder='Repetir el mismo de antes'> <br>")
        
        # campo de email
        self.response.write("<label>Email:</label> "
                            "<input name='email' placeholder='Email'> <br>")
        # botón de envio
        self.response.write("<br> <input type='submit'>")
        # final de formulario
        self.response.write("</form>")
        self.response.write("</body></html>")
 
    def post(self):
        self.response.write("<html><body>")
        self.response.write('<h1>Formulario recibido correctamente</h1>')
        self.response.write("Nombre: %s <br>" % self.request.get('nombre'))
        self.response.write("Email: %s <br>" % self.request.get('email'))
        self.response.write("<a href='/registro'><< Regresar</a>")
        self.response.write("</body></html>")

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body><head><link rel="stylesheet" href="/styles/main_eu.css"></head>')
        self.response.out.write('<p>Kaixo Mundua!</p><img src="/images/kaixo.gif" />')
        self.response.out.write('</body></html>')

class EsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body><head><link rel="stylesheet" href="/styles/main_es.css"></head>')
        self.response.out.write('<p>Hola Mundo!</p><img src="/images/kaixo.gif" />')
        self.response.out.write('</body></html>')

class EnHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body><head><link rel="stylesheet" href="/styles/main_en.css"></head>')
        self.response.out.write('<p>Hello World!</p><img src="/images/kaixo.gif" />')
        self.response.out.write('</body></html>')
 
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/es', EsHandler),
    ('/en', EnHandler),
    ('/registro', RegisterHandler),
], debug=True)

		