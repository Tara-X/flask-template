#-*- coding: utf-8 -*-

from functools import wraps
from flask import g, url_for, flash, abort, request, redirect, Markup, session, jsonify


def common_error_handler(status):
    def inner_handler(error):
        return jsonify({
            'err_code' : status,
            'err_msg' : traceback.format_exc(sys.exc_info())
        }), status
    return inner_handler


def default_error_handler(e):
    return jsonify({
        'err_code' : -1,
        'err_msg' : traceback.format_exc(sys.exc_info())
   })

