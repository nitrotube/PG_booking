from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

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

    for i in range(6, 22):
        event = {
            'summary': 'Test_event' + str(i),
            'location': 'PionierGarage, Karlsruhe, Germany',
            'description': 'Going to be fun',
            'start': {
                'dateTime': '2019-02-28T' + str(i) + ':00:00+01:00',  # Don't touch the given + values (What happens in summer?)
                'timeZone': 'Europe/Berlin',
            },
            'end': {
                'dateTime': '2019-02-28T' + str(i+1) + ':00:00+01:00',
                'timeZone': 'Europe/Berlin',
            },
            'attendees': [
                {'email': 'eg.spirin@gmail.com'},
                {'email': 'eg.spdfirin@gmail.com'},
                {'email': 'eg.spdffsfirin@gmail.com'},
                {'email': 'eg.spdfffirin@gmail.com'},
                {'email': 'eg.spdfisdfsvrin@gmail.com'},
            ],

        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        print(event.get('id'))

if __name__ == '__main__':
    main()