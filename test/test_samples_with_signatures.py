import requests
import json
import unittest

from constants_for_tests import *

class TestSamplesWithSignatures(unittest.TestCase):

    def test_samples_with_signatures(self):
        url = API_BASE + '/samples-with-signatures'
        
        payload = {
            "sources":["ICGC-BRCA-EU"],
            "signatures":[
                "COSMIC 1",
                "COSMIC 2",
                "COSMIC 3",
                "COSMIC 4",
                "COSMIC 5",
                "COSMIC 6",
                "COSMIC 7",
                "COSMIC 8",
                "COSMIC 9",
                "COSMIC 10",
                "COSMIC 11",
                "COSMIC 12",
                "COSMIC 13",
                "COSMIC 14",
                "COSMIC 15",
                "COSMIC 16",
                "COSMIC 17",
                "COSMIC 18",
                "COSMIC 19",
                "COSMIC 20",
                "COSMIC 21",
                "COSMIC 22",
                "COSMIC 23",
                "COSMIC 24",
                "COSMIC 25",
                "COSMIC 26",
                "COSMIC 27",
                "COSMIC 28",
                "COSMIC 29",
                "COSMIC 30",
                "5* A"
            ]
        }
        r = requests.post(url, data=json.dumps(payload))
        r.raise_for_status()
        res = r.json()
        
        self.assertEqual({'signatures', 'projects'}, set(res.keys()))
        self.assertEqual(31, len(list(res['signatures'].keys())))
        self.assertEqual(569, res['projects']['ICGC-BRCA-EU'])
    