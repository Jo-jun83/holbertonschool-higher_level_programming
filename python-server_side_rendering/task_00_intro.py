#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    """
    Generate invitation letters for attendees based on the template.
    """

    # Vérification des types d'entrée
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Nettoyage du template
    template = template.strip()
    
    # Gestion des entrées vides
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    generated_files = []

    for idx, attendee in enumerate(attendees, start=1):
        try:
            # Remplacement des valeurs, conversion explicite de None en "N/A"
            filled_template = template.format(
                name=attendee.get("name") or "N/A",
                event_title=attendee.get("event_title") or "N/A",
                event_date=attendee.get("event_date") or "N/A",
                event_location=attendee.get("event_location") or "N/A"
            )

            file_name = f"output_{idx}.txt"

            # Vérification de l'existence du fichier avant écriture
            if os.path.exists(file_name):
                print(f"File '{file_name}' already exists.")
            else:
                with open(file_name, 'w', encoding="utf-8") as file:
                    file.write(filled_template)
                generated_files.append(file_name)
                print(f"Generated file: {file_name}")

        except Exception as e:
            print(f"An error occurred while processing attendee {idx}: {e}")

    return generated_files
