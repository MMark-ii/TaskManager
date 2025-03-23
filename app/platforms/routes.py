from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required

platforms_bp = Blueprint('platforms', __name__, template_folder='templates')

@platforms_bp.route('/platforms')
@login_required
def platform_list():
    platforms = [
        {"name": "Platform 1", "script": "script1.py"},
        {"name": "Platform 2", "script": "script2.py"},
        {"name": "Platform 3", "script": "script3.py"}
    ]  # Замените на реальный список платформ из базы данных
    return render_template('platforms/list.html', platforms=platforms)

@platforms_bp.route('/platforms/add', methods=['GET', 'POST'])
@login_required
def add_platform():
    if request.method == 'POST':
        platform_name = request.form['platform_name']
        platform_script = request.form['platform_script']
        # Добавьте логику для сохранения новой платформы в базу данных
        flash('Platform added successfully')
        return redirect(url_for('platforms.platform_list'))
    return render_template('platforms/add.html')

@platforms_bp.route('/platforms/edit/<string:platform_name>', methods=['GET', 'POST'])
@login_required
def edit_platform(platform_name):
    platform = {"name": platform_name, "script": "script.py"}  # Замените на реальную платформу из базы данных
    if request.method == 'POST':
        platform['name'] = request.form['platform_name']
        platform['script'] = request.form['platform_script']
        # Добавьте логику для обновления платформы в базе данных
        flash('Platform updated successfully')
        return redirect(url_for('platforms.platform_list'))
    return render_template('platforms/edit.html', platform=platform)

@platforms_bp.route('/platforms/delete/<string:platform_name>', methods=['POST'])
@login_required
def delete_platform(platform_name):
    # Добавьте логику для удаления платформы из базы данных
    flash('Platform deleted successfully')
    return redirect(url_for('platforms.platform_list'))
