# https://hub.docker.com/r/codercom/code-server/tags
FROM codercom/code-server:4.4.0
USER root

ENV DEBIAN_FRONTEND=noninteractive

# Everything to be installed by apt-get
RUN apt update && apt install -y --no-install-recommends \
    wget \
    build-essential \
    python3.9 \
    python3-pip \
    julia \
    elixir \
    php \
    npm \
    zsh \
    neofetch && \
    rm -rf /var/lib/apt/lists/*

# Golang install
RUN wget https://dl.google.com/go/go1.18.1.linux-amd64.tar.gz && \
    tar -xvf go1.18.1.linux-amd64.tar.gz && \
    mv go /usr/local && \
    rm go1.18.1.linux-amd64.tar.gz

ENV GOROOT /usr/local/go
ENV GOPATH /home/coder/code-server/go
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH

# Python 3.9 install
RUN pip3 install pipenv pylint flake8

# Composer Install
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" &&\
    php composer-setup.php &&\
    php -r "unlink('composer-setup.php');" &&\
    mv composer.phar /usr/local/bin/composer

# Typescript install
RUN npm install -g npm && \
    npm install -g typescript node ts-node nodemon

# Get Docker
RUN curl -fsSL https://get.docker.com -o get-docker.sh && \
    sh get-docker.sh &&\
    curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose &&\
    chmod +x /usr/local/bin/docker-compose

# Install Rust
ENV CARGO_HOME /cargo
ENV RUSTUP_HOME=/rust
ENV PATH=/cargo/bin:/rust/bin:$PATH

RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

# zsh plugins
RUN chsh -s /bin/zsh &&\
    touch /home/coder/.zshrc &&\
    usermod -m -d /home/coder coder

ENV SHELL /usr/bin/zsh

RUN chown -R coder:coder /home/coder

USER coder

# Set terminal commands and permissions
RUN sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" &&\
    echo 'export PATH=/home/coder/bin/:$PATH' >> ~/.zshrc &&\
    echo 'export PATH=/home/coder/.local/bin/:$PATH' >> ~/.zshrc &&\
    echo 'export PATH=/usr/local/bin/:$PATH' >> .zshrc &&\
    sed -i -e 's/ZSH_THEME="robbyrussell"/ZSH_THEME="gnzh"/g' ~/.zshrc


# Install Sharp Programs

RUN sudo curl -s -L https://github.com/Sharpz7/sharpdev/releases/download/1.3/install.sh | sudo bash && \
    sudo curl -s -L https://github.com/Sharpz7/sharpcd/releases/download/3.7/install.sh | sudo bash -s client

# Custom Fonts
RUN git clone https://github.com/tuanpham-dev/code-server-font-patch.git &&\
    cd code-server-font-patch &&\
    sudo ./patch.sh


# Sharpnet Stuff
COPY ./buildfiles/start.sh /start.sh
COPY ./sharpnet/nginx.conf /sharpnet/nginx.conf

RUN sudo chmod +x /start.sh

ENTRYPOINT ["/start.sh"]
CMD [""]
