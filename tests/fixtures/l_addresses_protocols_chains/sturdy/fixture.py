from head.consts.protocols.const import Protocols


FIXTURE = {
    'Lending Pool': {
        'l_address_protocol_chain_prefix': 'lending-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Sturdy',
            'h_protocol_type': Protocols.LENDING
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xA422CA380bd70EeF876292839222159E41AAEe17'
    },
}
