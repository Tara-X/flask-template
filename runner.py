#-*- coding: utf-8 -*-

from app import app
import sys

app.secret_key = "tarax-demo"
default_encoding = 'utf-8'

if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
        
if __name__ == '__main__':
    app.run(host="0.0.0.0" , port = 8080, debug=True, use_reloader=True)
