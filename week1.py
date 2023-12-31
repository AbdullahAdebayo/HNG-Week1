from flask import Flask, request, jsonify
import datetime


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.datetime.utcnow().strftime("%A")
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    github_file_url = 'https://github.com/AbdullahAdebayo/HNG-Week1/blob/master/week1.py'
    github_repo_url = 'https://github.com/AbdullahAdebayo/HNG-Week1.git'

    response = {
        'slack_name': slack_name,
        'track': track,
        'current_day': current_day,
        'utc_time': utc_time,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)