from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app.models import Task, Platform
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
        try:
            data = request.form
            
            # Разрешенные поля
            allowed_fields = {
                'title', 'theme_prompt', 
                'article_prompt', 'image_prompt',
                'theme_list', 'article_list', 'platform_id',
                'schedule_time', 'schedule_days', 'is_active'
            }
            
            # Фильтрация полей
            task_data = {
                key: data.get(key) 
                for key in allowed_fields 
                if key in data
            }
            
            # Если платформа не выбрана, удалите ключ platform_id из task_data
            if not task_data.get('platform_id'):
                task_data.pop('platform_id', None)
            
            new_task = Task(**task_data)
            db.session.add(new_task)
            db.session.commit()
            
            flash('Task added successfully')
            return redirect(url_for('tasks.task_list'))
            
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}")
            return redirect(url_for('tasks.add_task'))
    platforms = Platform.query.all()
    return render_template('tasks/add.html', platforms=platforms)

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
        task.platform_id = request.form.get('platform_id') or None
        task.schedule_time = request.form['schedule_time']
        task.schedule_days = request.form['schedule_days']
        task.is_active = request.form['is_active']
        db.session.commit()
        flash('Task updated successfully')
        return redirect(url_for('tasks.task_list'))
    platforms = Platform.query.all()
    return render_template('tasks/edit.html', task=task, platforms=platforms)

@tasks_bp.route('/tasks/log/<int:task_id>')
@login_required
def task_log(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('tasks/log.html', task=task)

@tasks_bp.route('/tasks/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully')
    return redirect(url_for('tasks.task_list'))

@tasks_bp.route('/platforms', methods=['POST'])
def create_platform():
    data = request.get_json()
    new_platform = Platform(
        name=data['name'],
        description=data.get('description')
    )
    db.session.add(new_platform)
    db.session.commit()
    return jsonify({'message': 'Platform created'}), 201

@tasks_bp.route('/platforms/<int:platform_id>', methods=['GET'])
def get_platform(platform_id):
    platform = Platform.query.get_or_404(platform_id)
    return jsonify({
        'name': platform.name,
        'description': platform.description,
        'tasks_count': len(platform.tasks)
    })

@tasks_bp.route('/platforms')
@login_required
def platform_list():
    platforms = Platform.query.all()  # Получаем все платформы из БД
    return render_template('platforms/list.html', platforms=platforms)

@tasks_bp.route('/platforms/add', methods=['GET', 'POST'])
@login_required
def add_platform():
    if request.method == 'POST':
        platform_name = request.form['platform_name']
        new_platform = Platform(name=platform_name)
        db.session.add(new_platform)
        db.session.commit()
        flash('Platform added successfully')
        return redirect(url_for('platforms.platform_list'))
    return render_template('platforms/add.html')

@tasks_bp.route('/platforms/delete/<string:platform_name>', methods=['POST'])
@login_required
def delete_platform(platform_name):
    platform = Platform.query.filter_by(name=platform_name).first()
    if platform:
        db.session.delete(platform)
        db.session.commit()
        flash('Platform deleted successfully')
    return redirect(url_for('platforms.platform_list'))
