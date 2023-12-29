from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index_page():
    return render_template('index.html')

#@app.route('/resources')
#def resources_page():
#    return render_template('resources.html')

#@app.route('/glossary')
#def glossary_page():
#    return render_template('glossary.html')

#@app.route('/newsletter')
#def newsletter_page():
#    return render_template('newsletter.html')

#@app.route('/about')
#def about_page():
#    return render_template('about.html')

#@app.route('/contact')
#def contact_page():
#    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9090, debug=True)