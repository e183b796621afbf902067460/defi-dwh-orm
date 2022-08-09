from sqlalchemy import Column, Integer, ForeignKey

from base.main import Base


class LinkProtocolsChains(Base):

    __tablename__ = 'l_protocols_chains'
    __table_args__ = {
        'comment': "Chain's Protocols"
    }

    l_protocol_chain_id = Column(Integer, primary_key=True)  # PK
    h_protocol_id = Column(Integer, ForeignKey('h_protocols.h_protocol_id'), nullable=False)
    h_chain_id = Column(Integer, ForeignKey('h_chains.h_chain_id'), nullable=False)
