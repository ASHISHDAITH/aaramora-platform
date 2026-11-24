import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from search_reviewed_corpus import search

class LocalLexicalRetrievalTests(unittest.TestCase):
    def setUp(self):
        self.today=date(2026,11,24)
        self.index={
            "schemaVersion":1,
            "approvedEntryCount":2,
            "entries":[
                {"id":"sleep-1","title":"Sleep and rest","language":"en","licenseId":"AARAMORA-OWNED",
                 "sources":["https://example.org/sleep"],"reviewer":"Named clinician",
                 "reviewedOn":"2026-01-01","expiresOn":"2027-01-01",
                 "tags":["sleep","rest"],"text":"Sleep routines can support everyday rest. Discuss persistent sleep problems with a qualified clinician."},
                {"id":"relationship-1","title":"Relationship boundaries","language":"en","licenseId":"CC-BY-4.0",
                 "sources":["https://example.org/boundaries"],"reviewer":"Named editor",
                 "reviewedOn":"2026-02-01","expiresOn":"2027-02-01",
                 "tags":["relationships","boundaries"],"text":"A boundary describes what you will choose or accept in a relationship."}
            ]
        }
    def test_returns_ranked_source_linked_passages_without_model(self):
        result=search(self.index,"sleep routines",today=self.today)
        self.assertEqual("lexical_no_model",result["mode"])
        self.assertEqual("matches",result["status"])
        self.assertEqual("sleep-1",result["results"][0]["id"])
        self.assertEqual(["https://example.org/sleep"],result["results"][0]["sources"])
    def test_empty_approved_index_abstains(self):
        result=search({"schemaVersion":1,"approvedEntryCount":0,"entries":[]},"anxiety",today=self.today)
        self.assertEqual("no_approved_passages",result["status"])
        self.assertEqual([],result["results"])
    def test_expired_and_unreviewed_passages_are_excluded(self):
        index={**self.index,"entries":self.index["entries"]+[{
            "id":"draft","title":"Draft anxiety page","language":"en","licenseId":"AARAMORA-OWNED",
            "sources":["https://example.org/draft"],"reviewer":"Pending",
            "reviewedOn":"2026-01-01","expiresOn":"2026-01-01","tags":["anxiety"],
            "text":"Anxiety may be described in general terms."
        }],"approvedEntryCount":3}
        result=search(index,"anxiety",today=self.today)
        self.assertEqual("no_matching_passage",result["status"])
    def test_language_filter_is_respected(self):
        result=search(self.index,"sleep",language="hi",today=self.today)
        self.assertEqual("no_approved_passages",result["status"])
    def test_missing_rights_metadata_is_not_returned(self):
        bad={**self.index,"entries":[{**self.index["entries"][0],"licenseId":"link-only"}],"approvedEntryCount":1}
        result=search(bad,"sleep",today=self.today)
        self.assertEqual("no_approved_passages",result["status"])
    def test_empty_query_abstains(self):
        result=search(self.index,"  !!! ",today=self.today)
        self.assertEqual("empty_query",result["status"])
if __name__=="__main__":unittest.main()
