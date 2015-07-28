#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import webapp2
import os
import urllib2
import json
from google.appengine.api import users
from google.appengine.ext import ndb
import logging
import datetime

# Handler for comment
# /login -> allow user to log in
class MainHandler(webapp2.RequestHandler):
    def get(self):
        entry = jinja2_environment.get_template('template/loginpage.html')
        self.response.write(entry.render())
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href= %s>Sign Out</a>)' % (user.nickname(),
            users.create_logout_url('/')))
                        #^ send user back to the original page after they log out
        else:
            greeting = ('<a href= "%s"> Sign in or Register </a>.' % users.create_login_url
            ('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)

# welcome page Handler
# its work

#associated with surveyhandler
class User(ndb.Model):
        username = ndb.StringProperty(required=True)
        useful= ndb.StringProperty(required=True)
        created_date = ndb.DateTimeProperty(required=True)

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        entry = jinja2_environment.get_template('template/welcome.html')
        self.response.write(entry.render(login_url=users.create_login_url('/login')))

class SurveyHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('hello world')
        template = jinja2_environment.get_template("template/yourthoughts.html")
        self.response.write(template.render())


    def post(self):
        username = self.request.get('username')
        useful = self.request.get('useful')
        current_date = datetime.datetime.now()
        username1 = User (username=username, useful=useful)
        username1.created_date = current_date

        username1.put()
        # self.response.write('<a href=/add_name>Record User</a>')

        template_vars={'username' : username}
        entry = jinja2_environment.get_template('template/yourthoughts.html')
        self.response.write(entry.render(template_vars))

class UserDataHandler(webapp2.RequestHandler):
    def get(self):
        query = Survey.query()
        user_data = query.fetch()
        template_vars = {'username':user_data}
        template = jinja_environment.get_template(
            'templates/yourthoughts.html')
        self.response.write(template.render(template_vars))

# class AddUserHandler(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_environment.get_template("templates/add_student.html")
#         self.response.write(template.render())

class NodeHandler(webapp2.RequestHandler):
    def get(self):


        url = ("http://randomword.setgetgo.com/get.php")
        string = urllib2.urlopen(url).read()
        # json.loads(string) returns a dictionary
        logging.info(">>>>>>>>>>" + string)
        word = string
        #bigdictionary = string


        #word = bigdictionary['word']
        print (word)
        # temp = Temperature(temperature = int(howhot), created = datetime.datetime.now(),
        #     latitude = float(lat), longitude = float(lon))
        # temp.put()

        template_vars = {'word' : word}
        template = jinja2_environment.get_template('template/nodes.html')
        self.response.write(template.render(template_vars))


        # set up tempalte_vars dictionary from html {{}}
        # template_vars = {'temperature' : howhot, 'form': form}
        # self.response.write(template.render(template_vars))


jinja2_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/login', MainHandler),
    ('/survey', SurveyHandler),
    ('/nodes', NodeHandler),
    ('/survey', SurveyHandler),
    ('/nodes', NodeHandler)
], debug=True)
