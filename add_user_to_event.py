from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime
from datetime import timedelta

user_email = 'antoha_zhirniy@gmail.com'
time_begin = '2018-12-27T05:00:00+01:00'
max_att = 10

time_end = time_begin[:11]
time_end += '23:59:00+01:00'

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # First retrieve the event from the API.
    events_result = service.events().list(calendarId='primary',
                                          timeMin=time_begin,  # Does include events ending till
                                          # this time(exclusive)
                                          timeMax='2018-12-27T22:00:00+01:00',  # Does include events
                                          # beginning till this time (exclusive)
                                          maxResults=20, singleEvents=True,
                                          orderBy='startTime').execute()

    events = events_result.get('items', [])

    if (len(events[0]['attendees']) < max_att):
        print('hey')


    #updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()


if __name__ == '__main__':
    main()
