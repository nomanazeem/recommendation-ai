from flask import Flask
from flask_cors import CORS
from recommend_mysql import recommend_mysql_blueprint
from record import record_blueprint

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Register blueprints
app.register_blueprint(recommend_mysql_blueprint)
app.register_blueprint(record_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
