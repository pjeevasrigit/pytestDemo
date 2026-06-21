from playwright.sync_api import sync_playwright


def test_get_single_user():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.get(
            "https://jsonplaceholder.typicode.com/users/1"
        )

        assert response.ok

        data = response.json()

        assert data["address"]["street"] == "Kulas Light"
        assert data["name"] == "Leanne Graham"