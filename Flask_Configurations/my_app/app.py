from flask import Flask

app = Flask(__name__, instance_path=r'D:\Flask_Preparation\Flask_Practice\Flask_Configurations\my_app\instance',
            instance_relative_config=True)

app.config.from_pyfile('myconfig.cfg', silent=True)


# app.config.from_object('config.TestingConfig')
print(app.config['SECRET_KEY'])

'''Making Cnfigurations in the app file'''
# app.config['SECRET_KEY'] = 'defcasdcaac'
# print(app.config['SECRET_KEY'])
#
# app.config['DB_USERNAME'] = 'root'
# print(f"The Username of database is :{app.config['DB_USERNAME']}")
#
# app.config['PASSWORD'] = 'root1'
# print(f"The Password of this app is: {app.config['PASSWORD']}")
#
# app.config['DEBUG'] = True





# This is a decorator, which modifies the function that follows it (`hello_world()`).
# The `@app.route('/')` decorator means that
# this function will be run when the root URL of the application ('/') is accessed.

@app.route('/')
def hello_world():


    return 'Hello to the World of Flask!'

if __name__ == '__main__':
    app.run()
