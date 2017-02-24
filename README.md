## Install

```
$ pyenv use v2.7.12
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```


## Run
```
$ source venv/bin/activate
$ pip install -r requirements.txt

# Development mode
$ python runner.py

# Production mode
$ gunicorn -w4 -k gevent -b0.0.0.0:8899 run:app 
```



