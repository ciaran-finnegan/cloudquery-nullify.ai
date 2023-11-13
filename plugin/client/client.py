from dataclasses import dataclass, field
from cloudquery.sdk.scheduler import Client as ClientABC

from plugin.counts.client import CountsClient

DEFAULT_CONCURRENCY = 100
DEFAULT_QUEUE_SIZE = 10000


@dataclass
class Spec:
    access_token: str
    base_url: str = field(default="https://api.mantelgroup.nullify.ai")
    github_owner_id: str = field(default="6890923")
    concurrency: int = field(default=DEFAULT_CONCURRENCY)
    queue_size: int = field(default=DEFAULT_QUEUE_SIZE)

    def validate(self):
        pass
        if self.access_token is None:
            raise Exception("access_token must be provided")


class Client(ClientABC):
    def __init__(self, spec: Spec) -> None:
        self._spec = spec
        self._client = CountsClient(spec.access_token, spec.github_owner_id, spec.base_url)

    def id(self):
        return "counts"

    @property
    def client(self) -> CountsClient:
        return self._client
