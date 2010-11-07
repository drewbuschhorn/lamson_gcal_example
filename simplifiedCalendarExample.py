#!/usr/bin/python
#
# Copyright (C) 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Modified db at Nov. 06, 2010

__author__ = 'api.rboyd@gmail.com (Ryan Boyd)'

import sys
import os
sys.path.append(os.getcwd()+"/../gdata-2.0.5/src")

try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar
import atom
import getopt
import string
import time

class CalendarExample:

  def __init__(self, email, password):
    """Creates a CalendarService and provides ClientLogin auth details to it.
    The email and password are required arguments for ClientLogin.  The 
    CalendarService automatically sets the service to be 'cl', as is 
    appropriate for calendar.  The 'source' defined below is an arbitrary 
    string, but should be used to reference your name or the name of your
    organization, the app name and version, with '-' between each of the three
    values.  The account_type is specified to authenticate either 
    Google Accounts or Google Apps accounts.  See gdata.service or 
    http://code.google.com/apis/accounts/AuthForInstalledApps.html for more
    info on ClientLogin.  NOTE: ClientLogin should only be used for installed 
    applications and not for multi-user web applications."""

    self.cal_client = gdata.calendar.service.CalendarService()
    self.cal_client.email = email
    self.cal_client.password = password
    self.cal_client.source = 'dbmod_Google-Calendar_Python_Sample-1.0'
    self.cal_client.ProgrammaticLogin()

  def _InsertQuickAddEvent(self, 
      content="Tennis with John today ... 3pm-3:30pm ... ok?", title=None):
    """Creates an event with the quick_add property set to true so the content
    is processed as quick add content instead of as an event description."""
    event = gdata.calendar.CalendarEventEntry()
    event.content = atom.Content(text=content)
    event.quick_add = gdata.calendar.QuickAdd(value='true');

    new_event = self.cal_client.InsertEvent(event, 
        '/calendar/feeds/default/private/full')
    
    if title:
      new_event.quick_add = gdata.calendar.QuickAdd(value='false');
      new_event.title = atom.Title(text=title)
      new_event.content = atom.Content(text=content)
      self.cal_client.UpdateEvent(new_event.GetEditLink().href, new_event)
      
    return new_event

if __name__ == '__main__':

  sample = CalendarExample("REPLACEME", "REPLACEME")
  sample._InsertQuickAddEvent()
