from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

place_id = 'C1'  # Assign chair ID to booking
booking_id = 'nest44o70rafpiti9c28j24beo'

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
    event = service.events().get(calendarId='primary', eventId=booking_id).execute()

    event['location'] = place_id

    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()


if __name__ == '__main__':
    main()
