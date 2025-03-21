#!/usr/bin/python3

import os

#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    """
    Generate invitation letters for attendees based on the template.
    """
    if not isinstance(template, str):
        raise TypeError("template must be a string")
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        raise TypeError("attendees must be a list of dictionaries")

    if not template:
        print("Template is empty, no output files generated.")
        return []
    if not attendees:
        print("No data provided, no output files generated.")
        return []

    generated_files = []

    for idx, attendee in enumerate(attendees, start=1):
        try:
            filled_template = template.format(
                name=attendee.get("name", "N/A"),
                event_title=attendee.get("event_title", "N/A"),
                event_date=attendee.get("event_date", "N/A"),
                event_location=attendee.get("event_location", "N/A")
            )

            file_name = f"output_{idx}.txt"

            if os.path.exists(file_name):
                print(f"File '{file_name}' already exists")
            else:
                with open(file_name, 'w') as file:
                    file.write(filled_template)
                generated_files.append(file_name)
                print(f"Generated file: {file_name}")

        except KeyError as e:
            print(f"Missing key in attendee data: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    return generated_files
