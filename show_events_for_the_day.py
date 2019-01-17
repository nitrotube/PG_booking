from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
time_begin = '2019-02-28T00:00:00+01:00'
time_end = '2019-02-28T23:59:00+01:00'

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

    # Call the Calendar API
    events_result = service.events().list(calendarId='primary',
                                          timeMin=time_begin,  # Does include events ending till
                                                                                # this time(exclusive)
                                          timeMax=time_end,  # Does include events

                                          maxResults=50, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        try:
            print(event['start']['dateTime'][11:][:5], event['summary'], '   Attending: ', len(events[0]['attendees']))
        except:
            pass

if __name__ == '__main__':
    main()