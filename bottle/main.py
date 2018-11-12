import bottle
from bottle import route,SimpleTemplate, run, template, request, response, error, static_file
import mysql.connector
import db
import bottle_session
import threading,time
import re

#session
app = bottle.app()
plugin = bottle_session.SessionPlugin(cookie_lifetime = 600)
app.install(plugin)

@route('/css/<name>')
def server_static(name):
    return static_file(name, root='/var/bottle/css')
@route('/favicon.ico')
def favicon():
    pass

@route('/')
def index():
    return template('/var/bottle/template/index')

@route('/user',method='get')
def index(session):
    userId = session.get('id')
    if userId:
        if int(userId) == 1:
            return template('/var/bottle/template/user',username='flag',errors='hctf{26372420de8d5c94f8fb007c4389841f}',captcha = '')
    username = db.find_user(userId)
    if (username):
        captcha = db.get_random()
        session['captcha'] = captcha
        return template('/var/bottle/template/user', username=username , errors='',captcha='substr(md5(captcha),0,4) == ' + captcha)
    else :
        return 'you are not login'
@route('/user',method='post')
def index(session):
    userId = session.get('id')
    url = request.forms.get('url')
    if len(url)>200:
        return template('/var/bottle/template/user',username=username , errors='url too long',captcha='')
    captcha = request.forms.get('captcha')
    captcha = db.md5(captcha)[0:4]
    if captcha != session.get('captcha'):
        return bottle.redirect('/path?path=/user')
    username = db.find_user(userId)
    if (username):
        url_status =  db.insert_url(userId,url)
        if (url_status == 1):
            return template('/var/bottle/template/success')
        if (url_status == 0):
            return template('/var/bottle/template/user',username=username , errors='submit failed',captcha='')
    else :
        return 'you are not login'

@route('/logout',method='get')
def index(session):
    session.destroy()
    return template('/var/bottle/template/index')

@route('/register',method='get')
def index():
    return template('/var/bottle/template/register',error='')
@route('/register',method='post')
def index():
    username = request.forms.get('username')
    password = request.forms.get('password')
    confirm = request.forms.get('confirm')
    if  username and  password and confirm:
        pass
    else :
        return template('/var/bottle/template/register',error="don't empty")
    if password != confirm:
        return template('/var/bottle/template/register',error="Different password")
    if len(password) < 6:
        return template('/var/bottle/template/register',error='password too small')
    if len(password) >30:
        return template('/var/bottle/template/register',error='password too long')
    if len(username) > 20:
        return template('/var/bottle/template/register',error='username too long')
    register_status = db.register_user(username,password)
    if register_status == 2:
        return template('/var/bottle/template/register',error='username already exist')
    if register_status == 1:
        return bottle.redirect('/path?path=/login')
    if register_status == 0:
        return template('/var/bottle/template/register',error='Registration failed')

@route('/login',method='get')
def index():
    return template('/var/bottle/template/login',error='')
@route('/login',method='post')
def index(session):
    username = request.forms.get('username')
    password = request.forms.get('password')
    isLogin = db.login_user(username,password)
    if (isLogin):
        session['id'] = isLogin
        return bottle.redirect('/path?path=/user')
    else:
        return template('/var/bottle/template/login',error='Login failed')


def waf(string):
    if '@' in string:
        return 0
    if '(' in string:
        return 0
    if ')' in string:
        return 0
    if "'" in string:
        return 0
    if '"' in string:
        return 0
    #pattern = re.compile('^http://bottle.2018.hctf.io')
    #isConform = pattern.match(string)
    isConform = 1
    if isConform:
        return 1
    else:
        return 0
@route('/path')
def index():
    path = request.query.get('path', '/')
    response.add_header('Content-Security-Policy',"default-src 'self'; script-src 'self'")
    print(path)
    if waf(path):
        return bottle.redirect(path)
    else:
        return template('/var/bottle/template/path',path=path)




@error(404)
def error404(error):
    return template('/var/bottle/template/404')

if __name__ == '__main__':
    bottle.debug(False)
    run(host='0.0.0.0', port=3000,sever = 'paste')
