import json

# Load the JSON data from the file
with open('output_2_fixed.json', 'r') as infile:
    data = json.load(infile)

# Extract all channel names from the list of channels
channel_names = [channel['channelName'] for channel in data]

# Write the channel names to a new file (channel_names.json)
with open('channel_names.json', 'w') as outfile:
    json.dump(channel_names, outfile, indent=2)

print("Channel names have been successfully extracted to channel_names.json")