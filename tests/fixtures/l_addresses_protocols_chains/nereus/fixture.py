from head.consts.protocols.const import Protocols


FIXTURE = {
    'Lending Pool': {
        'l_address_protocol_chain_prefix': 'lending-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Nereus',
            'h_protocol_type': Protocols.LENDING
        },
        'h_chains': {
            'h_network_name': 'avax',
            'h_network_id': 5,
            'h_network_endpoint': 'avax.endpoint'
        },
        'h_addresses': '0xB9257597EDdfA0eCaff04FF216939FBc31AAC026'
    },
}
