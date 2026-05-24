import csv

def write_to_csv(listings: list[dict], output_path: str):
    """Write job listings to a CSV file."""

    print(f"Writing {len(listings)} listings to {output_path}")

    with open(output_path, mode="w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "source",
                "title",
                "company",
                "location",
                "link",
                "posted_at",
                "description",
                "tags"
            ]
        )

        writer.writeheader()

        print(f"First listing: {listings[0] if listings else 'None'}")

        writer.writerows(listings)