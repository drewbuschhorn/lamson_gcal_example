Simple example of setting up a LamsonProject.org server.
===

Full details at:
---
[Making your webapp react to emails](http://verpa.wordpress.com/2010/11/13/making-your-webapp-react-to-emails-with-lamson-pt-1)

Quick setup commands:
---
0. Follow Lamson's creator Zed Shaw's 30 second install guide ( setup notes in blog post ).
[http://lamsonproject.org/docs/getting_started.html](http://lamsonproject.org/docs/getting_started.html)
    $ easy_install lamson
    $ lamson gen -project mymailserver
    $ cd mymailserver
    $ lamson start
    $ lamson log
    $ nosetests
    $ lamson help -for send
    $ lamson send -sender me@mydomain.com -to test@test.com -subject “My test.” -body “Hi there.” -port 8823
    $ less logs/lamson.log
    $ mutt -F muttrc

1. Create a containing folder.

2. Into the containing folder, download and extract Google GData library:
[gdata-2.0.5.tar.gz](http://code.google.com/p/gdata-python-client/downloads/detail?name=gdata-2.0.5.tar.gz)
and clone this github repo:
`git clone https://github.com/drewbuschhorn/lamson_gcal_example.git`

3.  Edit lamson_gcal_example/simplifiedCalendarExample.py and replace 'REPLACEME' with GCal credentials.

4.  Navigate to lamson_gcal_example/mymailserver and run:
`lamson start`

5.  Run this command to create a entry on your calendar:
`lamson send -sender me@localhost -to me@localhost -subject "My test." -body "Hi there. Let's meet from 7pm until 9pm. Does that sound good?" -port 8823`

6.  Check your error logs for any issues:
`tail logs/lamson*`

