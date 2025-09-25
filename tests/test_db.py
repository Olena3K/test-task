from app.db import User, Address, CreditCard


def test_user_model():
    u = User(id=1, name="Test", email="test@test.com")
    assert u.name == "Test"


def test_address_and_card_linked_to_user():
    u = User(id=1, name="Test", email="test@test.com")
    a = Address(id=1, user_id=1, street="Shevchenka Street")
    c = CreditCard(id=1, user_id=1, card_number="0000-1111")
    assert a.user_id == u.id
    assert c.user_id == u.id
