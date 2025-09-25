import responses
from app.tasks import fetch_users, fetch_credit_cards, fetch_addresses


@responses.activate
def test_fetch_users():
    responses.add(
        responses.GET,
        "https://jsonplaceholder.typicode.com/users",
        json=[{"id": 1, "name": "Test User", "email": "test@test.com"}],
        status=200,
    )
    fetch_users()


@responses.activate
def test_fetch_addresses():
    responses.add(
        responses.GET,
        "https://random-data-api.com/api/address/random_address",
        json={"street_address": "Shevchenka Street", "city": "Lviv"},
        status=200,
    )
    fetch_addresses()


@responses.activate
def test_fetch_creditcards():
    responses.add(
        responses.GET,
        "https://random-data-api.com/api/credit_card/random_credit_card",
        json={"street_address": "Shevchenka Street", "city": "Lviv"},
        status=200,
    )
    fetch_credit_cards()
