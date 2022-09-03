import pytest

from sqlalchemy_utils import database_exists, drop_database, create_database
from sqlalchemy.orm.session import Session

from cfg.engine import db_url, db_engine
from cfg.session import Session

from base import *
from base.main import Base

from tests.fixtures.l_addresses_protocols_labels_chains.fixture import FIXTURES as POSITION_OVERVIEW_FIXTURES

from tests.fixtures.l_addresses_protocols_chains.aave.fixture import FIXTURE as AAVE_FIXTURE
from tests.fixtures.l_addresses_protocols_chains.convex.fixture import FIXTURE as CONVEX_FIXTURE
from tests.fixtures.l_addresses_protocols_chains.curve.fixture import FIXTURE as CURVE_FIXTURE
from tests.fixtures.l_addresses_protocols_chains.ellipsis.fixture import FIXTURE as ELLIPSIS_FIXTURE
from tests.fixtures.l_addresses_protocols_chains.geist.fixture import FIXTURE as GEIST_FIXTURE
from tests.fixtures.l_addresses_protocols_chains.nereus.fixture import FIXTURE as NEREUS_FIXTURE
from tests.fixtures.l_addresses_protocols_chains.pancakeswap.fixture import FIXTURE as PANCAKESWAP_FIXTURE
from tests.fixtures.l_addresses_protocols_chains.sturdy.fixture import FIXTURE as STURDY_FIXTURE
from tests.fixtures.l_addresses_protocols_chains.sushiswap.fixture import FIXTURE as SUSHISWAP_FIXTURE
from tests.fixtures.l_addresses_protocols_chains.uniswap.fixture import FIXTURE as UNISWAP_FIXTURE


@pytest.fixture(scope='session', autouse=True)
def db_init():
    if database_exists(db_url):
        drop_database(db_url)
    create_database(db_url)
    Base.metadata.create_all(db_engine)


@pytest.fixture(scope='session', autouse=True)
def session():
    _session = Session()
    yield _session
    _session.close()


@pytest.fixture(scope='session', autouse=True)
def l_addresses_protocols_labels_chains(
        session: Session,
        fixtures: dict = POSITION_OVERVIEW_FIXTURES
):
    for contract, fixture in fixtures.items():

        h_label = session.query(HubLabels).filter_by(h_label_name=fixture['h_labels']['h_label_name']).first()
        if not h_label:
            h_label = HubLabels(
                h_label_name=fixture['h_labels']['h_label_name']
            )

        h_protocol = session.query(HubProtocols).filter_by(
            h_protocol_name=fixture['h_protocols']['h_protocol_name'],
            h_protocol_type=fixture['h_protocols']['h_protocol_type']).first()
        if not h_protocol:
            h_protocol = HubProtocols(
                h_protocol_name=fixture['h_protocols']['h_protocol_name'],
                h_protocol_type=fixture['h_protocols']['h_protocol_type']
            )

        h_chain = session.query(HubChains).filter_by(
            h_network_name=fixture['h_chains']['h_network_name'],
            h_network_id=fixture['h_chains']['h_network_id']).first()
        if not h_chain:
            h_chain = HubChains(
                h_network_name=fixture['h_chains']['h_network_name'],
                h_network_id=fixture['h_chains']['h_network_id'],
                h_network_endpoint=fixture['h_chains']['h_network_endpoint']
            )

        h_address_wallet = session.query(HubAddresses).filter_by(h_address=fixture['h_addresses']['wallet']).first()
        if not h_address_wallet:
            h_address_wallet = HubAddresses(
                h_address=fixture['h_addresses']['wallet']
            )

        h_address_contract = session.query(HubAddresses).filter_by(h_address=fixture['h_addresses']['contract']).first()
        if not h_address_contract:
            h_address_contract = HubAddresses(
                h_address=fixture['h_addresses']['contract']
            )

        hubs = [
            h_label,
            h_protocol,
            h_chain,
            h_address_wallet,
            h_address_contract
        ]
        session.add_all(hubs)
        session.commit()

        l_protocol_chain = session.query(LinkProtocolsChains).filter_by(
            h_protocol_id=h_protocol.h_protocol_id,
            h_chain_id=h_chain.h_chain_id
        ).first()
        if not l_protocol_chain:
            l_protocol_chain = LinkProtocolsChains(
                h_protocol_id=h_protocol.h_protocol_id,
                h_chain_id=h_chain.h_chain_id
            )

        l_address_chain_wallet = session.query(LinkAddressesChains).filter_by(
            h_address_id=h_address_wallet.h_address_id,
            h_chain_id=h_chain.h_chain_id,
            l_address_chain_name=fixture['h_labels']['h_label_name']
        ).first()
        if not l_address_chain_wallet:
            l_address_chain_wallet = LinkAddressesChains(
                h_address_id=h_address_wallet.h_address_id,
                h_chain_id=h_chain.h_chain_id,
                l_address_chain_name=fixture['h_labels']['h_label_name']
            )

        l_address_chain_pool = session.query(LinkAddressesChains).filter_by(
            h_address_id=h_address_contract.h_address_id,
            h_chain_id=h_chain.h_chain_id,
            l_address_chain_name=contract
        ).first()
        if not l_address_chain_pool:
            l_address_chain_pool = LinkAddressesChains(
                h_address_id=h_address_contract.h_address_id,
                h_chain_id=h_chain.h_chain_id,
                l_address_chain_name=contract
            )

        links = [
            l_protocol_chain,
            l_address_chain_wallet,
            l_address_chain_pool
        ]
        session.add_all(links)
        session.commit()

        l_address_label_chain = session.query(LinkAddressesLabelsChains).filter_by(
            l_address_chain_id=l_address_chain_wallet.l_address_chain_id,
            h_label_id=h_label.h_label_id
        ).first()
        if not l_address_label_chain:
            l_address_label_chain = LinkAddressesLabelsChains(
                l_address_chain_id=l_address_chain_wallet.l_address_chain_id,
                h_label_id=h_label.h_label_id
            )

        session.add(l_address_label_chain)
        session.commit()

        l_address_protocol_chain = session.query(LinkAddressesProtocolsChains).filter_by(
            l_protocol_chain_id=l_protocol_chain.l_protocol_chain_id,
            l_address_chain_id=l_address_chain_pool.l_address_chain_id,
            l_address_protocol_chain_prefix=fixture['l_address_protocol_chain_prefix']
        ).first()
        if not l_address_protocol_chain:
            l_address_protocol_chain = LinkAddressesProtocolsChains(
                l_protocol_chain_id=l_protocol_chain.l_protocol_chain_id,
                l_address_chain_id=l_address_chain_pool.l_address_chain_id,
                l_address_protocol_chain_prefix=fixture['l_address_protocol_chain_prefix']
            )
        session.add(l_address_protocol_chain)
        session.commit()

        l_address_protocol_label_chain = session.query(LinkAddressesProtocolsLabelsChains).filter_by(
            l_address_protocol_chain_id=l_address_protocol_chain.l_address_protocol_chain_id,
            l_address_label_chain_id=l_address_label_chain.l_address_label_chain_id,
            l_address_protocol_label_chain_prefix=fixture['l_address_protocol_label_chain_prefix']
        ).first()
        if not l_address_protocol_label_chain:
            l_address_protocol_label_chain = LinkAddressesProtocolsLabelsChains(
                l_address_protocol_chain_id=l_address_protocol_chain.l_address_protocol_chain_id,
                l_address_label_chain_id=l_address_label_chain.l_address_label_chain_id,
                l_address_protocol_label_chain_prefix=fixture['l_address_protocol_label_chain_prefix']
            )

        session.add(l_address_protocol_label_chain)
        session.commit()


