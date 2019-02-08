import unittest
import json
import sys

sys.path.insert(0 ,"/home/lee/Downloads/Andela/politicoapp-api")

#local
from app import create_app
from instance import config


class TestParties(unittest.TestCase):
    def setUp(self):
        self.app= create_app(config.DevelopmentConfig)
        self.client=self.app.test_client()
        self.app_context=  self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    def tdest_party_creation(self):
        raw_data={
            "id": 11,
            "name": "GTD",
            "hqAddress": "Thika",
            "logoUrl":"sss.ssd/img.png"
        }
        res= self.client.post("/api/v1/parties", 
        data= json.dumps(raw_data),
        headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)
        

    def test_testswor(self):
        self.assertTrue(True,True)



