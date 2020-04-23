import src.eventbrite
import src.places
import src.meetup
import src.ticket_master

def collect_all():
    eventbrite_events = src.eventbrite.get_events()
    meetup_events = src.meetup.get_meetups()
    foursquare_events = src.places.get_all_events()
    ticketmaster_events = src.ticket_master.get_all_events()

    return eventbrite_events + meetup_events + foursquare_events + ticketmaster_events
