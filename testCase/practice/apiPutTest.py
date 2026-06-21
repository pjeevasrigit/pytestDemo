from playwright.sync_api import sync_playwright


def test_update_post():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        payload = {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated Body",
            "userId": 1
        }

        response = request_context.put(
            "https://jsonplaceholder.typicode.com/posts/1",
            data=payload
        )

        assert response.status == 200

        data = response.json()

        assert data["title"] == "Updated Title"