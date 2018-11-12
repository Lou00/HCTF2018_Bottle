from selenium import webdriver
import os
import time

browser = webdriver.Firefox(executable_path = '/var/bottle/geckodriver')
while(True):
    time.sleep(2)
    browser.get("http://127.0.0.1:3000/path?path=http://bottle.2018.hctf.io:0/%0a%0d%0a%0d<h1>")
    if 'Content-Security-Policy' in browser.page_source:
        browser.quit()
        break
    else:
        os.popen('/var/bottle/restart.sh')
with open('/var/bottle/header.log','a') as f:
    f.write(time.asctime( time.localtime(time.time()))+' cheak_header_error run'+ '\n')
