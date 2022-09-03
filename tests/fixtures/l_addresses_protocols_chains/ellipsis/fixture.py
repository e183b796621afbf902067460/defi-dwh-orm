from head.consts.protocols.const import Protocols


FIXTURE = {
    '3EPS Pool': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Ellipsis',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': 'bsc',
            'h_network_id': 2,
            'h_network_endpoint': 'bsc.endpoint'
        },
        'h_addresses': '0x160CAed03795365F3A589f10C379FfA7d75d4E76'
    },
    'USDD/3EPS Pool': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Ellipsis',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': 'bsc',
            'h_network_id': 2,
            'h_network_endpoint': 'bsc.endpoint'
        },
        'h_addresses': '0xC2cF01F785C587645440ccD488B188945C9505e7'
    },
    '2pool Pool': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Ellipsis',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': 'bsc',
            'h_network_id': 2,
            'h_network_endpoint': 'bsc.endpoint'
        },
        'h_addresses': '0x408A61e158D7BC0CD339BC76917b8Ea04739d473'
    }
}
