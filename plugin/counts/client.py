from typing import Generator, Dict, Any


class CountsClient:
    def __init__(self, access_token, githubOwnerId, base_url):
        self._access_token = access_token
        self._base_url = base_url
        self._github_owner_id = github_owner_id

    def counts_iterator(self, page: int = 1) -> Generator[Dict[str, Any], None, None]:
        console.log("Debug: Calling API)
        console.log(f"Debug: URL: {urljoin(self._base_url, '/sca/counts/severity/latest')}")
        console.log(f"Debug: Params: {{'githubOwnerId': self._github_owner_id}}")

        response = requests.get(urljoin(self._base_url, "/sca/counts/severity/latest"), params={"githubOwnerId": self._github_owner_id}, headers={"Authorization": f"Bearer {self._access_token}"})
        if response.status_code != 200:
            raise ValueError("Bad HTTP Response")
        data = response.json()
        # Add a unique ID to the 'counts' object
        data['counts']['id'] = str(uuid.uuid4())


        console.log("Debug: Response with ID: ")
        console.log(data)    
        yield data
