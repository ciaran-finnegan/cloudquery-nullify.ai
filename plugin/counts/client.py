from typing import Generator, Dict, Any
from urllib.parse import urljoin
import uuid
import requests

class CountsClient:
    def __init__(self, access_token, github_owner_id, base_url):
        self._access_token = access_token
        self._base_url = base_url
        self._github_owner_id = github_owner_id

    def counts_iterator(self, page: int = 1) -> Generator[Dict[str, Any], None, None]:
        # Construct the full URL
        full_url = urljoin(self._base_url, "/sca/counts/severity/latest")
        print(f"Debug: URL: {full_url}")

        # Make the request
        response = requests.get(full_url, params={"githubOwnerId": self._github_owner_id}, headers={"Authorization": f"Bearer {self._access_token}"})

        # Print request details for debugging
        print("Debug: Request Headers:", response.request.headers)
        # Print the full request URL (including params)
        print("Debug: Full Request URL:", response.url)

        # Print response details
        print("Debug: Response Status Code:", response.status_code)
        print("Debug: Response Headers:", response.headers)
        print("Debug: Response Body:", response.json())

        if response.status_code != 200:
            raise ValueError("Bad HTTP Response")
        data = response.json()
        # Add a unique ID to the 'counts' object
        data['counts']['id'] = str(uuid.uuid4())

        print("Debug: Response with ID:")
        print(data)    
        yield data
