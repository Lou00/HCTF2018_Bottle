from selenium import webdriver
import os
import time

browser = webdriver.Firefox(executable_path = '/var/bottle/geckodriver')
while(True):
    time.sleep(2)
    browser.get("http://127.0.0.1:3000/path?path=http://127.0.0.1:0/%0A%0D%0A%0D<h1>")
    if 'Content-Security-Policy' in browser.page_source:
        os.popen('/var/bottle/restart.sh')
    else:
        browser.quit()
        break
with open('/var/bottle/header.log','a') as f:
    f.write(time.asctime( time.localtime(time.time()))+' cheak_header run' + '\n')
