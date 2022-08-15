from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from base.main import Base


class SatelliteLendingOverview(Base):

    __tablename__ = 's_lending_overview'
    __table_args__ = {
        'comment': 'Lending Overview'
    }

    s_lending_overview_id = Column(Integer, primary_key=True)  # PK
    l_address_abi_token_protocol_chain_id = Column(Integer, ForeignKey('l_addresses_abis_tokens_protocols_chains.l_address_abi_token_protocol_chain_id'), nullable=False)
    s_reserve_size = Column(Float, nullable=False)
    s_borrow_size = Column(Float, nullable=False)
    s_dex_overview_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
