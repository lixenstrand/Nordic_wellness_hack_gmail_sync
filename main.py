from datetime import datetime, timedelta
from gcsa.google_calendar import GoogleCalendar
import config

gc = GoogleCalendar(credentials_path='credentials/credentials.json')
calendar = GoogleCalendar(config.gmail_dit_du_syncar_passen_till, credentials_path='credentials/credentials.json')


def look_for_matching_event():
    for event in calendar.get_events(datetime.now(),
                                     datetime.now() + timedelta(days=config.antal_dagar_framåt_scriptet_ska_kolla)):
        if "wellness" in str(event.location).lower():

            update_reminders_for_event(event)


def update_reminders_for_event(event):
    #  print(event)
    event.add_popup_reminder(minutes_before_start=config.antal_timmar_innan_påminnelsen_ska_komma * 60)
    # event.add_email_reminder(minutes_before_start=config.antal_timmar_innan_påminnelsen_ska_komma * 60)
    updated_event = calendar.update_event(event)
    print(updated_event)


look_for_matching_event()
