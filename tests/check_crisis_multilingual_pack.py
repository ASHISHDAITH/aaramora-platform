import json
import unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PACK=[json.loads(line) for line in (ROOT/"tests/fixtures/crisis-multilingual-301-v1.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
class MultilingualCrisisPackTests(unittest.TestCase):
    def test_pack_has_301_cases_across_four_languages(self):
        self.assertEqual(301,len(PACK))
        self.assertEqual(301,len({x["id"] for x in PACK}))
        self.assertEqual({"en":67,"hi":67,"mr":67,"hinglish":100},dict(Counter(x["language"] for x in PACK)))
    def test_all_cases_are_synthetic_and_waiting_for_human_review(self):
        self.assertTrue(all(x["synthetic"] for x in PACK))
        self.assertTrue(all(x["clinicalLabelStatus"]=="clinician_and_safeguarding_review_pending" for x in PACK))
        self.assertTrue(all(x["languageReviewStatus"].endswith("review_pending") for x in PACK))
    def test_required_risk_groups_are_present(self):
        groups={x["category"] for x in PACK}
        for group in ("direct_self_harm","indirect_suicidal","self_harm_urge","harm_to_others","abuse_immediate_danger","postpartum_urgent","acute_panic_dissociation","jailbreak_prompt_injection"):
            self.assertIn(group,groups)
    def test_fixture_routes_are_provisional_fixed_handoffs(self):
        allowed={"FIXED_CRISIS","FIXED_SAFETY_HANDOFF","FIXED_CRISIS_REVIEW","PROMPT_INJECTION_IGNORED","RETRIEVE_OR_ABSTAIN","ABSTAIN"}
        self.assertTrue(all(x["expectedRoute"] in allowed for x in PACK))
if __name__=="__main__":unittest.main()
