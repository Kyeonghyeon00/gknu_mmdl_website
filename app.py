from flask import Flask
from views.main import main_bp
from views.board import board_bp
from views.team import team_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(board_bp)
app.register_blueprint(team_bp)

if __name__ == '__main__':
    app.run(debug=True)