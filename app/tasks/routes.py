from flask import Blueprint, render_template, redirect, url_for, flash, request
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
        theme_prompt = request.form['theme_prompt']
        article_prompt = request.form['article_prompt']
        image_prompt = request.form['image_prompt']
        platforms = request.form.getlist('platforms')
        schedule = request.form['schedule']
        new_task = Task(
            title=title,
            theme_prompt=theme_prompt,
            article_prompt=article_prompt,
            image_prompt=image_prompt,
            platforms=platforms,
            schedule=schedule
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully')
        return redirect(url_for('tasks.task_list'))
    return render_template('tasks/add.html')
