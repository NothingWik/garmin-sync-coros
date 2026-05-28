import os
import sys
import unittest

SCRIPT_DIR = os.path.join(os.path.dirname(__file__), "..", "..")
sys.path.append(os.path.abspath(SCRIPT_DIR))

from coros.coros_client import CorosClient


class CorosClientGetAllActivitiesTest(unittest.TestCase):
    def test_get_all_activities_handles_missing_total_page(self):
        client = CorosClient("", "")

        def fake_get_activities(size, page):
            return {"data": {"dataList": [{"labelId": "1"}]}}

        client.getActivities = fake_get_activities
        all_activities = client.getAllActivities()
        self.assertEqual([{"labelId": "1"}], all_activities)

    def test_get_all_activities_reads_all_pages(self):
        client = CorosClient("", "")

        def fake_get_activities(size, page):
            pages = {
                1: {"data": {"totalPage": 2, "dataList": [{"labelId": "1"}]}},
                2: {"data": {"totalPage": 2, "dataList": [{"labelId": "2"}]}},
            }
            return pages[page]

        client.getActivities = fake_get_activities
        all_activities = client.getAllActivities()
        self.assertEqual([{"labelId": "1"}, {"labelId": "2"}], all_activities)


if __name__ == "__main__":
    unittest.main()