@pytest.fixture(scope='session', autouse=True)
def l_addresses_protocols_chains(
        l_addresses_protocols_labels_chains,
        session: Session,
        fixtures: tuple = (
            AAVE_FIXTURE, CONVEX_FIXTURE, CURVE_FIXTURE,
            ELLIPSIS_FIXTURE, GEIST_FIXTURE, NEREUS_FIXTURE,
            PANCAKESWAP_FIXTURE, STURDY_FIXTURE, SUSHISWAP_FIXTURE,
            UNISWAP_FIXTURE
        )
):
    for protocol in fixtures:
        for contract, fixture in protocol.items():

            h_protocol = session.query(HubProtocols).filter_by(
                h_protocol_name=fixture['h_protocols']['h_protocol_name'],
                h_protocol_type=fixture['h_protocols']['h_protocol_type']).first()
            if not h_protocol:
                h_protocol = HubProtocols(
                    h_protocol_name=fixture['h_protocols']['h_protocol_name'],
                    h_protocol_type=fixture['h_protocols']['h_protocol_type']
                )

            h_chain = session.query(HubChains).filter_by(
                h_network_name=fixture['h_chains']['h_network_name'],
                h_network_id=fixture['h_chains']['h_network_id']).first()
            if not h_chain:
                h_chain = HubChains(
                    h_network_name=fixture['h_chains']['h_network_name'],
                    h_network_id=fixture['h_chains']['h_network_id'],
                    h_network_endpoint=fixture['h_chains']['h_network_endpoint']
                )

            h_address_contract = session.query(HubAddresses).filter_by(h_address=fixture['h_addresses']).first()
            if not h_address_contract:
                h_address_contract = HubAddresses(
                    h_address=fixture['h_addresses']
                )

            hubs = [
                h_protocol,
                h_chain,
                h_address_contract
            ]
            session.add_all(hubs)
            session.commit()

            l_protocol_chain = session.query(LinkProtocolsChains).filter_by(
                h_protocol_id=h_protocol.h_protocol_id,
                h_chain_id=h_chain.h_chain_id).first()
            if not l_protocol_chain:
                l_protocol_chain = LinkProtocolsChains(
                    h_protocol_id=h_protocol.h_protocol_id,
                    h_chain_id=h_chain.h_chain_id
                )

            l_address_chain_pool = session.query(LinkAddressesChains).filter_by(
                h_address_id=h_address_contract.h_address_id,
                h_chain_id=h_chain.h_chain_id,
                l_address_chain_name=contract
            ).first()
            if not l_address_chain_pool:
                l_address_chain_pool = LinkAddressesChains(
                    h_address_id=h_address_contract.h_address_id,
                    h_chain_id=h_chain.h_chain_id,
                    l_address_chain_name=contract
                )

            links = [
                l_protocol_chain,
                l_address_chain_pool
            ]
            session.add_all(links)
            session.commit()

            l_address_protocol_chain = session.query(LinkAddressesProtocolsChains).filter_by(
                l_protocol_chain_id=l_protocol_chain.l_protocol_chain_id,
                l_address_chain_id=l_address_chain_pool.l_address_chain_id,
                l_address_protocol_chain_prefix=fixture['l_address_protocol_chain_prefix']
            ).first()
            if not l_address_protocol_chain:
                l_address_protocol_chain = LinkAddressesProtocolsChains(
                    l_protocol_chain_id=l_protocol_chain.l_protocol_chain_id,
                    l_address_chain_id=l_address_chain_pool.l_address_chain_id,
                    l_address_protocol_chain_prefix=fixture['l_address_protocol_chain_prefix']
                )
            session.add(l_address_protocol_chain)
            session.commit()
