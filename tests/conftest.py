import pytest

from sqlalchemy_utils import database_exists, drop_database, create_database
from sqlalchemy.orm.session import Session

from cfg.engine import db_url, db_engine
from cfg.session import Session

from base import *
from base.main import Base

from tests.fixtures.l_addresses_protocols_categories_chains.aave.fixture import FIXTURE as AAVE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_chains.convex.fixture import FIXTURE as CONVEX_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_chains.curve.fixture import FIXTURE as CURVE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_chains.ellipsis.fixture import FIXTURE as ELLIPSIS_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_chains.geist.fixture import FIXTURE as GEIST_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_chains.nereus.fixture import FIXTURE as NEREUS_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_chains.pancakeswap.fixture import FIXTURE as PANCAKESWAP_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_chains.sturdy.fixture import FIXTURE as STURDY_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_chains.sushiswap.fixture import FIXTURE as SUSHISWAP_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_chains.uniswap.fixture import FIXTURE as UNISWAP_FIXTURE

from tests.fixtures.l_addresses_protocols_categories_labels_chains.aave.fixture import FIXTURE as AAVE_EXPOSURE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_labels_chains.convex.fixture import FIXTURE as CONVEX_EXPOSURE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_labels_chains.curve.fixture import FIXTURE as CURVE_EXPOSURE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_labels_chains.ellipsis.fixture import FIXTURE as ELLIPSIS_EXPOSURE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_labels_chains.geist.fixture import FIXTURE as GEIST_EXPOSURE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_labels_chains.nereus.fixture import FIXTURE as NEREUS_EXPOSURE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_labels_chains.pancakeswap.fixture import FIXTURE as PANCAKESWAP_EXPOSURE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_labels_chains.sturdy.fixture import FIXTURE as STURDY_EXPOSURE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_labels_chains.sushiswap.fixture import FIXTURE as SUSHISWAP_EXPOSURE_FIXTURE
from tests.fixtures.l_addresses_protocols_categories_labels_chains.uniswap.fixture import FIXTURE as UNISWAP_EXPOSURE_FIXTURE


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
def l_addresses_protocols_categories_labels_chains(
        session: Session,
        fixtures: tuple = (
            AAVE_EXPOSURE_FIXTURE, CONVEX_EXPOSURE_FIXTURE, CURVE_EXPOSURE_FIXTURE,
            ELLIPSIS_EXPOSURE_FIXTURE, GEIST_EXPOSURE_FIXTURE, NEREUS_EXPOSURE_FIXTURE,
            PANCAKESWAP_EXPOSURE_FIXTURE, STURDY_EXPOSURE_FIXTURE, SUSHISWAP_EXPOSURE_FIXTURE,
            UNISWAP_EXPOSURE_FIXTURE
        )
):
    for protocol in fixtures:
        for contract, fixture in protocol.items():

            h_protocol = session.query(HubProtocols) \
                .filter_by(
                h_protocol_name=fixture['h_protocols']['h_protocol_name']
            ) \
                .first()
            if not h_protocol:
                h_protocol = HubProtocols(
                    h_protocol_name=fixture['h_protocols']['h_protocol_name']
                )

            h_protocol_category = session.query(HubProtocolsCategories) \
                .filter_by(
                h_protocol_category_name=fixture['h_protocols']['h_protocol_category_name']
            ) \
                .first()
            if not h_protocol_category:
                h_protocol_category = HubProtocolsCategories(
                    h_protocol_category_name=fixture['h_protocols']['h_protocol_category_name']
                )

            h_chain = session.query(HubChains) \
                .filter_by(
                h_network_name=fixture['h_chains']['h_network_name'],
                h_network_id=fixture['h_chains']['h_network_id']) \
                .first()
            if not h_chain:
                h_chain = HubChains(
                    h_network_name=fixture['h_chains']['h_network_name'],
                    h_network_id=fixture['h_chains']['h_network_id'],
                    h_network_endpoint=fixture['h_chains']['h_network_endpoint']
                )

            h_address_pool = session.query(HubAddresses) \
                .filter_by(
                h_address=fixture['h_addresses']['h_pool_address']) \
                .first()
            if not h_address_pool:
                h_address_pool = HubAddresses(
                    h_address=fixture['h_addresses']['h_pool_address']
                )

            h_address_wallet = session.query(HubAddresses) \
                .filter_by(
                h_address=fixture['h_addresses']['h_wallet_address']) \
                .first()
            if not h_address_wallet:
                h_address_wallet = HubAddresses(
                    h_address=fixture['h_addresses']['h_wallet_address']
                )

            h_label = session.query(HubLabels) \
                .filter_by(
                h_label_name=fixture['h_labels']['h_label_name']) \
                .first()
            if not h_label:
                h_label = HubLabels(
                    h_label_name=fixture['h_labels']['h_label_name']
                )

            hubs = [
                h_protocol,
                h_protocol_category,
                h_chain,
                h_address_pool,
                h_address_wallet,
                h_label
            ]
            session.add_all(hubs)
            session.commit()

            l_protocol_category = session.query(LinkProtocolsCategories) \
                .filter_by(
                h_protocol_id=h_protocol.h_protocol_id,
                h_protocol_category_id=h_protocol_category.h_protocol_category_id) \
                .first()
            if not l_protocol_category:
                l_protocol_category = LinkProtocolsCategories(
                    h_protocol_id=h_protocol.h_protocol_id,
                    h_protocol_category_id=h_protocol_category.h_protocol_category_id
                )

            l_address_chain_pool = session.query(LinkAddressesChains) \
                .filter_by(
                h_address_id=h_address_pool.h_address_id,
                h_chain_id=h_chain.h_chain_id,
                l_address_chain_name=contract
            ) \
                .first()
            if not l_address_chain_pool:
                l_address_chain_pool = LinkAddressesChains(
                    h_address_id=h_address_pool.h_address_id,
                    h_chain_id=h_chain.h_chain_id,
                    l_address_chain_name=contract
                )

            l_address_chain_wallet = session.query(LinkAddressesChains) \
                .filter_by(
                h_address_id=h_address_wallet.h_address_id,
                h_chain_id=h_chain.h_chain_id,
                l_address_chain_name=contract
            ) \
                .first()
            if not l_address_chain_wallet:
                l_address_chain_wallet = LinkAddressesChains(
                    h_address_id=h_address_wallet.h_address_id,
                    h_chain_id=h_chain.h_chain_id,
                    l_address_chain_name='Wallet'
                )

            links = [
                l_protocol_category,
                l_address_chain_pool,
                l_address_chain_wallet
            ]
            session.add_all(links)
            session.commit()

            l_protocol_category_chain = session.query(LinkProtocolsCategoriesChains) \
                .filter_by(
                l_protocol_category_id=l_protocol_category.l_protocol_category_id,
                h_chain_id=h_chain.h_chain_id
            ) \
                .first()
            if not l_protocol_category_chain:
                l_protocol_category_chain = LinkProtocolsCategoriesChains(
                    l_protocol_category_id=l_protocol_category.l_protocol_category_id,
                    h_chain_id=h_chain.h_chain_id
                )

            l_address_label_chain = session.query(LinkAddressesLabelsChains) \
                .filter_by(
                l_address_chain_id=l_address_chain_wallet.l_address_chain_id,
                h_label_id=h_label.h_label_id
            ) \
                .first()
            if not l_address_label_chain:
                l_address_label_chain = LinkAddressesLabelsChains(
                    l_address_chain_id=l_address_chain_wallet.l_address_chain_id,
                    h_label_id=h_label.h_label_id
                )
            links = [
                l_address_label_chain,
                l_protocol_category_chain
            ]
            session.add_all(links)
            session.commit()

            l_address_protocol_category_chain = session.query(LinkAddressesProtocolsCategoriesChains) \
                .filter_by(
                l_protocol_category_chain_id=l_protocol_category_chain.l_protocol_category_chain_id,
                l_address_chain_id=l_address_chain_pool.l_address_chain_id
            ) \
                .first()
            if not l_address_protocol_category_chain:
                l_address_protocol_category_chain = LinkAddressesProtocolsCategoriesChains(
                    l_protocol_category_chain_id=l_protocol_category_chain.l_protocol_category_chain_id,
                    l_address_chain_id=l_address_chain_pool.l_address_chain_id
                )
            session.add(l_address_protocol_category_chain)
            session.commit()

            l_address_protocol_category_label_chain = session.query(LinkAddressesProtocolsCategoriesLabelsChains) \
                .filter_by(
                l_address_label_chain_id=l_address_label_chain.l_address_label_chain_id,
                l_address_protocol_category_chain_id=l_address_protocol_category_chain.l_address_protocol_category_chain_id
            ) \
                .first()
            if not l_address_protocol_category_label_chain:
                l_address_protocol_category_label_chain = LinkAddressesProtocolsCategoriesLabelsChains(
                    l_address_label_chain_id=l_address_label_chain.l_address_label_chain_id,
                    l_address_protocol_category_chain_id=l_address_protocol_category_chain.l_address_protocol_category_chain_id
                )
            session.add(l_address_protocol_category_label_chain)
            session.commit()


