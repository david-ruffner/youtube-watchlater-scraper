import json
from collections import OrderedDict

def convert_json_to_array(input_file, output_file):
    # Load the nested JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)

    # Flatten to array of videos, ordered by channel
    output_array = []
    for channel_name, videos in data.items():
        for video_title, video_data in videos.items():
            output_array.append(video_data)

    # Write the array to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_array, f, indent=2, ensure_ascii=False)

    print(f"Converted {len(output_array)} videos to array and saved to '{output_file}'.")

# Example usage:
convert_json_to_array('output_2.json', 'output_2_fixed.json')