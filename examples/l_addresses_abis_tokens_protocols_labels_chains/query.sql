SELECT
        l_address_abi_token_protocol_chain_pool as pool,
        l_address_abi_chain_contract as contract,
        h_address,
        h_abi_list,
        h_network_name,
        h_label_name,
        h_protocol_name,
        h_protocol_type
FROM l_addresses_abis_tokens_protocols_labels_chains
LEFT JOIN l_addresses_labels_chains USING(l_address_label_chain_id)
LEFT JOIN h_labels USING(h_label_id)
LEFT JOIN l_addresses_abis_tokens_protocols_chains USING(l_address_abi_token_protocol_chain_id)
LEFT JOIN l_addresses_abis_tokens_chains USING(l_address_abi_token_chain_id)
LEFT JOIN h_tokens USING(h_token_id)
LEFT JOIN l_addresses_abis_chains ON l_addresses_abis_tokens_protocols_chains.l_address_abi_chain_id = l_addresses_abis_chains.l_address_abi_chain_id
LEFT JOIN h_abis USING(h_abi_id)
LEFT JOIN l_addresses_chains ON l_addresses_abis_chains.l_address_chain_id = l_addresses_chains.l_address_chain_id
LEFT JOIN h_addresses USING(h_address_id)
LEFT JOIN l_protocols_chains USING(l_protocol_chain_id)
LEFT JOIN h_protocols USING(h_protocol_id)
LEFT JOIN h_chains ON l_protocols_chains.h_chain_id = h_chains.h_chain_id