#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("template must be a string")
    if not isinstance(attendees, list):
        raise TypeError("attendees must be a list of dictionaries")
    if not template:
        raise Exception("Template is empty")
    if not attendees:
        raise Exception("Data is empty")
        
    for idx, attendee in enumerate(attendees, start=1):
        template_cpy = template.replace("name", attendee.get("name", "N/A"))
        template_cpy = template_cpy.replace("event_title", attendee.get("event_title", "N/A"))
        template_cpy = template_cpy.replace("event_date", attendee.get("event_date", "N/A") or "N/A")
        template_cpy = template_cpy.replace("event_location", attendee.get("event_location", "N/A") or "N/A")

        file_name = f"output_{idx}.txt"

        try:
            with open(file_name, 'w') as file:
                file.write(template_cpy)
        except Exception as e:
            print(f"Error writing to {file_name}: {e}")

