FROM tsl0922/ttyd:latest 
RUN apt-get update
RUN apt-get install python3 -y
RUN  mkdir d
RUN  cd  d
WORKDIR  /d
ADD p.py .
ENTRYPOINT ["ttyd","python3","p.py"]

