from head.consts.protocols.const import Protocols


FIXTURE = {
    'REN/WETH LP': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Sushiswap',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0x611CDe65deA90918c0078ac0400A72B0D25B9bb1'
    },
    'USDT/WETH LP': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Sushiswap',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0x06da0fd433C1A5d7a4faa01111c044910A184553'
    }
}
