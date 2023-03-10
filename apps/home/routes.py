# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound

from apps.task.models import Task
from apps.authentication.models import Users


@blueprint.route('/index')
@login_required
def index():
    usersdata = Users.query.all()
    totaluser = Users.query.count()
    user_db_data = Task.query.filter_by(user_id=current_user.id).all()
    user_db_count = Task.query.filter_by(user_id=current_user.id).count()

    return render_template('home/index.html', tasks = user_db_data, task_count = user_db_count, list_users = usersdata, total_user = totaluser, segment='index')


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
