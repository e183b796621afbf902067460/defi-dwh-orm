from sqlalchemy import Column, Integer, Text, DateTime, Enum
from sqlalchemy.sql import func

from head.consts.protocols.const import Protocols
from base.main import Base


class HubProtocols(Base):

    __tablename__ = 'h_protocols'

    h_protocol_id = Column(Integer, primary_key=True)  # PK
    h_protocol_name = Column(Text, nullable=False)
    h_protocol_type = Column(Enum(Protocols), nullable=False)
    h_protocol_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
