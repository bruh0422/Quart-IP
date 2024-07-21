from quart import Quart, render_template
import requests

app = Quart(__name__)

@app.route('/')
async def home():
    return await render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')