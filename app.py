from datetime import timezone, datetime

from flask import Flask, request, render_template, jsonify
from flask_restful import Api

from Model_sqlite import Workout, db
from config import  Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

api = Api(app)
with app.app_context():
    db.create_all()

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

    workout = Workout(
        date=data["date"],
        time=data["time"],
        sent_to_flask=True,
        sent_at=datetime.now(timezone.utc),
        data=data["data"]
    )

    db.session.add(workout)

    db.session.commit()

    print(workout)

    return jsonify({"status": "success"}), 200




if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()

    app.run(host="0.0.0.0", port=5000, debug=True)