#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask import render_template, redirect, url_for, abort, flash, request, current_app,\
    make_response
from flask.ext.login import login_required, current_user
import os

from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template("harryx.html")