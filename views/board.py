from flask import Blueprint, render_template

board_bp = Blueprint('board', __name__, url_prefix='/board')

@board_bp.route('/')
def board():
    return render_template('board.html')

@board_bp.route('/notice1')
def notice1():
    return render_template('notice1.html')

@board_bp.route('/notice2')
def notice2():
    return render_template('notice2.html')

@board_bp.route('/notice3')
def notice3():
    return render_template('notice3.html')