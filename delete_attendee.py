from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

#event_id = '0m8psqpauuh7nfj9nmvqcrsi48'
#user_email = "eg.spdfffirin@gmail.com"

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


def delete_user(event_id, user_email):
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API

    event = service.events().get(calendarId='primary', eventId=event_id).execute()
    to_be_deleted = ''

    for attendee in event['attendees']:
        if (attendee['email'] == user_email):
            to_be_deleted = attendee
    print(to_be_deleted)
    try:
        event['attendees'].remove(to_be_deleted)
    except:
        print("User not found in the event attendees list")
    service.events().update(calendarId='primary', eventId=event_id, body=event).execute()



if __name__ == '__main__':
    delete_user('0m8psqpauuh7nfj9nmvqcrsi48', "eg.spdfffirin@gmail.com")