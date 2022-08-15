from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from base.main import Base


class SatellitePrices(Base):

    __tablename__ = 's_price'
    __table_args__ = {
        'comment': 'Token prices'
    }

    s_price_id = Column(Integer, primary_key=True)  # PK
    h_token_id = Column(Integer, ForeignKey('h_tokens.h_token_id'), nullable=False)
    s_price = Column(Float, nullable=False)
    s_price_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
