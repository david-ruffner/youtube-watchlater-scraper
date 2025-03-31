import json
from collections import OrderedDict


def convert_json_to_grouped_array(input_file, output_file):
    # Load the nested JSON file while preserving channel order
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)

    # Create an array that groups videos by channel
    grouped_array = []
    for channel_name, videos in data.items():
        # Collect all video objects for this channel
        video_list = []
        for video_title, video_data in videos.items():
            video_list.append(video_data)

        # Append the channel object with its videos
        grouped_array.append({
            "channelName": channel_name,
            "videos": video_list
        })

    # Write the grouped array to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(grouped_array, f, indent=2, ensure_ascii=False)

    print(f"Processed {len(grouped_array)} channels. Output saved to '{output_file}'.")


# Example usage:
convert_json_to_grouped_array('output_2.json', 'output_2_fixed.json')