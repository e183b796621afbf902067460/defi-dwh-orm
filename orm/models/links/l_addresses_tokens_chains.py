from sqlalchemy import Column, Integer, ForeignKey

from base.main import Base


class LinkAddressesTokensChains(Base):

    __tablename__ = 'l_addresses_tokens_chains'
    __table_args__ = {
        'comment': 'Token Contracts'
    }

    l_address_token_chain_id = Column(Integer, primary_key=True)  # PK
    l_address_chain_id = Column(Integer, ForeignKey('l_addresses_chains.l_address_chain_id'), nullable=False)
    h_token_id = Column(Integer, ForeignKey('h_tokens.h_token_id'), nullable=False)
