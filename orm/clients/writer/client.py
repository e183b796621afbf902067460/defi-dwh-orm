from sqlalchemy.engine.cursor import CursorResult

from head.interfaces.clients.db.client import IClient
from head.decorators.singleton import singleton


@singleton
class DBWriterClient(IClient):

    def execute(self, query: str, *args, **kwargs) -> CursorResult:  # None
        return self.engine.execute(statement=query)
