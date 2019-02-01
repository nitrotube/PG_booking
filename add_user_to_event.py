from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

#user_email = 'antoha_zhirniy@gmail.com'
#event_id = '0m8psqpauuh7nfj9nmvqcrsi48'

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


def add_user(user_email, event_id):
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))


    event = service.events().get(calendarId='primary', eventId=event_id).execute()
    event['attendees'].append({'email': user_email})
    service.events().update(calendarId='primary', eventId=event_id, body=event).execute()


if __name__ == '__main__':
    add_user('antoha_zhirniy@gmail.com', '0m8psqpauuh7nfj9nmvqcrsi48')
