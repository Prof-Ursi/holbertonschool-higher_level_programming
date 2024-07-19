import os

def generate_invitations(template, attendees):

    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: The template should be a string.")
        return

    # Check if the attendees is a list of dictionaries
    if not isinstance(attendees, list) or \
            not all(isinstance(a, dict) for a in attendees):
        return ("Attendees must be a list of dictionaries")


    # Check if the template is empty
    if not template:
        print("Error: Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for this attendee
        personalized_invitation = template[:]

        # Replace placeholders with actual values or "N/A" if missing
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        personalized_invitation = personalized_invitation.replace("{name}", name)
        personalized_invitation = personalized_invitation.replace("{event_title}", event_title)
        personalized_invitation = personalized_invitation.replace("{event_date}", event_date)
        personalized_invitation = personalized_invitation.replace("{event_location}", event_location)

        # Define the output file name
        output_file_name = f"output_{index + 1}.txt"

        # Write the personalized invitation to the output file
        try:
            with open(output_file_name, 'w') as output_file:
                output_file.write(personalized_invitation)
            print(f"Generated file: {output_file_name}")
        except Exception as e:
            print(f"Error writing to file {output_file_name}: {e}")

    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

