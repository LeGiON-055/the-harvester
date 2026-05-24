import time
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from .base import BoardAdapter

class Naukri(BoardAdapter):
    """Adapter for Naukri.com job board."""
    
    def fetch(self, role: str, location: str) -> List[Dict]:
        """Fetch job listings from Naukri.
        
        Args:
            role: Job role to search for
            location: Location to search in
            
        Returns:
            List of job listings in standardized format
        """
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/91.0.4472.124 Safari/537.36"
            }
            
            # Construct search URL
            url = f"https://www.naukri.com/{role.replace(' ', '-')}-jobs-in-{location.replace(' ', '-')}"
            
            # Make request with delay
            response = requests.get(url, headers=headers)
            time.sleep(1)  # Be polite with delay
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.text, "html.parser")
            jobs = soup.find_all("article", class_="jobTuple")
            print(f"Found {len(jobs)} jobs on Naukri")
            
            # Standardize results
            listings = []
            for job in jobs:
                try:
                    listings.append({
                        "source": "Naukri",
                        "title": job.find("a", class_="title").text.strip(),
                        "company": job.find("a", class_="subTitle").text.strip(),
                        "location": job.find("li", class_="location").text.strip(),
                        "link": job.find("a", class_="title")["href"],
                        "posted_at": job.find("span", class_="postedDate").text.strip(),
                        "description": job.find("div", class_="job-description").text.strip()
                    })
                except Exception as e:
                    print(f"Error parsing job: {e}")
            
            return listings
            
        except Exception as e:
            print(f"Error fetching from Naukri: {e}")
            return []