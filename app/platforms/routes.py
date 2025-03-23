from flask import Blueprint, render_template

platforms_bp = Blueprint('platforms', __name__, template_folder='templates')

@platforms_bp.route('/platforms')
def platform_list():
    return render_template('platforms/list.html')
