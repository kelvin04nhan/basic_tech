# from flask import Flask
# app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return 'Hello, welcome to geeksforgeeks'


# @app.route('/post/<int:id>')
# def show_post(id):
#     #show the post with given id
#     return f"This post has id {id}"
# @app.route('/user/<username>') 
# def show_user(username): 
#     # Greet the user 
#     return f'Hello {username} !. Do you want to have a play with me'

# @app.route('/')
# def index():
#     return 'Homepage of geeksforgeeks'
# app.add_url_rule('/user/<username>','show_user', show_user)
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask

# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return '<h1>Hello</h1>, welcome you here Nhan'

# if __name__ == "__main__":
#     app.run(debug=True)
# import the Flask library
from flask import Flask, render_template, request
 
 
# Create the Flask instance and pass the Flask 
# constructor the path of the correct module
app = Flask(__name__)
 
# The URL  'localhost:5000/square' is mapped to
# view function 'squarenumber'
# The GET request will display the user to enter 
# a number (coming from squarenum.html page)
 
 
@app.route('/', methods=['GET'])
def squarenumber():
    # If method is GET, check if  number is entered 
    # or user has just requested the page.
    # Calculate the square of number and pass it to 
    # answermaths method
    if request.method == 'GET':
   # If 'num' is None, the user has requested page the first time
        if(request.args.get('num') == None):
            return render_template('squarenum.html')
          # If user clicks on Submit button without 
          # entering number display error
        elif(request.args.get('num') == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
          # User has entered a number
          # Fetch the number from args attribute of 
          # request accessing its 'id' from HTML
            number = request.args.get('num')
            sq = int(number) * int(number)
            # pass the result to the answer HTML
            # page using Jinja2 template
            return render_template('answer.html', 
                                   squareofnum=sq, num=number)
 
 
# Start with flask web app with debug as
# True only if this is the starting page
if(__name__ == "__main__"):
    app.run(debug=True)