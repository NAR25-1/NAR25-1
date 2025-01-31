from flask import Flask, render_template, request
from database import get_db_connection
app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
    return render_template("test.html")

@app.route('/login', methods=['GET', 'POST'])
def query():
    results = None  
    if request.method == 'POST':
        trainee_numb = request.form.get('trainee_number')
        trainee_pass = request.form.get('trainee_pass')
        connection = get_db_connection()
        if connection is None:
            return "Failed to connect to the database!"
        try:
            with connection.cursor() as cursor:
                query = "SELECT * FROM trainee WHERE trainee_number = %s AND trainee_pass = %s"
                cursor.execute(query, (trainee_numb,trainee_pass))
                results = cursor.fetchall() 
        finally:
            connection.close()
    return render_template("login.html", results=results)

if __name__ == '__main__':
    app.run(debug=True)