import os

def generate_invitations(template, attendees):

    # Check if the template is a string
    if not isinstance(template, str):
        return ("Template must be a string")

    # Check if the attendees is a list of dictionaries
    if not isinstance(attendees, list) or \
            not all(isinstance(a, dict) for a in attendees):
        return ("Attendees must be a list of dictionaries")


    # Check if the template is empty
    if not template:
        return ("Error: Template is empty, no output files generated.")


    # Check if the attendees list is empty
    if not attendees:
        return ("No data provided, no output files generated.")

    # Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or "N/A" if missing
        invitation = template.format(
            name=attendee.get("name", "N/A") or "N/A",
            event_title=attendee.get("event_title", "N/A") or "N/A",
            event_date=attendee.get("event_date", "N/A") or "N/A",
            event_location=attendee.get("event_location", "N/A") or "N/A"
        )

        # Define the output file name
        filename = "output_{}.txt".format(index)
        with open(filename, 'w') as file:
            file.write(invitation)

        # Write the personalized invitation to the output file
        print("Generated invitation for {} in {}".format(attendee.get('name', 'N/A'), filename))
