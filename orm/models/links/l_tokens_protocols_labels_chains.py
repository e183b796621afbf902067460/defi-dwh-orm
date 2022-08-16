from sqlalchemy import Column, Integer, ForeignKey

from base.main import Base


class LinkTokensProtocolsLabelsChains(Base):

    __tablename__ = 'l_tokens_protocols_labels_chains'
    __table_args__ = {
        'comment': "Incentives from positions"
    }

    l_token_protocol_label_chain_id = Column(Integer, primary_key=True)  # PK
    l_address_abi_token_protocol_label_chain_id = Column(Integer, ForeignKey('l_addresses_abis_tokens_protocols_labels_chains.l_address_abi_token_protocol_label_chain_id'), nullable=False)
    h_token_id = Column(Integer, ForeignKey('h_tokens.h_token_id'), nullable=False)
