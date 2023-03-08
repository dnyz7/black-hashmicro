from apps.test import blueprint
from flask import render_template, request, redirect,url_for
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.test.forms import TestForm

# from apps import db
from apps.test import blueprint
from apps.test.forms import TestForm
# from apps.task.models import Task

@blueprint.route('/test', methods=['GET', 'POST'])
@login_required
def index():
    create_test_form = TestForm(request.form)
    if 'test' in request.form:
        string1 = request.form["string1"]
        string2 = request.form["string2"]
        n = 0
        samestring = ''
        for char1 in range(0, len(string1)):
            for char2 in range(0,len(string2)):
                # print(string1[char1] + ',' + string1[char1])
                if string1[char1].lower() == string2[char2].lower():
                    # print(string1[char1] + ',' + string1[char1])
                    samestring = samestring + string1[char1]
                    n = n + 1
                    break
        percent = (n / len(string1)) * 100
        
        if n > 0:
            result = '' + string1 + ' on ' + string2 + ' = ' + samestring + ' = ' + str(n) + '/' + str(len(string1)) + ' = ' + str(percent) + '%'
        else:
            result = '' + string1 + ' on ' + string2 + ' = Not Found = ' + str(percent) + '%'
        return render_template('test/index.html', result = result, segment='test',form=create_test_form)
        # return redirect(url_for('test_blueprint.index'))
    else:
         
        return render_template('test/index.html', segment='test',form=create_test_form)
    # create_test_form = TestForm(request.form)
    # if 'test' in request.form:
    #     # string1 = request.form["string1"]
    #     # string2 = request.form["string2"] 

    #     return redirect(url_for('test_blueprint.index'))
       
    # else:
    #     return redirect(url_for('test_blueprint.index'))
    #     # return render_template('test/index.html', segment='test',form=create_test_form)

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