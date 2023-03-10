import time
from datetime import datetime, timedelta
from gcsa.google_calendar import GoogleCalendar
import config

gc = GoogleCalendar(credentials_path='credentials/credentials.json')
calendar = GoogleCalendar(config.gmail_you_want_to_check_the_calender, credentials_path='credentials/credentials.json')


def look_for_matching_event():
    for event in calendar.get_events(datetime.now(),
                                     datetime.now() + timedelta(days=config.amount_of_days_forward_you_want_the_calender_to_check)):
        if "wellness" in str(event.location).lower():
            if "PopupReminder - minutes_before_start:300" in str(event.reminders):
                print("Påminnelsen är redan satt")
            else:
                print("Påminnelsen är inte satt, sätter påminnelsen")
                update_reminders_for_event(event)


def update_reminders_for_event(event):
    #  print(event)
    event.add_popup_reminder(minutes_before_start=config.amount_of_hours_before_reminder_comes * 60)
    # event.add_email_reminder(minutes_before_start=config.antal_timmar_innan_påminnelsen_ska_komma * 60)
    updated_event = calendar.update_event(event)
    print(updated_event)

while True:
    look_for_matching_event()
    time.sleep(300) # scriptet körs 1 gång var 5 minut