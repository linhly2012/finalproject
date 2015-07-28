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
                greeting = ('Welcome, %s! (<a href= %s> sign out</a>)' % (user.nickname(),
                users.create_logout_url('/')))
                            #^ send user back toc the original page after they log out
        else:
            greeting = ('<a href= "%s"> Sign in or Register </a>.' % users.create_login_url
            ('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)

# welcome page Handler
# its work
class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        entry = jinja2_environment.get_template('template/welcome.html')
        self.response.write(entry.render())

class NodeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('template/nodes.html')
        self.response.write(template.render())


jinja2_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/login', MainHandler),
    ('/nodes', NodeHandler)
], debug=True)
