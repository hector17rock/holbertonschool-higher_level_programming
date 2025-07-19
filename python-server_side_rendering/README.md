# Python Server Side Rendering - Task 0: Simple Templating Program

## Overview
This project implements a simple templating system in Python that generates personalized invitation files from a template with placeholders and a list of attendee objects.

## Files
- `task_00_intro.py`: Contains the main `generate_invitations` function
- `template.txt`: Template file with placeholders for invitation content
- `main.py`: Example usage of the templating function
- `test_error_handling.py`: Tests for error handling scenarios

## Features
- **Template Processing**: Replaces placeholders `{name}`, `{event_title}`, `{event_date}`, and `{event_location}` with actual values
- **Error Handling**: Validates input types and handles empty inputs gracefully
- **Missing Data Handling**: Replaces missing or `None` values with "N/A"
- **Sequential Output**: Creates numbered output files (`output_1.txt`, `output_2.txt`, etc.)

## Usage
```python
from task_00_intro import generate_invitations

# Read template
with open('template.txt', 'r') as file:
    template_content = file.read()

# Define attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"}
]

# Generate invitations
generate_invitations(template_content, attendees)
```

## Error Handling
- **Invalid Input Types**: Validates that template is a string and attendees is a list of dictionaries
- **Empty Template**: Logs error and terminates if template is empty
- **Empty Attendees**: Logs error and terminates if attendees list is empty
- **Missing Data**: Replaces missing values with "N/A" in output

## Testing
Run the test files to verify functionality:
```bash
python main.py
python test_error_handling.py
```

## Author
Hector
