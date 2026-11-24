import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from build_reviewed_corpus import build, eligible

class ReviewedCorpusGateTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        (self.root/"content").mkdir()
        (self.root/"content"/"guide.md").write_text("A reviewed owned passage.",encoding="utf-8")
        self.good={
            "id":"guide-1","title":"Owned guide","file":"content/guide.md",
            "language":"en","licenseId":"AARAMORA-OWNED",
            "sources":["https://example.org/source"],"owner":"AARAMORA editor",
            "reviewer":"Named qualified reviewer","reviewedOn":"2026-01-01",
            "expiresOn":"2027-01-01","approvalStatus":"approved",
            "contentStatus":"current","audience":"public","tags":["wellbeing"],\n            "rightsVerified":True,"rightsReviewer":"Named rights reviewer","rightsCheckedOn":"2026-02-01"
        }
    def tearDown(self):
        self.temp.cleanup()
    def test_only_signed_current_rights_eligible_items_are_indexed(self):
        result=build({"entries":[self.good]},self.root,date(2026,11,24))
        self.assertEqual(1,result["approvedEntryCount"])
        self.assertEqual("A reviewed owned passage.",result["entries"][0]["text"])
        self.assertFalse(result["runtimeEnabled"])
        self.assertFalse(result["llmEnabled"])
    def test_draft_or_unsigned_content_is_excluded(self):
        item={**self.good,"approvalStatus":"pending"}
        result=build({"entries":[item]},self.root,date(2026,11,24))
        self.assertEqual(0,result["approvedEntryCount"])
        self.assertEqual("not_signed_approved",result["excluded"][0]["reason"])
    def test_expired_content_is_excluded(self):
        item={**self.good,"expiresOn":"2026-11-23"}
        result=build({"entries":[item]},self.root,date(2026,11,24))
        self.assertEqual("expired",result["excluded"][0]["reason"])
    def test_missing_reviewer_or_sources_is_excluded(self):
        for change in ({"reviewer":""},{"sources":[]}):
            item={**self.good,**change}
            ok,reason=eligible(item,self.root,date(2026,11,24))
            self.assertFalse(ok)
    def test_unapproved_third_party_license_is_excluded(self):
        item={**self.good,"licenseId":"CC-BY-NC-ND-4.0"}
        ok,reason=eligible(item,self.root,date(2026,11,24))
        self.assertFalse(ok)
        self.assertEqual("rights_not_allowlisted",reason)
    def test_cc_by_item_without_exact_rights_review_is_excluded(self):\n        item={**self.good,"licenseId":"CC-BY-4.0","rightsVerified":False}\n        ok,reason=eligible(item,self.root,date(2026,11,24))\n        self.assertFalse(ok)\n        self.assertEqual("rights_review_missing",reason)\n    def test_path_traversal_and_outside_paths_are_excluded(self):
        item={**self.good,"file":"../secret.txt"}
        ok,reason=eligible(item,self.root,date(2026,11,24))
        self.assertFalse(ok)
        self.assertEqual("unsafe_file_path",reason)
    def test_manifest_defaults_to_no_indexed_content(self):
        manifest=json.loads((ROOT/"data/rag-corpus-manifest.json").read_text(encoding="utf-8"))
        result=build(manifest,ROOT,date(2026,11,24))
        self.assertEqual(0,result["approvedEntryCount"])
        self.assertEqual([],result["entries"])
        self.assertFalse(result["llmEnabled"])

if __name__=="__main__": unittest.main()
