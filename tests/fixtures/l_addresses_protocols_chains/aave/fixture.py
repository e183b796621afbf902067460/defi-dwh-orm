from head.consts.protocols.const import Protocols


FIXTURE = {
    'Lending Pool': {
        'l_address_protocol_chain_prefix': 'lending-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Aave',
            'h_protocol_type': Protocols.LENDING
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9'
    },
}
