from apps.task import blueprint
from flask import render_template, request,flash, redirect,url_for
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound

from apps import db, login_manager
from apps.task import blueprint
from apps.task.forms import TaskForm
from apps.task.models import Task
from apps.authentication.models import Users

@blueprint.route('/task', methods=['GET', 'POST'])
@login_required
def index():
    create_task_form = TaskForm(request.form)
    if 'task' in request.form:
        info = request.form["task_info"]
        name = request.form["task_name"] 
        result = add_task(current_user.id,name.title(),info.title())

        return redirect(url_for('task_blueprint.index'))
        # return render_template('task/index.html',
        #                        result,user_list_task = list_task(),
        #                        form=create_task_form)
    else:
       
        return render_template('task/index.html', user_list_task = list_task(), segment='task',form=create_task_form)

@blueprint.route("/list_task",methods=['GET'])
def list_task():
    try:
        user_task = []
        user_db_data = Task.query.filter_by(user_id=current_user.id).all()
        # user_db_data = Task.query.filter_by(user_id=current_user.id).order_by(timestamp.desc()).all()
        for index,value in enumerate(user_db_data):
            print(value.status)
            if value.status != 1:
                user_task.append(value)
        return user_task
    except:
        return render_template('home/page-500.html'), 500
    
@blueprint.route("/add_task",methods=['POST'])
def add_task(user_id,task_name, task_info):
    try:
        add_task = Task(user_id=user_id,task_info=task_info.title(),task_name=task_name.title())
        db.session.add(add_task)
        db.session.commit()
        result = {"msg":"Task created successfully", "succes":True}
        return result
    except:
        result = {"msg":"Create task failed", "succes":False}
        return render_template('home/page-500.html'), 500