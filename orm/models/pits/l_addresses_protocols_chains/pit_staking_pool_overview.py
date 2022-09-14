from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey, Text
from sqlalchemy.sql import func

from base.main import Base


class PITStakingPoolOverview(Base):

    __tablename__ = 'pit_staking_pool_overview'
    __table_args__ = {
        'comment': 'Staking Pool Overview'
    }

    pit_liquidity_pool_overview_id = Column(Integer, primary_key=True)  # PK
    l_address_protocol_chain_id = Column(Integer, ForeignKey('l_addresses_protocols_chains.l_address_protocol_chain_id'), nullable=False)
    pit_token_symbol = Column(Text, nullable=False)
    pit_token_reserve = Column(Float, nullable=False)
    pit_token_price = Column(Float, nullable=False)
    pit_staking_pool_overview_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
