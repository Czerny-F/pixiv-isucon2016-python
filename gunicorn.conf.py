import multiprocessing

bind = 'unix:/tmp/gunicorn_isucon.sock'
backlog = 2048

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

daemon = False
raw_env = [
    # 'DJANGO_SECRET_KEY=something',
    # 'SPAM=eggs',
]
pidfile = '/tmp/gunicorn.pid'
umask = 0
user = None
group = None
tmp_upload_dir = None

#
#   Logging
#
#   logfile - The path to a log file to write to.
#
#       A path string. "-" means log to stdout.
#
#   loglevel - The granularity of log output
#
#       A string of "debug", "info", "warning", "error", "critical"
#

errorlog = '/tmp/gunicorn.error.log'
loglevel = 'info'
accesslog = '/tmp/gunicorn.access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
