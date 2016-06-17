FROM ubuntu:latest
MAINTAINER onerhao@gmail.com

# TODO: change the apt-get mirror in /etc/apt/sources.list and pip mirror in $HOME/.pip/pip.conf
# otherwise it would be way too slow in China mainland

# change apt-get software respository's mirror url
# heredoc cat << EOF is not supported
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse" > /etc/apt/sources.list

# change pip' mirror url
RUN mkdir $HOME/.pip && echo "[global]\n#index-urls:  https://pypi.douban.com, https://mirrors.aliyun.com/pypi,\ncheckout https://www.pypi-mirrors.org/ for more available mirror servers\nindex-url = https://pypi.douban.com/simple\ntrusted-host = pypi.douban.com" > $HOME/.pip/pip.conf

# install basic requirements
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        curl \
        libjpeg-dev \
        zlib1g-dev \
        python-dev \
        python-setuptools \
        python-pip \
        python3 \
        python3-pip \
        python3-dev \
        python-scrapy \
        python-django \
        libmysqlclient-dev \
        mysql-server \
        mysql-client \
        redis-server

RUN easy_install pip==8.1.2 setuptools
# install scrapyprj
RUN mkdir $HOME/src/
RUN git clone https://github.com/Alexoner/web-crawlers.git $HOME/src/scrapyprj && \
    cd $HOME/src/scrapyprj && pip install -r requirements.txt && cd ..
RUN git clone https://github.com/Alexoner/sloth.git $HOME/src/sloth && \
    cd $HOME/src/sloth && pip install -r requirements.txt && cd ..

RUN rm -rf /var/lib/apt/lists/*
# create unprivileged user
RUN adduser --disabled-password --gecos '' admin

WORKDIR $HOME/src/
EXPOSE 8000 8000
