from head.consts.protocols.const import Protocols


FIXTURE = {
    'Lending Pool': {
        'l_address_protocol_chain_prefix': 'lending-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Geist',
            'h_protocol_type': Protocols.LENDING
        },
        'h_chains': {
            'h_network_name': 'ftm',
            'h_network_id': 4,
            'h_network_endpoint': 'ftm.endpoint'
        },
        'h_addresses': '0x9FAD24f572045c7869117160A571B2e50b10d068'
    },
}
