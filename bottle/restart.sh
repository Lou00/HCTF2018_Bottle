kill `ps aux|grep -n 'python3\ main.py'|awk '{print $2}'`
nohup python3 main.py &