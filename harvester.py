# Main script for The Harvester
import argparse
from boards import Naukri, RemoteOK
from filters import dedupe, filter_by_role, filter_by_location
from writers import write_to_csv

def main():
    parser = argparse.ArgumentParser(description="Job listing harvester")
    parser.add_argument("--role", help="Job role to search for", required=True)
    parser.add_argument("--location", help="Location to search in", required=True)
    parser.add_argument("--output", help="Output file path", required=True)
    args = parser.parse_args()

    # Fetch listings from implemented boards
    listings = []
    for adapter in [Naukri(), RemoteOK()]:  # Wellfound not implemented yet
        listings.extend(adapter.fetch(args.role, args.location))

    print(f"Raw listings count: {len(listings)}")

    listings = filter_by_role(listings, args.role)
    print(f"After role filter: {len(listings)}")

    # listings = filter_by_location(listings, args.location)
    # print(f"After location filter: {len(listings)}")

    listings = dedupe(listings)
    print(f"After dedupe: {len(listings)}")

    # Write to CSV
    write_to_csv(listings, args.output)

if __name__ == "__main__":
    main()