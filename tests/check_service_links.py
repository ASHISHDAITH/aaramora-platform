import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"data/service-links.json").read_text(encoding="utf-8"))
class PublicSupportNumberGateTests(unittest.TestCase):
    def test_only_two_numbers_are_marked_for_public_display(self):
        visible=[]
        for record in DATA["records"]:
            for number in record.get("displayedNumbers",[]):
                visible.append(str(number.get("tel","")))
        self.assertTrue(visible)
        self.assertTrue(set(visible).issubset({"14416","112"}))
        self.assertIn("14416",visible)
        self.assertIn("112",visible)
    def test_alternative_tele_manas_number_is_not_public(self):
        tele=next(r for r in DATA["records"] if r["id"]=="tele-manas")
        shown=[str(x.get("tel","")) for x in tele.get("displayedNumbers",[])]
        self.assertEqual(shown,["14416"])
        self.assertNotIn("18008914416",shown)
        self.assertNotIn("1800-89-14416",shown)
    def test_womens_helpline_candidate_is_not_public_until_signoff(self):
        candidates=[r for r in DATA["records"] if "181" in json.dumps(r)]
        for record in candidates:
            self.assertEqual(record.get("displayedNumbers",[]),[])
            self.assertEqual(record.get("humanSignOff"),"pending")
    def test_public_display_policy_is_explicit(self):
        self.assertIn("only Tele-MANAS 14416",DATA["policy"]["description"])
        self.assertIn("named human",DATA["policy"]["description"])
if __name__=="__main__":unittest.main()
