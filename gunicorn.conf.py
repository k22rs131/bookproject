# gunicorn.conf.py
bind = "0.0.0.0:8000"
workers = 3
threads = 1
timeout = 30
loglevel = "debug"
