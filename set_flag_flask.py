from flask import Flask, make_response

app = Flask(__name__)

@app.route('/set_flag')
def set_flag():
    # Create the response message
    message = "Flag cookie set. <a href='search.php'>Go to search</a>"
    
    # Create response and set cookie
    response = make_response(message)
    response.set_cookie(
        key='flag',
        value='flag{r3fl3ct3d_xss_pwn3d}',
        max_age=3600,  # Expires in 1 hour
        path='/'       # Available site-wide
    )
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)