from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from base.main import Base


class SatelliteSupply(Base):

    __tablename__ = 's_supply'
    __table_args__ = {
        'comment': 'Token supplies'
    }

    s_supply_id = Column(Integer, primary_key=True)  # PK
    l_address_token_chain_id = Column(Integer, ForeignKey('l_addresses_tokens_chains.l_address_token_chain_id'), nullable=False)
    s_supply = Column(Float, nullable=False)
    s_supply_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
