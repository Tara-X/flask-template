# -*- coding: utf-8 -*-


import os
import sys
import time

from flask import Flask, jsonify, session, request, send_file, redirect

from app.routes.auth import mod


@mod.route('/auth', methods=["GET"])
def test_auth():
    return jsonify({'route' : '/api/auth'})

