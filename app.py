from flask import Flask, render_template, request
from n_queen_solver import get_solution

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n = int(request.form['n'])
        solution = get_solution(n)
        if solution:
            return render_template('index.html', board=solution, n=n, success=True)
        else:
            return render_template('index.html', error="No solution exists for N = {}".format(n), success=False)
    return render_template('index.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)
