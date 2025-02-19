from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'The About Page'

@app.route('/blog')
def blog():
    return render_template('index.html')

@app.route('/blog/<blog_id>')
def blogpost(blog_id):
    return f'This is another post {blog_id}'




if __name__ == "__main__":
    app.run(debug=True)