from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory storage for votes
votes = {'Candidate A': 0, 'Candidate B': 0}

# LOGIN PAGE
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        voter_id = request.form.get('voter_id')
        password = request.form.get('password')

        # Simple dummy login check (for project)
        if voter_id == "admin" and password == "admin123":
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')


# DASHBOARD PAGE
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', votes=votes)


# VOTING API
@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    candidate = data.get('candidate')

    if candidate in votes:
        votes[candidate] += 1
        return jsonify({
            "message": f"Vote cast for {candidate}!",
            "current_tally": votes
        })

    return jsonify({"error": "Invalid candidate"}), 400


# METRICS FOR DEVOPS (PROMETHEUS)
@app.route('/metrics')
def metrics():
    return (
        "# HELP total_votes Total number of votes\n"
        "# TYPE total_votes counter\n"
        f"total_votes {sum(votes.values())}"
    )


if __name__ == '__main__':
    app.run(debug=True)

    