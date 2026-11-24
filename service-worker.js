"use strict";
const CACHE_NAME="aaramora-support-v1";
const CORE=[
"/","/index.html","/get-help.html","/offline.html","/site.css","/site.js","/favicon.svg","/manifest.webmanifest",
"/assets/reading-library-book-still-life.webp",
"/assets/illustrations/journal.svg","/assets/illustrations/garden.svg","/assets/illustrations/appointment.svg",
"/assets/healing-garden.svg","/assets/safe-corner.svg","/assets/thought-river.svg"
];
self.addEventListener("install",event=>{
 event.waitUntil(caches.open(CACHE_NAME)
  .then(cache=>cache.addAll(CORE))
  .then(()=>self.skipWaiting()));
});
self.addEventListener("activate",event=>{
 event.waitUntil(caches.keys()
  .then(keys=>Promise.all(keys.filter(key=>key.startsWith("aaramora-")&&key!==CACHE_NAME).map(key=>caches.delete(key))))
  .then(()=>self.clients.claim()));
});
self.addEventListener("fetch",event=>{
 const request=event.request;
 if(request.method!=="GET")return;
 const url=new URL(request.url);
 if(url.origin!==self.location.origin)return;
 if(request.mode==="navigate"){
  event.respondWith(fetch(request).then(response=>{
   if(response&&response.ok){const copy=response.clone();caches.open(CACHE_NAME).then(cache=>cache.put(request,copy));}
   return response;
  }).catch(()=>caches.match(request).then(hit=>hit||caches.match("/offline.html")));
  return;
 }
 event.respondWith(caches.match(request).then(hit=>hit||fetch(request).then(response=>{
  if(response&&response.ok){const copy=response.clone();caches.open(CACHE_NAME).then(cache=>cache.put(request,copy));}
  return response;
 }).catch(()=>Response.error())));
});