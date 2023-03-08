from apps.test import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

@blueprint.route('/test')
@login_required
def index():
    return render_template('test/index.html', segment='test')

# from apps import db, login_manager
# from apps.task import blueprint
# from apps.task.forms import TaskForm
# from apps.task.models import Task
# from apps.authentication.models import Users

# from flask_login import current_user

# @blueprint.route("/add_new_task",methods=['POST'])
# def add_new_task():
#     # task_form = TaskForm(request.form)
#     title = request.form("task_info")
#     info = request.form("task_name")   

#     # if not title.strip():
#     #     return redirect('/')
#     # if not info.strip:
#     #     return redirect('/')
#     # task = Task(**request.form)

#     # add task to user db
#     new_task = Task(user_id=current_user['user_id'],task_info=info.title(),task_title=title.title())
#     try:
#         db.session.add(new_task)
#         db.session.commit()
#         flash("Task Added SuccessFully")
#         return redirect('/')
#     except:
#         return render_template('home/page-500.html'), 500