# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, send_from_directory

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
    return jsonify({'status' : 'ok'})

@mod.route('/api')
def api():
    return jsonify({'status' : 'api-ok'})
