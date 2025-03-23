from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from .models import Task
from app import db

tasks_bp = Blueprint('tasks', __name__, template_folder='templates')

@tasks_bp.route('/tasks')
@login_required
def task_list():
    tasks = Task.query.all()
    return render_template('tasks/list.html', tasks=tasks)

@tasks_bp.route('/tasks/add', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully')
        return redirect(url_for('tasks.task_list'))
    return render_template('tasks/add.html')
