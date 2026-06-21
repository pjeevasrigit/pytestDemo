from playwright.sync_api import sync_playwright


def test_get_single_user():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.delete(
            "https://jsonplaceholder.typicode.com/users/1"
        )

        assert response.status == 200