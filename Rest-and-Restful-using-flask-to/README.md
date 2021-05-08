# Learning how to make a API
 Api_old_flask.py
  uses the old way to do a api, using @route.test
  the old if methods=='get','post','put':
    @app.route('/'):
        if request.method=='GET':
          pass
        elif request.method=='PUT':
        elif request.method=='DELETE':
        
# app_restful.py
  this time using the class from flask_restful library; Flask-RESTful==0.3.8
  so we just need to create a class and pass the methods get, post and put as args on class paramenter ()
    like;
      class NewClass(Resource):
        def get(self):
          pass
        def post(self):
          pass
        def delete(self):
          pass
