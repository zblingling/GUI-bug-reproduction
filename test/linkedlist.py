import json

linked_list = [
    {"screenshot": "state1.jpg", "type": "Trackball", "action": "ACTION_MOVE"},
    {"screenshot": "state2.jpg", "type": "Touch", "action": "ACTION_UP"},
    {"screenshot": "state2.jpg", "type": "Flip", "action": "ACTION_DOWN"},
]

# Specify the file path
json_file_path = "linked_list_data.json"

# Dump the data to JSON file
with open(json_file_path, "w") as json_file:
    json.dump(linked_list, json_file, indent=2)

print(f"Data dumped to {json_file_path}")
