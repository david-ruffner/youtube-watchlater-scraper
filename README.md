# Convert Your Youtube Watch Later List Into Usable JSON data

## Setup
    1. Go to Google Takeout and download your youtube watch later playlist data.
    You will receive a csv file that looks like the watch-later-example.csv file.
    You can also use that example file to start if you would just like to demo this program.

    2. Simply run python3 ./main.py scrape
    
    3. Let the script run for a while. It uses a headless browser to grab all of the information
    for each video, so that we don't run into any issues with rate limiters, or anti-bot detection.
    Any errors will be output to error.txt.

    4. Periodically check error.txt, because it's very possible at some point
    that my HTML selectors you'll see in playwright_scraper.py have become outdated.
    In that case you will probably need to change them yourself. This script is obviously un-finished, 
    but I won't be updating it in the near future.

    5. When it's all finished, your output will be in a file called output.json

### This was tested to work last on 3/29/25

## Other Considerations
    1. The docker-compose is there to spin up an instance of ELK (without the L)
    I will probably update this soon to include Logstash, and have it automatically ingest output.json.

### Huge Thank You to https://github.com/microsoft/playwright-python. If you're doing a similar project, use this instead of Selenium.
