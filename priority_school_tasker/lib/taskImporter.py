from canvasapi import Canvas
import requests

# Canvas API URL
API_URL = "https://famu-fsu-eng.instructure.com"

# Canvas API key **** Will be unique per user
API_KEY = "12564~DnjktTW4xXJC6LPoU1S398ZaVZy4qJD9e2hVoes3tMjLks03JvrJZ91r1PkHMlBb"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#Pulls id for current user
currentUser = canvas.get_current_user()

#Pulls upcoming events
upComingEvents = requests.get(API_URL + "/api/v1/calendar_events?access_token=" + API_KEY)





