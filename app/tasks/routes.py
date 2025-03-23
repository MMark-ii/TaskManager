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
        theme_list = request.form['theme_list']
        article_list = request.form['article_list']
        platforms = request.form.getlist('platforms')
        schedule_time = request.form['schedule_time']
        schedule_days = request.form['schedule_days']
        is_active = request.form['is_active'] == 'active'
        schedule = f"{schedule_time} every {schedule_days} days"
        new_task = Task(
            title=title,
            theme_prompt=theme_prompt,
            article_prompt=article_prompt,
            image_prompt=image_prompt,
            theme_list=theme_list,
            article_list=article_list,
            platforms=platforms,
            schedule=schedule,
            is_active=is_active
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully')
        return redirect(url_for('tasks.task_list'))
    return render_template('tasks/add.html')

@tasks_bp.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.theme_prompt = request.form['theme_prompt']
        task.article_prompt = request.form['article_prompt']
        task.image_prompt = request.form['image_prompt']
        task.theme_list = request.form['theme_list']
        task.article_list = request.form['article_list']
        task.platforms = request.form.getlist('platforms')
        schedule_time = request.form['schedule_time']
        schedule_days = request.form['schedule_days']
        task.schedule = f"{schedule_time} every {schedule_days} days"
        task.is_active = request.form['is_active'] == 'active'
        db.session.commit()
        flash('Task updated successfully')
        return redirect(url_for('tasks.task_list'))
    return render_template('tasks/edit.html', task=task)

@tasks_bp.route('/tasks/log/<int:task_id>')
@login_required
def task_log(task_id):
    task = Task.query.get_or_404(task_id)
    # Здесь вы можете добавить логику для отображения журнала задачи
    return render_template('tasks/log.html', task=task)

@tasks_bp.route('/tasks/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully')
    return redirect(url_for('tasks.task_list'))

@tasks_bp.route('/platforms')
@login_required
def platform_list():
    platforms = ["Platform 1", "Platform 2", "Platform 3"]  # Замените на реальный список платформ из базы данных
    return render_template('platforms/list.html', platforms=platforms)

@tasks_bp.route('/platforms/add', methods=['GET', 'POST'])
@login_required
def add_platform():
    if request.method == 'POST':
        platform_name = request.form['platform_name']
        # Добавьте логику для сохранения новой платформы в базу данных
        flash('Platform added successfully')
        return redirect(url_for('platforms.platform_list'))
    return render_template('platforms/add.html')

@tasks_bp.route('/platforms/delete/<string:platform_name>', methods=['POST'])
@login_required
def delete_platform(platform_name):
    # Добавьте логику для удаления платформы из базы данных
    flash('Platform deleted successfully')
    return redirect(url_for('platforms.platform_list'))
