

# all ['h_addresses']['wallet'] are taken from the latest certain pool tx
FIXTURES = {
    # curve
    '3CRV Gauge': {
        'l_address_protocol_label_chain_prefix': 'staking-pool-position-overview',
        'l_address_protocol_chain_prefix': 'staking-pool-overview',
        'h_labels': {
            'h_label_name': 'RANDOM_WALLET_3CRV'
        },
        'h_protocols': {
            'h_protocol_name': 'Curve',
            'h_protocol_type': Protocols.STAKING
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': {
            'wallet': '0x735ecC415cB6cB90ADbA978B7e9a229C6EF6ae9d',
            'contract': '0xbFcF63294aD7105dEa65aA58F8AE5BE2D9d0952A'  # 3crv gauge
        }
    },
    # uniswap
    'USDC/WETH LP': {
        'l_address_protocol_label_chain_prefix': 'liquidity-pool-position-overview',
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_labels': {
            'h_label_name': 'RANDOM_WALLET_UNISWAP_USDC/WETH',
            'h_label_notional': 'USD'
        },
        'h_protocols': {
            'h_protocol_name': 'Uniswap',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': {
            'wallet': '0xeC08867a12546ccf53b32efB8C23bb26bE0C04f1',
            'contract': '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc'  # USDC/WETH
        }
    },
    # convex
    'sUSD/3CRV Gauge': {
        'l_address_protocol_label_chain_prefix': 'staking-pool-position-overview',
        'l_address_protocol_chain_prefix': 'staking-pool-overview',
        'h_labels': {
            'h_label_name': 'RANDOM_WALLET_CONVEX_sUSD/3CRV',
            'h_label_notional': 'USD'
        },
        'h_protocols': {
            'h_protocol_name': 'Convex',
            'h_protocol_type': Protocols.STAKING
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': {
            'wallet': '0x10bf1Dcb5ab7860baB1C3320163C6dddf8DCC0e4',
            'contract': '0x22eE18aca7F3Ee920D01F25dA85840D12d98E8Ca'  # sUSD/3CRV
        }
    },
    # sushi
    'REN/WETH LP': {
        'l_address_protocol_label_chain_prefix': 'liquidity-pool-position-overview',
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_labels': {
            'h_label_name': 'RANDOM_WALLET_SUSHI_REN/WETH',
            'h_label_notional': 'USD'
        },
        'h_protocols': {
            'h_protocol_name': 'Sushiswap',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': 'eth',
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': {
            'wallet': '0xc5ed2333f8a2C351fCA35E5EBAdb2A82F5d254C3',
            'contract': '0x611CDe65deA90918c0078ac0400A72B0D25B9bb1'  # SRM/WETH
        }
    },
}
