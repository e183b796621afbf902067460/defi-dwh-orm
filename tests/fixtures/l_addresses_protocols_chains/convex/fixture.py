from head.consts.protocols.const import Protocols


FIXTURE = {
    'sUSD/3CRV Gauge': {
        'l_address_protocol_chain_prefix': 'staking-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Convex',
            'h_protocol_type': Protocols.STAKING
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0x22eE18aca7F3Ee920D01F25dA85840D12d98E8Ca'
    },
    'FRAX/3CRV Gauge': {
        'l_address_protocol_chain_prefix': 'staking-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Convex',
            'h_protocol_type': Protocols.STAKING
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xB900EF131301B307dB5eFcbed9DBb50A3e209B2e'
    }
}