@pytest.fixture(scope='session', autouse=True)
def l_addresses_protocols_categories_chains(
        l_addresses_protocols_categories_labels_chains,
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

            h_protocol = session.query(HubProtocols)\
                .filter_by(
                h_protocol_name=fixture['h_protocols']['h_protocol_name']
            )\
                .first()
            if not h_protocol:
                h_protocol = HubProtocols(
                    h_protocol_name=fixture['h_protocols']['h_protocol_name']
                )

            h_protocol_category = session.query(HubProtocolsCategories)\
                .filter_by(
                h_protocol_category_name=fixture['h_protocols']['h_protocol_category_name']
            )\
                .first()
            if not h_protocol_category:
                h_protocol_category = HubProtocolsCategories(
                    h_protocol_category_name=fixture['h_protocols']['h_protocol_category_name']
                )

            h_chain = session.query(HubChains)\
                .filter_by(
                h_network_name=fixture['h_chains']['h_network_name'],
                h_network_id=fixture['h_chains']['h_network_id'])\
                .first()
            if not h_chain:
                h_chain = HubChains(
                    h_network_name=fixture['h_chains']['h_network_name'],
                    h_network_id=fixture['h_chains']['h_network_id'],
                    h_network_endpoint=fixture['h_chains']['h_network_endpoint']
                )

            h_address_pool = session.query(HubAddresses)\
                .filter_by(
                h_address=fixture['h_addresses'])\
                .first()
            if not h_address_pool:
                h_address_pool = HubAddresses(
                    h_address=fixture['h_addresses']
                )

            hubs = [
                h_protocol,
                h_protocol_category,
                h_chain,
                h_address_pool
            ]
            session.add_all(hubs)
            session.commit()

            l_protocol_category = session.query(LinkProtocolsCategories)\
                .filter_by(
                h_protocol_id=h_protocol.h_protocol_id,
                h_protocol_category_id=h_protocol_category.h_protocol_category_id)\
                .first()
            if not l_protocol_category:
                l_protocol_category = LinkProtocolsCategories(
                    h_protocol_id=h_protocol.h_protocol_id,
                    h_protocol_category_id=h_protocol_category.h_protocol_category_id
                )

            l_address_chain_pool = session.query(LinkAddressesChains)\
                .filter_by(
                h_address_id=h_address_pool.h_address_id,
                h_chain_id=h_chain.h_chain_id,
                l_address_chain_name=contract
            )\
                .first()
            if not l_address_chain_pool:
                l_address_chain_pool = LinkAddressesChains(
                    h_address_id=h_address_pool.h_address_id,
                    h_chain_id=h_chain.h_chain_id,
                    l_address_chain_name=contract
                )

            links = [
                l_protocol_category,
                l_address_chain_pool
            ]
            session.add_all(links)
            session.commit()

            l_protocol_category_chain = session.query(LinkProtocolsCategoriesChains)\
                .filter_by(
                l_protocol_category_id=l_protocol_category.l_protocol_category_id,
                h_chain_id=h_chain.h_chain_id
            )\
                .first()
            if not l_protocol_category_chain:
                l_protocol_category_chain = LinkProtocolsCategoriesChains(
                    l_protocol_category_id=l_protocol_category.l_protocol_category_id,
                    h_chain_id=h_chain.h_chain_id
                )
            session.add(l_protocol_category_chain)
            session.commit()

            l_address_protocol_category_chain = session.query(LinkAddressesProtocolsCategoriesChains) \
                .filter_by(
                l_protocol_category_chain_id=l_protocol_category_chain.l_protocol_category_chain_id,
                l_address_chain_id=l_address_chain_pool.l_address_chain_id
            ) \
                .first()
            if not l_address_protocol_category_chain:
                l_address_protocol_category_chain = LinkAddressesProtocolsCategoriesChains(
                    l_protocol_category_chain_id=l_protocol_category_chain.l_protocol_category_chain_id,
                    l_address_chain_id=l_address_chain_pool.l_address_chain_id
                )
            session.add(l_address_protocol_category_chain)
            session.commit()
