from sqlalchemy import Column, Integer, ForeignKey, Text

from base.main import Base


class LinkAddressesAbisTokensProtocolsChains(Base):

    __tablename__ = 'l_addresses_abis_tokens_protocols_chains'
    __table_args__ = {
        'comment': "Protocol's contracts"
    }

    l_address_abi_token_protocol_chain_id = Column(Integer, primary_key=True)  # PK
    l_protocol_chain_id = Column(Integer, ForeignKey('l_protocols_chains.l_protocol_chain_id'), nullable=False)
    l_address_abi_chain_id = Column(Integer, ForeignKey('l_addresses_abis_chains.l_address_abi_chain_id'), nullable=False)
    l_address_abi_token_chain_id = Column(Integer, ForeignKey('l_addresses_abis_tokens_chains.l_address_abi_token_chain_id'))

    l_address_abi_token_protocol_chain_pool = Column(Text, nullable=False)
