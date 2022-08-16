from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from base.main import Base


class SatelliteIncentiveOverview(Base):

    __tablename__ = 's_incentive_overview'
    __table_args__ = {
        'comment': 'Incentive Overview'
    }

    s_incentive_overview_id = Column(Integer, primary_key=True)  # PK
    l_token_protocol_label_chain_id = Column(Integer, ForeignKey('l_tokens_protocols_labels_chains.l_token_protocol_label_chain_id'), nullable=False)
    s_reward_balance = Column(Float, nullable=False)
    s_incentive_overview_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
