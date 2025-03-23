from flask import Blueprint, render_template
from flask_login import login_required
from app.tasks.models import Task  # ← Исправлен импорт

# Инициализация Blueprint должна быть в начале
tasks_bp = Blueprint('tasks', __name__, template_folder='templates')

@tasks_bp.route('/tasks')
@login_required
def task_list():
    tasks = Task.query.all()
    return render_template('tasks/list.html', tasks=tasks)
