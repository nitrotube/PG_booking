from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

#user_email = "eg.spirin@gmail.com"

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


def get_user_events(user_email):
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.utcnow().isoformat()[:19] + '+01:00'  # 'Z' indicates UTC time
    now_in_a_year = (datetime.utcnow() + timedelta(days=365)).isoformat()[:19] + '+01:00'
    events_result = service.events().list(calendarId='primary',
                                          timeMin= now,  # Does include events ending till
                                                                                # this time(exclusive)
                                          timeMax=now_in_a_year,  # Does include events
                                          #timeMin='2018-12-27T05:00:00+01:00',  # Does include events ending till

                                          #timeMax='2020-12-27T22:00:00+01:00',
                                                                                # beginning till this time (exclusive)
                                          maxResults=50, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    else:
        print(len(events))
    for event in events:
        try:
            for attendee in event['attendees']:
                if (attendee['email'] == user_email):
                    print(event['start']['dateTime'], event['end']['dateTime'], event['summary'], event['id'])
        except:
            pass

if __name__ == '__main__':
    get_user_events("eg.spirin@gmail.com")