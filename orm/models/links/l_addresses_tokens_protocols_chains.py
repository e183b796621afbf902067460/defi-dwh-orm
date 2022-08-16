from sqlalchemy import Column, Integer, ForeignKey, Text

from base.main import Base


class LinkAddressesTokensProtocolsChains(Base):

    __tablename__ = 'l_addresses_tokens_protocols_chains'
    __table_args__ = {
        'comment': "Protocol's contracts"
    }

    l_address_token_protocol_chain_id = Column(Integer, primary_key=True)  # PK
    l_protocol_chain_id = Column(Integer, ForeignKey('l_protocols_chains.l_protocol_chain_id'), nullable=False)
    l_address_chain_id = Column(Integer, ForeignKey('l_addresses_chains.l_address_chain_id'), nullable=False)
    l_address_token_chain_id = Column(Integer, ForeignKey('l_addresses_tokens_chains.l_address_token_chain_id'))

    l_address_token_protocol_chain_pool = Column(Text, nullable=False)
