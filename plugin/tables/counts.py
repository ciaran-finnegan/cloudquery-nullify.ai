from typing import Any, Generator
import uuid

import pyarrow as pa
from cloudquery.sdk.scheduler import TableResolver
from cloudquery.sdk.schema import Column
from cloudquery.sdk.schema import Table
from cloudquery.sdk.schema.resource import Resource

from plugin.client import Client


class Counts(Table):
    '''
    {
    "counts": {
        "critical": 0,
        "high": 0,
        "low": 0,
        "medium": 0,
        "unknown": 0
    }
}
    '''

    def __init__(self) -> None:
        super().__init__(
            name="example_item",
            title="Example Item",
            columns=[
                Column("_id", pa.uint64(), primary_key=True),
                Column("critical", pa.uint64()),
                Column("high", pa.uint64()),
                Column("low", pa.uint64()),
                Column("medium", pa.uint64()),
                Column("unknown", pa.uint64()),
                
            ],
        )

    @property
    def resolver(self):
        return CountsResolver(table=self)


class CountsResolver(TableResolver):
    def __init__(self, table) -> None:
        super().__init__(table=table)

    def resolve(
        self, client: Client, parent_resource: Resource
    ) -> Generator[Any, None, None]:
        for counts_response in client.client.item_iterator():
            yield counts_response
