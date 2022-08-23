from sqlalchemy import Column, Integer, ForeignKey, Text

from base.main import Base


class LinkAddressesProtocolsLabelsChains(Base):

    __tablename__ = 'l_addresses_protocols_labels_chains'
    __table_args__ = {
        'comment': "Positions in protocol's contracts"
    }

    l_address_protocol_label_chain_id = Column(Integer, primary_key=True)  # PK
    l_address_label_chain_id = Column(Integer, ForeignKey('l_addresses_labels_chains.l_address_label_chain_id'), nullable=False)
    l_address_protocol_chain_id = Column(Integer, ForeignKey('l_addresses_protocols_chains.l_address_protocol_chain_id'), nullable=False)
