from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="rlewsley99",
    password="rapid7pool",
    hostname="rlewsley99.mysql.pythonanywhere-services.com",
    databasename="rlewsley99$pool-records",
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Create the SQLAlchemy object
db = SQLAlchemy(app)

# Create a simple model for recordings


class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Ronan = db.Column(db.Integer)
    Glenn = db.Column(db.Integer)

    def __repr__(self):
        return f"Scores('{self.Ronan}', {self.Glenn})"


with app.app_context():
    db.create_all()

# Route to display recordings


@app.route("/", methods=["GET", "POST"])
def display_scores():
    if request.method == "GET":

        total = {'ronan': 0, 'glenn': 0}
        for score in Scores.query.all():
            total['ronan'] += score.Ronan
            total['glenn'] += score.Glenn

        return render_template('Scores.html', scores=Scores.query.all(), total_count=total)

    score = Scores(Ronan=request.form["Ronan"], Glenn=request.form["Glenn"])
    db.session.add(score)
    db.session.commit()
    return redirect(url_for('display_scores'))


@app.route("/delete/<int:id>", methods=["POST"])
def delete_score(id):
    score = Scores.query.filter_by(id=id).first()
    db.session.delete(score)
    db.session.commit()
    return redirect(url_for('display_scores'))


if __name__ == '__main__':
    app.run(debug=True)
