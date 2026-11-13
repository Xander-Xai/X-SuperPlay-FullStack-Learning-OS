"""Only static router behavior is verified; independent learning remains NOT_RUN."""
import sys
import unittest
from pathlib import Path

LEARN = Path(__file__).resolve().parents[1] / "learning"
sys.path.insert(0, str(LEARN))
import route_need  # noqa: E402


class TestDemandRouter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nodes = route_need.load()

    def test_java_spring_query(self):
        ids = [n["id"] for n in route_need.find("Spring Boot API", self.nodes)]
        self.assertIn("B04", ids)

    def test_b04_has_java_and_web_minimal_prerequisites(self):
        ids = [n["id"] for n in route_need.minimum_prerequisites(self.nodes["B04"], self.nodes)]
        self.assertIn("B03", ids)
        self.assertIn("F01", ids)
        self.assertNotIn("F04", ids)

    def test_app_routes(self):
        self.assertIn("M01", [n["id"] for n in route_need.find("我要做微信小程序", self.nodes)])
        self.assertIn("A01", [n["id"] for n in route_need.find("Agent工具", self.nodes)])
        self.assertIn("B06", [n["id"] for n in route_need.find("SSE断连", self.nodes)])

    def test_known_node_and_unknown_query(self):
        self.assertEqual(route_need.find("B04", self.nodes)[0]["id"], "B04")
        self.assertEqual(route_need.find("不存在的神秘工具名", self.nodes), [])


if __name__ == "__main__":
    unittest.main()
