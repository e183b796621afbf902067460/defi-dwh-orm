from head.consts.protocols.const import Protocols
from head.consts.chains.const import Chains


FIXTURES = {
    # curve
    '3CRV Pool': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Curve',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': Chains.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7'
    },
    # uniswap
    'USDC/WETH LP': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Uniswap',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': Chains.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc'
    },
    # convex
    'sUSD/3CRV Pool': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Curve',
            'h_protocol_type': Protocols.STAKING
        },
        'h_chains': {
            'h_network_name': Chains.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xA5407eAE9Ba41422680e2e00537571bcC53efBfD'
    },
    # sushi
    'REN/WETH LP': {
        'l_address_protocol_chain_prefix': 'liquidity-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Sushiswap',
            'h_protocol_type': Protocols.DEX
        },
        'h_chains': {
            'h_network_name': Chains.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0x611CDe65deA90918c0078ac0400A72B0D25B9bb1'
    },
    'sUSD/3CRV Gauge': {
        'l_address_protocol_chain_prefix': 'staking-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Convex',
            'h_protocol_type': Protocols.STAKING
        },
        'h_chains': {
            'h_network_name': Chains.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0x22eE18aca7F3Ee920D01F25dA85840D12d98E8Ca'
    },
    '3CRV Gauge': {
        'l_address_protocol_chain_prefix': 'staking-pool-overview',
        'h_protocols': {
            'h_protocol_name': 'Curve',
            'h_protocol_type': Protocols.STAKING
        },
        'h_chains': {
            'h_network_name': Chains.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xbFcF63294aD7105dEa65aA58F8AE5BE2D9d0952A'
    },
}
