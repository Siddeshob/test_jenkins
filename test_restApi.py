import requests
import pytest

BASE_URL = "https://api.restful-api.dev"

@pytest.mark.smoke
class TestAPITest:

    @pytest.mark.getdata
    def test_get_mobile_list(self):
        response = requests.get(f"{BASE_URL}/objects")

        # Status code validation
        assert response.status_code == 200

        # Response validation
        json_res = response.json()
        assert isinstance(json_res, list)

        # Optional: check data exists
        assert len(json_res) > 0


    




# add next endpoint 