from flask import Flask, render_template
app = Flask(__name__)
@app.route('/insert')
def insertData():
    my_data = Data(username="viveksdf", email="vivsadaek@gmail.com")
    db.session.add(my_data)
    db.session.commit()

@app.route('/')
def hello_world():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)