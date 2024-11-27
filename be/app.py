from __init__ import create_app
from flask import request, redirect
from service import Service

BASE_URL = 'http://localhost:5000'
app = create_app()
service = Service()

# Helper function
def structure_short_code_response(short_code):
    return {'short_url': f'{BASE_URL}/{short_code}', 'short_code': short_code}

# Routes
@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json.get('url')

    if not long_url:
        return {"error": "URL is required"}, 400

    existing_short_code = service.get_short_code(long_url)
    if existing_short_code:
        return structure_short_code_response(existing_short_code), 200

    short_code = service.create_short_code(long_url)
    return structure_short_code_response(short_code), 201


@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    long_url = service.get_long_url(short_code)

    if not long_url:
        return {"error": "Short URL not found"}, 404

    return redirect(long_url, code=302)


if __name__ == '__main__':
    app.run(debug=True)
