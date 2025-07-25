from flask import Blueprint, render_template

team_bp = Blueprint('team', __name__, url_prefix='/team')

@team_bp.route('/')
def team():
    return render_template('team.html')

@team_bp.route('/professor')
def professor():
    return render_template('professor.html')

@team_bp.route('/students')
def students():
    return render_template('students.html')