import os
import tempfile

import pytest
from flask import Flask

from src.distogo import create_app
from src.distogo.models import db
from src.distogo.models.auth import User, Account
from src.distogo.models.dashboard import (
    Product,
    ProductEtsy,
    Inventory,
    InventoryWhenSold,
    Listing,
    ListingEtsy,
    Channel,
    ChannelEtsy,
    Platform
)


def create_and_test(model, data):
    new_model = model(**data)
    db.session.add(new_model)
    db.session.commit()
    for key, value in data.items():
        assert getattr(new_model, key) == value


@pytest.fixture
def app():
    app = create_app('testing')
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()

    with app.app_context():
        db.create_all(app=app)
        user = User('john@doe.com', 'johndoe12345')
        db.session.add(user)
        db.session.commit()
        account = Account(1)
        db.session.add(account)
        db.session.commit()

    yield app

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_product(app: Flask):
    with app.app_context():
        data = {
            'title': 'Macbook Pro',
            'url': 'https://www.apple.com/ie/shop/buy-mac/macbook-pro',
            'caption': '2.4GHz Quad-Core Processor with '
                       'Turbo Boost up to 4.1GHz '
                       '256GB Storage Touch Bar and Touch ID',
            'description': '2.4GHz quad-core '
                           '8th‑generation Intel Core i5 processor, '
                           'Turbo Boost up to 4.1GHz \n'
                           'Retina display with True Tone \n'
                           'Touch Bar and Touch ID \n'
                           'Intel Iris Plus Graphics 655 \n'
                           '8GB 2133MHz LPDDR3 memory \n'
                           '256GB SSD storage \n'
                           'Four Thunderbolt 3 ports \n'
                           'Backlit Keyboard - British',
            'account_id': 1
        }
        create_and_test(Product, data)


def test_product_etsy(app: Flask):
    with app.app_context():
        data = {
            'category': "Men's coat",
            'renewal': 'Manual',
            'type': 'Physical',
            'section': 'Custom section',
            'who_made_it': 'I did',
            'what_is_it': 'A finished product',
            'when_was_it_made': 'Made to order',
            'tags': 'Shape, colour, style, function, etc.',
            'materials': 'Ingredients, components',
            'product_id': 1
        }
        create_and_test(ProductEtsy, data)


def test_inventory(app: Flask):
    with app.app_context():
        data = {
            'sku': 'macbook-pro-1',
            'price': 50,
            'quantity': 25,
            'is_active': True,
            'product_id': 1,
            'when_sold_id': 1
        }
        create_and_test(Inventory, data)


def test_inventory_when_sold(app: Flask):
    with app.app_context():
        data = {
            'name': 'When sold'
        }
        create_and_test(InventoryWhenSold, data)


def test_listing(app: Flask):
    with app.app_context():
        data = {
            'inventory_id': 1,
            'channel_id': 1
        }
        create_and_test(Listing, data)


def test_listing_etsy(app: Flask):
    with app.app_context():
        data = {
            'listing_id': 1,
            'listing_etsy_id': 718275147
        }
        create_and_test(ListingEtsy, data)


def test_channel(app: Flask):
    with app.app_context():
        data = {
            'platform_id': 1,
            'account_id': 1,
        }
        create_and_test(Channel, data)


def test_channel_etsy(app: Flask):
    with app.app_context():
        data = {
            'oauth_token': '12345',
            'oauth_token_secret': '12345',
            'shop_id': 'shop-id-1',
            'shop_name': 'test-distogo',
            'user_id': 'j12k3kdsl',
            'channel_id': 1
        }
        create_and_test(ChannelEtsy, data)


def test_platform(app: Flask):
    with app.app_context():
        data = {
            'name': 'Etsy'
        }
        create_and_test(Platform, data)
