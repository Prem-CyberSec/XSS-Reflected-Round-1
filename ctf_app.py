from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

@app.route('/set_flag')
def set_flag():
    # Create the response message
    message = "Flag cookie set. <a href='/'>Go to search</a>"
    
    # Create response and set cookie
    response = make_response(message)
    response.set_cookie(
        key='flag',
        value='flag{r3fl3ct3d_xss_pwn3d}',
        max_age=3600,  # Expires in 1 hour
        path='/'       # Available site-wide
    )
    
    return response

@app.route('/', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if query:
        # **VULNERABLE SINK**: Directly include query without sanitization
        result_message = f"<p>You searched for: {query}</p>"
    else:
        result_message = "<p>Enter a search term.</p>"
    
    html = """
<!DOCTYPE html>
<html>
<head><title>Search Results</title></head>
<body>
<h1>Search Results</h1>
{{ result_message | safe }}
<form method="GET">
<input type="text" name="query">
<input type="submit" value="Search">
</form>
</body>
</html>
"""
    return render_template_string(html, result_message=result_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)