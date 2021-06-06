FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root

ADD entrypoint.sh /root/entrypoint.sh

RUN apt update && \
    apt upgrade -y && \
    apt install -y python3 python3-pip git curl vim* && \
    mkdir -p /etc/vim/backup && \
    mkdir -p /etc/vim/undo && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/vim/vimrc -o /etc/vim/vimrc && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/linux/bashrc/.bashrc_node_docker -o /root/.bashrc && \
    git clone https://github.com/tuimac/screen_capture && \
    git config --global user.email "tuimac.devadm01@gmail.com" && \
    git config --global user.name "tuimac" && \
    pip3 install opencv-python pyautogui numpy

#ENTRYPOINT ["/root/entrypoint.sh"]
