# AARAMORA Brand Film Assets

Approved first campaign exports supplied on 2026-11-24.

## Files

| Local filename | Intended repository path | Format | Duration | Resolution | FPS | Codec | Size |
|---|---|---:|---:|---:|---:|---|---:|
| AARAMORA_MASTER_16_9(2).mp4 | assets/brand-film/aaramora-master-16x9.mp4 | 16:9 | 33.325 s | 1920x1080 | 30 | H.264 + AAC | 12,114,271 bytes |
| AARAMORA_INSTAGRAM_9_16(2).mp4 | assets/brand-film/aaramora-instagram-9x16.mp4 | 9:16 | 33.325 s | 1080x1920 | 30 | H.264 + AAC | 10,346,721 bytes |
| AARAMORA_CLEAN_NO_ADDED_AUDIO(2).mp4 | Not stored separately | 16:9 | 33.325 s | 1920x1080 | 30 | H.264 + AAC | 12,114,271 bytes |

## Important verification note

The uploaded file named `AARAMORA_CLEAN_NO_ADDED_AUDIO(2).mp4` is byte-identical to `AARAMORA_MASTER_16_9(2).mp4` (SHA-256: `df610b81b9f6f4f0a79fe1a573c8c3922cbdebd6a4cd6f0341c3cb2c4b848487`) and contains an AAC audio stream. It is therefore not a silent/no-added-audio master. Keep one landscape master in Git and do not store the duplicate.

Vertical export SHA-256: `053d2f79b0990325b408542c4e2c1f13ead8c5e88e39cfa950f0f7c6090deb0c`.

## Website usage

- The repository stores the two MP4s at the paths in the table above.
- The homepage uses a user-initiated video with native controls, `preload=none`, `playsinline` and a poster image. It does not autoplay.
- In the deployed static snapshot, video URLs are served from jsDelivr's GitHub CDN path for the same committed files, avoiding a second binary transfer into the Vercel project.
- Use the vertical file for social previews and mobile-first campaign placements.
- Do not autoplay audio. Respect reduced-motion and data-saver preferences. Provide a poster image and accessible description.
- Avoid loading the video until the visitor explicitly starts it.

## Campaign sequence

1. The Quiet Morning
2. A Moment of Care
3. Thoughts on Paper
4. A Place to Breathe
5. You Are Not Alone
6. AARAMORA Brand Reveal

Tagline: **A gentle place to begin again.**

## Current upload status

**Status: committed to GitHub**

Both unique MP4 files are present on the `main` branch at the paths listed in the Files table. They were added in commit `12126e3223df930568ed2ffc71a118cc90803782`.

The landscape master is 12,114,271 bytes and the vertical edit is 10,346,721 bytes. The duplicate `CLEAN_NO_ADDED_AUDIO` export is intentionally excluded. No local upload step is pending.