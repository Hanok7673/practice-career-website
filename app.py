from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Kathmandu, Nepal',
    'salary': 'Rs.320000'
}, {
    'id': 2,
    'title': 'Software Engineer',
    'location': 'Kathmandu, Nepal',
    'salary': 'Rs.120000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Kathmandu, Nepal',
    'salary': 'Rs.100000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Kathmandu, Nepal',
    'salary': 'Rs.150000'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Paisa Kamau')


@app.route('/api/jobs')
def job_list():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
