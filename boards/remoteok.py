import requests
from typing import List, Dict
from .base import BoardAdapter

class RemoteOK(BoardAdapter):
    """Adapter for RemoteOK job board."""
    
    def fetch(self, role: str, location: str) -> List[Dict]:
        """Fetch job listings from RemoteOK API.
        
        Args:
            role: Job role to search for
            location: Location to search in
            
        Returns:
            List of job listings in standardized format
        """
        try:
            # RemoteOK API endpoint
            url = "https://remoteok.com/api"
            
            # Make API request
            response = requests.get(url)
            response.raise_for_status()
            
            # Parse and filter results
            raw_jobs = response.json()
            print(f"Raw API response contains {len(raw_jobs)} entries")
            listings = []
            
            for job in raw_jobs[1:]:
                if not job.get("position"):
                    continue
                if isinstance(job, dict):  # Skip metadata entries
                    try:
                        listings.append({
                            "source": "remoteok",
                            "title": job.get("position", ""),
                            "company": job.get("company", ""),
                            "location": job.get("location", ""),
                            "link": job.get("url", ""),
                            "posted_at": job.get("date", ""),
                            "description": job.get("description", ""),
                            "tags": job.get("tags", [])
                        })
                    except Exception as e:
                        print(f"Error parsing job: {e}")
            
            # Return all listings for testing
            print(f"Returning {len(listings)} jobs")
            
            return listings
            
        except Exception as e:
            print(f"Error fetching from RemoteOK: {e}")
            return []