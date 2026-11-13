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
        self.assertIn("F11", [n["id"] for n in route_need.find("SSE断连", self.nodes)])


    def test_vue_nuxt_and_desktop_routes(self):
        self.assertIn("F08", [n["id"] for n in route_need.find("我要做Vue3后台", self.nodes)])
        self.assertIn("F09", [n["id"] for n in route_need.find("Nuxt SSR", self.nodes)])
        self.assertIn("M03", [n["id"] for n in route_need.find("Electron桌面应用", self.nodes)])
        self.assertIn("M04", [n["id"] for n in route_need.find("uni-app小程序", self.nodes)])

    def test_node_protocol_and_native_routes(self):
        self.assertIn("B07", [n["id"] for n in route_need.find("NestJS Node后端", self.nodes)])
        self.assertIn("F11", [n["id"] for n in route_need.find("WebSocket双向消息", self.nodes)])
        self.assertIn("A02", [n["id"] for n in route_need.find("MCP server工具", self.nodes)])
        self.assertIn("B08", [n["id"] for n in route_need.find("Go语言API", self.nodes)])

    def test_vue_prerequisites_and_refs(self):
        n = self.nodes["F08"]
        ids = [item["id"] for item in route_need.minimum_prerequisites(n, self.nodes)]
        self.assertIn("F02", ids)
        self.assertIn("F03", ids)
        self.assertNotIn("F04", ids)
        desc = route_need.describe(n, self.nodes)
        self.assertIn("vuejs.org", desc)
        self.assertIn("X-SuperPlay-AI-Learning-OS", desc)


    def test_all_nodes_have_real_learning_cards(self):
        self.assertEqual(42, len(self.nodes))
        needed = ("definition", "mechanism", "analogy", "boundary",
                  "study_url", "read_first", "lab", "failure", "upstream_role")
        for n in self.nodes.values():
            for field in needed:
                with self.subTest(node=n["id"], field=field):
                    self.assertTrue(n.get(field))

    def test_prerequisite_semantics_no_false_course_gate(self):
        self.assertNotIn("D01", self.nodes["B05"]["requires"])
        self.assertEqual([], self.nodes["M05"]["requires"])
        self.assertNotIn("F01", self.nodes["E02"]["requires"])
        self.assertNotIn("B01", self.nodes["D05"]["requires"])
        self.assertEqual(["F04"], self.nodes["F05"]["requires"])

    def test_task_vs_stream_protocol(self):
        self.assertIn("F11", [n["id"] for n in route_need.find("SSE断连", self.nodes)])
        self.assertIn("B06", [n["id"] for n in route_need.find("Celery任务崩溃", self.nodes)])
        self.assertNotIn("B06", [n["id"] for n in route_need.find("WebSocket双向", self.nodes)])

    def test_json_card_and_study_url(self):
        n = self.nodes["F08"]
        card = route_need.to_dict(n, self.nodes)
        self.assertTrue(card["study_url"].startswith("https://vuejs.org/"))
        self.assertIn("失败", card["failure"] + "失败")
        self.assertIn("definition", card)
        self.assertEqual("UNASSESSED", card["state"])

    def test_language_name_does_not_pollute_unrelated_routes(self):
        js_matches = [n["id"] for n in route_need.find("JavaScript asynchronous", self.nodes)]
        self.assertIn("F03", js_matches)
        self.assertNotIn("B03", js_matches)
        nest_matches = [n["id"] for n in route_need.find("NestJS controller", self.nodes)]
        self.assertIn("B07", nest_matches)
        self.assertNotIn("F03", nest_matches)

    def test_topological_minimal_prerequisites(self):
        deps = [n["id"] for n in route_need.minimum_prerequisites(self.nodes["F05"], self.nodes)]
        self.assertEqual(["F02", "F03", "F04"], deps)

    def test_known_node_and_unknown_query(self):
        self.assertEqual(route_need.find("B04", self.nodes)[0]["id"], "B04")
        self.assertEqual(route_need.find("不存在的神秘工具名", self.nodes), [])


if __name__ == "__main__":
    unittest.main()
