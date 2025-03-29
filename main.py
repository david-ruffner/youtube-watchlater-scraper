import argparse
from scraper import *

def export_to_csv():
    pass


def list_videos():
    pass


def main():
    parser = argparse.ArgumentParser(
        description="YouTube Watch Later Scraper"
    )

    subparsers = parser.add_subparsers(
        title="commands", dest="command", required=True
    )

    # scrape command
    scrape_parser = subparsers.add_parser("scrape", help="Scrape the Watch Later list")
    scrape_parser.add_argument(
        "--range",
        type=str,
        help="Specify range of videos to scrape, e.g. '1-50'"
    )

    # other commands
    subparsers.add_parser("export", help="Export scraped data to CSV")
    subparsers.add_parser("list", help="List scraped videos")

    args = parser.parse_args()

    if args.command == "scrape":
        scrape_watch_later()
    elif args.command == "export":
        export_to_csv()
    elif args.command == "list":
        list_videos()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()