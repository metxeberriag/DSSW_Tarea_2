#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import webapp2
 
class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <html>
            <head>
                <script>
                $(document)
                    .on('click','form input[type=submit]', function(e) {
                        if ($('#password1').val()==''){
                            $('#error').text('Las contraseñas no son las mismas!');
                            e.preventDefault();
                        }
                    });
                </script>
            </head>
            <body>
                <form method='POST' id='tarea2'>
                    <label>Nombre de usuario:</label>
                    <input type='text' name='nombre' id='nombre' placeholder='Nombre' required='true'> <br>
                    <label>Password:</label>
                    <input type='password' name='password1' id='password1' placeholder='Password' required='true'> <br>
                    <label>Repetir Password:</label>
                    <input type='password' name='password2' id='password2' placeholder='Repetir el mismo de antes' required='true'> <br>
                    <label>Email:</label>
                    <input type='text" name='email' id='email' placeholder='Email' required='true'> <br>
                    <br><input type='submit'>
                    <span id='error'></span>
                </form>
            </body>
        </html>''')
 
    def post(self):
        self.response.write('''
            <html>
                <body>
                    <h1>Formulario recibido correctamente</h1>'''
                    + "Hola " + self.request.get('nombre')+'''<br>'''
                    + "Tu email es " + self.request.get('email')+'''<br>
                    <a href="/registro">Volver</a>
                </body>
            </html>''')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('''
            <html>
                <body>
                    <head>
                        <link rel="stylesheet" href="/styles/main_eu.css">
                    </head>
                    <p>Kaixo Mundua!</p>
                    <img src="/images/kaixo.gif" />
                </body>
            </html>''')

class EsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('''
            <html>
                <body>
                    <head>
                        <link rel="stylesheet" href="/styles/main_es.css">
                    </head>
                    <p>Hola Mundo!</p>
                    <img src="/images/kaixo.gif" />
                </body>
            </html>''')

class EnHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('''
            <html>
                <body>
                    <head>
                        <link rel="stylesheet" href="/styles/main_en.css">
                    </head>
                    <p>Hello World!</p>
                    <img src="/images/kaixo.gif" />
                </body>
            </html>''')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/es', EsHandler),
    ('/en', EnHandler),
    ('/registro', RegisterHandler),
], debug=True)

		