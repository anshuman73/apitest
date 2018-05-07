"""
Making this for demonstration purposes.
My preferred method of running a wsgi app is through gunicorn cause scalability in python,
but let's keep this cause simpler.
I should learn golang for the multithreading support tbh, even got a freaking gopher sticker from that google session
"""

from apitest import app
import os

if __name__ == '__main__':
    app.debug = False
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)  # Remember to not use threaded for prod bois, check online why


# TODO: Find a way to import data from CSVs on program startup, but only once, as DB will then hold the values
