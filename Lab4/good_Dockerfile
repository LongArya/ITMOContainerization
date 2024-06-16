FROM jupyterhub/jupyterhub:3.1.1

WORKDIR /jupyter

# system deps 
RUN apt update && \
    apt -y install python3-dev \
    git \ 
    vim \
    nano

# python deps 
RUN pip3 install psycopg2-binary notebook
CMD jupyterhub --log-level=DEBUG