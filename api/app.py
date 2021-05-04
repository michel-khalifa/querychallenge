import connexion

app = connexion.App(__name__, specification_dir='')
app.add_api('swagger.yml')


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return "<h1>Hello MR</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
