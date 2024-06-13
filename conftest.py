import requests
import json

def test_negative_booking_submission():
    url = "https://automationintesting.online/booking/"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-01",
            "checkout": "2024-07-10"
        },
        "additionalneeds": "Breakfast"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    assert response.status_code == 400, f"Expected 400, but got {response.status_code}"
    
    response_data = response.json()
    expected_error_message = "First name is required"
    assert "error" in response_data, "Expected error key in response"
    assert response_data["error"] == expected_error_message, f"Expected '{expected_error_message}', but got '{response_data['error']}'"

    print("Negative test case passed!")

test_negative_booking_submission()
