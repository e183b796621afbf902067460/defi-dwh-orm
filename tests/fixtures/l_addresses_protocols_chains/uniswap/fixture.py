from head.consts.protocols.const import Protocols


FIXTURE = {
    'USDC/WETH LP': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Uniswap',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc'
    },
    'USDT/WETH LP': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Uniswap',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0x0d4a11d5EEaaC28EC3F61d100daF4d40471f1852'
    },
    'USDC/DAI LP': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Uniswap',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xAE461cA67B15dc8dc81CE7615e0320dA1A9aB8D5'
    },
}
