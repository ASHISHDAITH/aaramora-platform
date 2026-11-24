import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PROMPT=(ROOT/"docs/rag/SYSTEM_PROMPT_V2.md").read_text(encoding="utf-8")
DRAFT=(ROOT/"docs/rag/CRISIS_TEMPLATE_REVIEW_DRAFT.md").read_text(encoding="utf-8")
POLICY=json.loads((ROOT/"data/rag-ingestion-policy.json").read_text(encoding="utf-8"))
MANIFEST=json.loads((ROOT/"data/rag-corpus-manifest.json").read_text(encoding="utf-8"))
FIXTURES=[json.loads(x) for x in (ROOT/"tests/fixtures/hinglish-redteam-v2.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
class RagReleaseGateTests(unittest.TestCase):
    def test_prompt_is_draft_and_has_external_deterministic_crisis_gate(self):
        self.assertIn("REVIEW DRAFT",PROMPT)
        self.assertIn("before generation",PROMPT)
        self.assertIn("skip the LLM call",PROMPT)
        self.assertIn("[[CRISIS_TEMPLATE]]",PROMPT)
    def test_only_current_public_national_routes_are_named(self):
        self.assertIn("14416",PROMPT)
        self.assertIn("112",PROMPT)
        for forbidden in ("1800-891-4416","1800-89-14416","181"):
            self.assertNotIn(forbidden,PROMPT)
    def test_crisis_script_is_not_approved(self):
        self.assertIn("NOT APPROVED",DRAFT)
        self.assertIn("UNASSIGNED",DRAFT)
        self.assertIn("Permission to deploy",DRAFT)
    def test_corpus_and_runtime_are_default_deny(self):
        self.assertFalse(POLICY["runtimeEnabled"])
        self.assertFalse(POLICY["modelCallsEnabled"])
        self.assertEqual([],POLICY["approvedItems"])
        self.assertEqual([],MANIFEST["entries"])
        self.assertFalse(MANIFEST["runtimeEnabled"])
    def test_rights_policy_keeps_restricted_sources_link_only(self):
        names={x["name"] for x in POLICY["linkOnlyOrNoIngestion"]}
        for required in ("OpenStax Psychology 2e","SuttaCentral","CCI workbooks","Jain eLibrary","Sikher translations","BaniDB translations","Quran translations","Gita Supersite translations"):
            self.assertIn(required,names)
        self.assertFalse(POLICY["candidatePendingExactLicenceCheck"][0]["allowedForIngestion"])
    def test_exactly_100_synthetic_hinglish_cases_are_present(self):
        self.assertEqual(100,len(FIXTURES))
        self.assertEqual(100,len({x["id"] for x in FIXTURES}))
        self.assertTrue(all(x["language"]=="hinglish" and x["synthetic"] for x in FIXTURES))
        self.assertGreaterEqual(sum(x["category"]=="jailbreak_prompt_injection" for x in FIXTURES),10)
        self.assertGreaterEqual(sum(x["expectedRoute"]=="FIXED_CRISIS" for x in FIXTURES),30)
    def test_fixture_text_does_not_contain_personal_identifiers(self):
        full=" ".join(x["message"] for x in FIXTURES).lower()
        for marker in ("@gmail.com","@yahoo.com","+91-","aadhaar","passport number"):
            self.assertNotIn(marker,full)
if __name__=="__main__": unittest.main()
