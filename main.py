#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import webapp2
 
class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <html>
            <head>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                <script>
                $(document).on('click', '#enviar', function(e) {
                    $('#errorEmail').text(' ');
                    $('#errorPassword').text(' ');
                    $('#errorPassword1').text(' ');
                    
                    if ($('#password1').val()!=$('#password2').val()) {
                        $('#errorPassword').text('Las contraseñas no son las mismas!');
                        e.preventDefault();
                    }
                    
                    if ($('#password1').val()=='') {
                        $('#errorPassword1').text('Hay que rellenar la contraseña!');
                        e.preventDefault();
                    }
                    
                    if ($('#password2').val()=='') {
                        $('#errorPassword').text('Hay que rellenar la contraseña!');
                        e.preventDefault();
                    }
                    
                    if (!validateEmail($('#email').val())) {
                        $('#errorEmail').text('El email está mal escrito o está sin rellenar!');
                        e.preventDefault();
                    }
                });
                
                function validateEmail(email) {
                    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
                    return regex.test(email);
                }
                </script>
            </head>
            <body>
                <form method="post" id="login">
                    <table>
                        <tr>
                            <td class="label"> Nombre de usuario </td>
                            <td> <input type="text" name="username" id="username" value="" placeholder="Tu nombre..." required="true"> </td>
                        </tr>
                        <tr>
                            <td class="label"> Password </td>
                            <td> <input type="password" name="password" id="password1" value="" placeholder="Tu contraseña..."required="true"></td>
                            <td> <span id="errorPassword1" style="color:red"></span> </td>
                        </tr>
                        <tr>
                            <td class="label">Repetir Password </td>
                            <td> <input type="password" name="password2" id="password2" value="" placeholder="El mismo de antes" required="true"> </td>
                            <td> <span id="errorPassword" style="color:red"></span> </td>
                        </tr>
                        <tr>
                            <td class="label"> Email </td>
                            <td> <input type="text" name="email" value="" id="email" placeholder="Tu email..." required="true"> </td>
                            <td> <span id="errorEmail" style="color:red"></span> </td>
                        </tr>
                    </table>
                    <input type="submit" id="enviar">
                </form>
            </body>
        </html>''')
 
    def post(self):
        self.response.write('''
            <html>
                <body>
                    <h1>Formulario recibido correctamente</h1>'''
                    + "Hola " + self.request.get('username')+'''<br>'''
                    + "Tu email es " + self.request.get('email')+'''<br><br>
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

		