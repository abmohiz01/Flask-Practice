from flask import render_template, request
@hello.route('/')
@hello.route('/hello')
def hello_world():
    user = request.args.get('user', 'AB mohiz')
    return render_template('index.html', user=user)