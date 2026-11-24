#!/usr/bin/env python3
"""Local lexical retrieval over the approved RAG index. No model or network calls."""
from __future__ import annotations
import argparse
import json
import math
import re
import unicodedata
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
DEFAULT_INDEX=ROOT/"data"/"rag-approved-index.json"
TOKEN=re.compile(r"[^\W_]+",re.UNICODE)
ALLOWED_LICENSES={"AARAMORA-OWNED","CC-BY-4.0"}

def tokens(value:str)->list[str]:
    normal=unicodedata.normalize("NFKC",value).casefold()
    return TOKEN.findall(normal)

def valid_entry(entry:dict[str,Any],today:date)->bool:
    required=("id","title","language","licenseId","sources","reviewer","reviewedOn","expiresOn","text")
    if any(not entry.get(k) for k in required):
        return False
    if entry["licenseId"] not in ALLOWED_LICENSES:
        return False
    if not entry["sources"] or not all(isinstance(x,str) and x.startswith("https://") for x in entry["sources"]):
        return False
    try:
        reviewed=date.fromisoformat(entry["reviewedOn"])
        expires=date.fromisoformat(entry["expiresOn"])
    except (TypeError,ValueError):
        return False
    return reviewed<=today and expires>=today

def search(index:dict[str,Any],query:str,limit:int=5,language:str|None=None,today:date|None=None)->dict[str,Any]:
    today=today or date.today()
    query_terms=tokens(query)
    if not query_terms:
        return {"mode":"lexical_no_model","status":"empty_query","results":[]}
    if index.get("schemaVersion")!=1 or index.get("approvedEntryCount")!=len(index.get("entries",[])):
        return {"mode":"lexical_no_model","status":"invalid_index","results":[]}
    entries=[e for e in index.get("entries",[]) if isinstance(e,dict) and valid_entry(e,today)]
    if language:
        entries=[e for e in entries if e.get("language")==language]
    if not entries:
        return {"mode":"lexical_no_model","status":"no_approved_passages","results":[]}
    documents=[]
    df=Counter()
    for entry in entries:
        body=tokens(entry.get("text",""))
        title=tokens(entry.get("title",""))
        tags=tokens(" ".join(entry.get("tags",[])))
        combined=body+title*3+tags*2
        freq=Counter(combined)
        documents.append((entry,body,title,tags,freq,len(body)))
        df.update(set(combined))
    count=len(documents)
    avg_len=sum(item[5] for item in documents)/max(1,count)
    k1=1.5
    b=0.75
    scored=[]
    for entry,body,title,tags,freq,length in documents:
        score=0.0
        for term in set(query_terms):
            if term not in freq:
                continue
            idf=math.log(1+(count-df[term]+0.5)/(df[term]+0.5))
            tf=freq[term]
            denom=tf+k1*(1-b+b*length/max(1,avg_len))
            score+=idf*(tf*(k1+1))/denom
            if term in title:
                score+=1.25
            if term in tags:
                score+=0.5
        if score>0:
            text=entry["text"].strip()
            excerpt=text[:440].rstrip()
            if len(text)>440:
                excerpt+="…"
            scored.append({
                "id":entry["id"],
                "title":entry["title"],
                "language":entry["language"],
                "score":round(score,4),
                "excerpt":excerpt,
                "sources":entry["sources"],
                "licenseId":entry["licenseId"],
                "reviewer":entry["reviewer"],
                "reviewedOn":entry["reviewedOn"],
                "expiresOn":entry["expiresOn"]
            })
    scored.sort(key=lambda x:(-x["score"],x["title"].casefold()))
    if not scored:
        status="no_matching_passage"
    else:
        status="matches"
    return {"mode":"lexical_no_model","status":status,"results":scored[:max(1,min(limit,20))]}

def main()->int:
    parser=argparse.ArgumentParser(description="Search AARAMORA's approved local passages without an LLM.")
    parser.add_argument("query",help="Question or search terms")
    parser.add_argument("--index",type=Path,default=DEFAULT_INDEX)
    parser.add_argument("--language",choices=("en","hi","mr","hinglish"))
    parser.add_argument("--limit",type=int,default=5)
    parser.add_argument("--today",help="ISO date override for deterministic review-expiry checks")
    args=parser.parse_args()
    index=json.loads(args.index.read_text(encoding="utf-8"))
    today=date.fromisoformat(args.today) if args.today else date.today()
    result=search(index,args.query,args.limit,args.language,today)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
