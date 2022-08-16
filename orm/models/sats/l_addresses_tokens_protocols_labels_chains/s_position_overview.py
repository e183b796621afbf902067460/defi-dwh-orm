from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from base.main import Base


class SatellitePositionOverview(Base):

    __tablename__ = 's_position_overview'
    __table_args__ = {
        'comment': 'Position Overview'
    }

    s_position_overview_id = Column(Integer, primary_key=True)  # PK
    l_address_token_protocol_label_chain_id = Column(Integer, ForeignKey('l_addresses_tokens_protocols_labels_chains.l_address_token_protocol_label_chain_id'), nullable=False)
    s_lp_balance = Column(Float, nullable=False)
    s_lp_total_supply = Column(Float, nullable=False)
    s_position_overview_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
