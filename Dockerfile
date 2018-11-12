#HCTF 2018 web Bottle
#
#usage : 
#    进入Dockerfile目录
#    [docker build -t '自定义镜像名字' . ] //最后的.别少了
#    [docker run -itd --name '你的应用名称' -p 外部端口:3000 ]
FROM ubuntu:16.04
RUN bash -c "debconf-set-selections <<< 'mysql-server mysql-server/root_password password Lou0073eE8'"
RUN bash -c "debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password Lou0073eE8'"
RUN apt-get update
RUN apt-get install -y python3.5  python3-pip && \
    pip3 install https://github.com/bottlepy/bottle/archive/0.12.10.zip && \
    pip3 install mysql-connector && \
    pip3 install bottle-session && \
    pip3 install selenium && \
    pip3 install requests && \
    apt-get install -y xvfb && \
    apt-get install -y firefox && \
    apt-get install -y mysql-server && \
    apt-get install -y redis-server && \
    apt-get install -y cron
ADD bottle /var/bottle
ADD bottle.sql /tmp/bottle.sql
RUN usermod -d /var/lib/mysql/ mysql;ln -s /var/lib/mysql/mysql.sock /tmp/mysql.sock;chown -R mysql:mysql /var/lib/mysql;service mysql start && \
    mysql -uroot -pLou0073eE8 < /tmp/bottle.sql && \
    rm /tmp/bottle.sql
RUN /etc/init.d/redis-server start && \
    /etc/init.d/cron start
RUN echo "*/3 * * * * kill \`ps aux|grep -n 'Xvfb\ :99'|awk '{print $2}'\`;xvfb-run python3 /var/bottle/cheak_header.py" >> /etc/crontab && \
    echo "*/10 * * * * kill \`ps aux|grep -n 'Xvfb\ :99'|awk \'{print $2}'\`;xvfb-run python3 /var/bottle/cheak_header_error.py" >> /etc/crontab
WORKDIR /var/bottle
RUN chmod +x restart.sh
CMD ln -s /var/lib/mysql/mysql.sock /tmp/mysql.sock;chown -R mysql:mysql /var/lib/mysql;service mysql start && \
    /etc/init.d/redis-server start && \
    /var/bottle/restart.sh && \
    /bin/bash
EXPOSE 3000