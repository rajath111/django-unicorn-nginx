import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
wsgi_app = 'sample_api.wsgi:application'
