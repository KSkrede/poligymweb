from flask import Flask, render_template
from get_slots import get_slots

app = Flask(__name__)

@app.route('/')
def index():
    start_date_str = "2023-11-07"
    end_date_str = "2023-11-10"
    playground_id = "55"
    
    slots = get_slots(start_date_str, end_date_str, playground_id)
    
    return render_template('index.html', slots=slots)


if __name__ == '__main__':
    app.run(debug=True)
