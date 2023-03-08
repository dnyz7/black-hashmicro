from apps.task import blueprint
from flask import render_template, request,flash, redirect,url_for
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound

from apps import db, login_manager
from apps.task import blueprint
from apps.task.forms import TaskForm
from apps.task.models import Task

@blueprint.route('/task', methods=['GET', 'POST'])
@login_required
def index():
    create_task_form = TaskForm(request.form)
    if 'task' in request.form:
        info = request.form["task_info"]
        name = request.form["task_name"] 
        result = add_task(current_user.id,name.title(),info.title())

        return redirect(url_for('task_blueprint.index'))
        
    else:
       
        return render_template('task/index.html', user_list_task = list_task(), segment='task',form=create_task_form)

@blueprint.route("/list_task",methods=['GET'])
def list_task():
    try:
        user_db_data = Task.query.filter_by(user_id=current_user.id).all()
        user_db_count = Task.query.filter_by(user_id=current_user.id).count()
       
        return user_db_data, user_db_count
    except:
        return render_template('home/page-500.html'), 500
    
@blueprint.route("/add_task",methods=['POST'])
def add_task(user_id,task_name, task_info):
    try:
        add_task = Task(user_id=user_id,task_info=task_info.title(),task_name=task_name.title())
        db.session.add(add_task)
        db.session.commit()
        result = {"msg":"Task created successfully", "success":True}
        return result
    except:
        result = {"msg":"Create task failed", "succes":False}
        return render_template('home/page-500.html'), 500

@blueprint.route("/task/<int:id>", methods=["GET"])
def get_task(id):
    task = Task.query.get(id)
    if task is None:
        return render_template('home/page-404.html'), 404
    return redirect(url_for('task_blueprint.index'))

@blueprint.route("/update_task/<int:id>", methods=["POST"])
def delete_task(id):
    task = Task.query.get(id)
    if task is None:
        return render_template('home/page-404.html'), 404
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('task_blueprint.index'))

@blueprint.route("/delete_task/<int:id>", methods=["POST"])
def update_task(id):
    if not request.form:
       return render_template('home/page-400.html'), 400
    task = Task.query.get(id)
    if task is None:
        return render_template('home/page-404.html'), 404
    task.task_name = request.form["task_name"]
    task.task_info = request.form["task_info"]
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('task_blueprint.index'))