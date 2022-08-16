from orm.consts.protocolType import ProtocolType
from orm.consts.chainName import ChainName


FIXTURES = {
    # curve
    '3CRV Pool': {
        'l_address_token_protocol_chain_pool': '3CRV',
        'h_protocols': {
            'h_protocol_name': 'Curve',
            'h_protocol_type': ProtocolType.DEX
        },
        'h_chains': {
            'h_network_name': ChainName.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7'
    },
    # uniswap
    'USDC/WETH LP': {
        'l_address_token_protocol_chain_pool': 'USDC/WETH',
        'h_protocols': {
            'h_protocol_name': 'Uniswap',
            'h_protocol_type': ProtocolType.DEX
        },
        'h_chains': {
            'h_network_name': ChainName.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc'
    },
    # balancer
    'SRM/WETH LP': {
        'l_address_token_protocol_chain_pool': 'SRM/WETH',
        'h_protocols': {
            'h_protocol_name': 'Balancer',
            'h_protocol_type': ProtocolType.DEX
        },
        'h_chains': {
            'h_network_name': ChainName.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0x231E687C9961d3A27e6E266Ac5C433Ce4F8253E4'
    },
    # convex
    'sUSD/3CRV Pool': {
        'l_address_token_protocol_chain_pool': 'sUSD/3CRV',
        'h_protocols': {
            'h_protocol_name': 'Convex',
            'h_protocol_type': ProtocolType.STAKING
        },
        'h_chains': {
            'h_network_name': ChainName.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0xA5407eAE9Ba41422680e2e00537571bcC53efBfD'
    },
    # sushi
    'REN/WETH LP': {
        'l_address_token_protocol_chain_pool': 'REN/WETH',
        'h_protocols': {
            'h_protocol_name': 'Sushiswap',
            'h_protocol_type': ProtocolType.DEX
        },
        'h_chains': {
            'h_network_name': ChainName.ETH,
            'h_network_id': 1,
            'h_network_endpoint': 'eth.endpoint'
        },
        'h_addresses': '0x611CDe65deA90918c0078ac0400A72B0D25B9bb1'
    },
}
