from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

# In-memory storage for votes
votes = {'Candidate A': 0, 'Candidate B': 0}

@app.route('/')
def home():
    return "<h1>Online Voting System Online</h1><p>System Health: Good</p>"

@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    candidate = data.get('candidate')
    if candidate in votes:
        votes[candidate] += 1
        return jsonify({"message": f"Vote cast for {candidate}!", "current_tally": votes})
    return jsonify({"error": "Invalid candidate"}), 400

@app.route('/metrics')
def metrics():
    # This endpoint is for Prometheus (DevOps Monitoring)
    return f"# HELP total_votes Total number of votes\n# TYPE total_votes counter\ntotal_votes {sum(votes.values())}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)