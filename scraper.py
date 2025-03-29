import json

from playwright_scraper import *
import csv

def scrape_watch_later():
    channels = {}

    with open("./watch-later.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        ids = [row[0] for row in reader]

    for id in ids:
        try:
            vidData = getVidInfo(id)
            channelName = vidData["channelName"]
            vidTitle = vidData["title"]

            if channelName not in channels:
                channels[channelName] = {}

            channels[channelName][vidTitle] = vidData
            print("Metadata For Video ${0} | ${1}".format(id, vidData))

            # Overwrite output.json with updated state
            with open("output.json", "w") as outfile:
                json.dump(channels, outfile, indent=2)

            print("Successfully added to output.json!")

        except Exception as e:
            with open("error.txt", "a") as outfile:
                outfile.write("Error trying to read video | ID: {0} "
                    "| Exception: {1}".format(id, e))

    print(channels)