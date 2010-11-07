import logging
from lamson.routing import route, route_like, stateless
from config.settings import relay
from lamson import view

#######
import sys
sys.path.append("..")
sys.path.append("../../gdata-2.0.5/src")
import simplifiedCalendarExample
#######


@route("(address)@(host)", address=".+")
def START(message, address=None, host=None):
  
  content_string = "Subject: " + message['Subject']
  content_string += "\r\n" + message.body()
  
  sample = simplifiedCalendarExample.CalendarExample("REPLACEME", "REPLACEME")
  sample._InsertQuickAddEvent(content_string, message['Subject'])

  return
