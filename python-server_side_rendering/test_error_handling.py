from task_00_intro import generate_invitations

print("Test 1: Invalid template type")
generate_invitations(123, [{"name": "Alice"}])

print("\nTest 2: Invalid attendees type")
generate_invitations("Template", "not_a_list")

print("\nTest 3: Empty template")
generate_invitations("", [{"name": "Alice"}])

print("\nTest 4: Empty attendees list")
generate_invitations("Template", [])

print("\nTest 5: Valid inputs with missing data")
attendees_missing_data = [
    {"name": "Alice", "event_title": "Conference"},  # Missing date and location
    {"event_date": "2023-07-15"}  # Missing name, title, and location
]
generate_invitations("Hello {name}, Event: {event_title} on {event_date} at {event_location}", attendees_missing_data)

print("\nTest complete - Check output files for Test 5")
