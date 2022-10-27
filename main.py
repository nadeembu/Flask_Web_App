# Import the create_app function from website init.py
from website import create_app

app = create_app()

# debug=True means every time we make a change to our python
# code it will automatically rerun the flask webserver.
if __name__ == '__main__':
    app.run(debug=True)
