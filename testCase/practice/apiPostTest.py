from playwright.sync_api import sync_playwright


def test_create_post():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        payload = {
            "title": "Playwright",
            "body": "API Testing",
            "userId": 1
        }

        response = request_context.post(
            "https://jsonplaceholder.typicode.com/posts",
            data=payload
        )

        assert response.status == 201

        response_data = response.json()

        print(response_data)

        assert response_data["title"] == "Playwright"