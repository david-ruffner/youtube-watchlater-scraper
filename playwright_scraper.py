import string

from playwright.sync_api import sync_playwright

def getVidInfo(videoID):
    with sync_playwright() as p:
        # Launch a headless browser (default is headless=True)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        video_url = "https://www.youtube.com/watch?v={0}".format(videoID)
        print(f"🌐 Navigating to {video_url}...")
        page.goto(video_url, wait_until="load", timeout=30000)

        page.wait_for_selector("#title h1 yt-formatted-string", timeout=30000)

        # Evaluate metadata from the page
        metadata = page.evaluate("""
            () => {
                const videoId = new URLSearchParams(window.location.search).get('v');

                const title = document.querySelector("#title h1 yt-formatted-string")?.textContent.trim();

                const channelName = document.querySelector('ytd-channel-name a')?.textContent.trim();

                const description = (() => {
                    const desc = document.querySelector('ytd-video-secondary-info-renderer #description')
                              || document.querySelector('ytd-watch-metadata #description');
                    if (!desc) return null;
                    return Array.from(desc.querySelectorAll('span'))
                        .map(span => span.textContent.trim())
                        .filter(Boolean)
                        .join('\\n')
                        .trim();
                })();

                const uploadDate = (() => {
                    const el = document.querySelector('ytd-video-primary-info-renderer #info-strings yt-formatted-string')
                             || document.querySelector('ytd-watch-metadata #info-strings yt-formatted-string');
                    return el?.textContent.trim() || null;
                })();

                return { videoId, title, channelName, description, uploadDate };
            }
        """)

        print("🎥 Extracted Metadata:")
        # for key, value in metadata.items():
        #     print(f"{key}: {value}")

        browser.close()

        return metadata