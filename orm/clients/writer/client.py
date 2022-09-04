from sqlalchemy.engine.cursor import CursorResult

from head.interfaces.clients.db.client import IClient


class DBWriterClient(IClient):

    def execute(self, query: str, *args, **kwargs) -> CursorResult:  # None
        return self.engine.execute(statement=query)
