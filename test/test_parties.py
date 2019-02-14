"""A module for testing the all party functionalities"""
import json
from test.base_testcase import BaseTest
from app.api.v1.models.party_model import Party
#from app.api.v1.models.party_models import Party
from app.api.v1.models.office_model import Office
from app.api.v1.utils import find_by_id


class TestParty(BaseTest):



    def test_create_party_already_exists(self):
        """Tests the creation of a party that already exists"""
        with self.app_context():
            response = self.app.post(
                "/api/v1/parties", data=json.dumps(self.party_test_data), content_type="application/json")
            self.assertEqual(response.status_code, 400,
                             msg="POST creating an existing party did not return a 400 bad request.")

    def test_get_all_parties(self):
        """Test whether the API can list all products"""
        with self.app_context():
            response = self.app.get("/api/v1/parties")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "application/json")

    def test_get_specific_party(self):
        pass

    def test_get_party_not_found(self):
        """Tests the getting of a party which is not there """
        with self.app_context():
            response = self.app.get("/api/v1/parties/1000")
            self.assertEqual(response.status_code, 404,
                             msg="Error Party found, expectedd a 404 not found")

    def test_edit_party(self):
        pass

    def test_delete_party(self):
        pass

    def test_invalid_delete(self):
        """Tests for deleting a party that is not their"""
        with self.app_context():
            response = self.app.delete("/api/v1/parties/10")
            self.assertEqual(response.status_code, 404)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertIn("status", response_msg)
            response_data = response_msg["data"]
            self.assertListEqual(response_data, [{
                "message": "party does not exists"
            }])