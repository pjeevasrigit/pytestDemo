import json

def test_create_user(api_context):

    with open("payloads/user.json") as file:
        payload = json.load(file)

    payload["name"] = "Jeevasri"
    payload["job"] = "Automation Engineer"

    response = api_context.post(
        "/users",
        data=payload
    )

    assert response.status == 201

    print(response.json())