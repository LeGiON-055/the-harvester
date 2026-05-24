def dedupe(listings: list[dict]) -> list[dict]:
    """Remove duplicate job listings."""
    
    seen = set()
    unique_listings = []

    for listing in listings:
        key = (
            listing.get("title", "").lower(),
            listing.get("company", "").lower()
        )

        if key not in seen:
            seen.add(key)
            unique_listings.append(listing)

    return unique_listings


def filter_by_role(listings: list[dict], role: str) -> list[dict]:
    """Filter listings by role keywords."""

    role_keywords = role.lower().split()

    filtered = []

    for listing in listings:
        title = listing.get("title", "").lower()
        tags = " ".join(listing.get("tags", [])).lower()

        text = title + " " + tags

        if any(keyword in text for keyword in role_keywords):
            filtered.append(listing)

    return filtered


def filter_by_location(listings: list[dict], location: str) -> list[dict]:
    """Filter listings by location."""

    location = location.lower()

    filtered = []

    for listing in listings:
        listing_location = listing.get("location", "").lower()

        # Keep remote or empty locations too
        if (
            location in listing_location or
            "remote" in listing_location or
            listing_location == ""
        ):
            filtered.append(listing)

    return filtered