from flask import Flask, render_template, redirect, url_for
from get_slots import get_slots

app = Flask(__name__)
slots = {}

@app.route('/')
def index():
    return render_template('index.html', slots=slots)

@app.route('/fetch_slots', methods=['POST'])
def fetch_slots():
    start_date_str = "2023-11-08"
    end_date_str = "2023-11-08"
    playground_id = "55"
    
    global slots
    slots = get_slots(start_date_str, end_date_str, playground_id)
    
    return render_template('index.html', slots=slots)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))