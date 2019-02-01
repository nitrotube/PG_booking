from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

time_begin = '2019-02-28T00:00:00+01:00'
time_end = '2019-02-28T23:59:00+01:00'
user_email = "eg.spirin@gmail.com"

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


def main():
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
            user_found = False
            for attendee in event['attendees']:
                if attendee['email'] == user_email:
                    user_found = True
            if not(user_found):
                print(event['start']['dateTime'][11:][:5], event['summary'], '   Attending: ', len(event['attendees']),
                      event['id'])
        except:
            pass

if __name__ == '__main__':
    main()