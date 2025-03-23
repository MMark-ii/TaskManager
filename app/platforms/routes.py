from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required

platforms_bp = Blueprint('platforms', __name__, template_folder='templates')

@platforms_bp.route('/platforms')
@login_required
def platform_list():
    platforms = ["Platform 1", "Platform 2", "Platform 3"]  # Замените на реальный список платформ из базы данных
    return render_template('platforms/list.html', platforms=platforms)

@platforms_bp.route('/platforms/add', methods=['GET', 'POST'])
@login_required
def add_platform():
    if request.method == 'POST':
        platform_name = request.form['platform_name']
        # Добавьте логику для сохранения новой платформы в базу данных
        flash('Platform added successfully')
        return redirect(url_for('platforms.platform_list'))
    return render_template('platforms/add.html')

@platforms_bp.route('/platforms/delete/<string:platform_name>', methods=['POST'])
@login_required
def delete_platform(platform_name):
    # Добавьте логику для удаления платформы из базы данных
    flash('Platform deleted successfully')
    return redirect(url_for('platforms.platform_list'))
