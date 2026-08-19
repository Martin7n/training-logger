from flask import Flask, request, render_template, jsonify
from flask_restful import Api

from Models_psgr import BookModel
from config import db_connection1
from data_pr import test3
from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'{db_connection1}'
db.init_app(app)

api = Api(app)
# db.create_all()

# api.add_resource(Book, "/<int:pk>")


'''templates start'''
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/x5')
def x5():
    return render_template('on6.html')

@app.route('/workout/add',  methods=["POST"])
def workout_add():
    data = request.get_json()
    print(data)

    return jsonify({"status": "success"}), 200




if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()

    app.run(host="0.0.0.0", port=5000, debug=True)