
from flask_cors import CORS
from flask import Flask, jsonify, request
from solve_n_queens import solve_n_queens

app = Flask(__name__)
CORS(app)
@app.route('/solve_n_queens', methods=['POST','OPTIONS'])
def solve_n_queens_route():
    if request.method == 'OPTIONS':
        
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        return ('', 200, headers)  # Changed  204 to 200

    try:
        data = request.get_json()
        n = data['n']
        solutions = solve_n_queens(n)

        
        response = jsonify({'solutions': solutions})
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except Exception as e:
        return jsonify({'error': str(e)})
if __name__ == '__main__':
    app.run(debug=True)
