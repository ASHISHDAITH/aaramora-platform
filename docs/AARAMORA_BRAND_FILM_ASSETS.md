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

- The homepage film section uses `assets/brand-film/aaramora-master-16x9.mp4` as a user-initiated video with native controls, `preload=none`, `playsinline` and a poster image. It does not autoplay.
- Use `assets/brand-film/aaramora-instagram-9x16.mp4` for vertical social previews and mobile-first campaign placements.
- Do not autoplay audio. Respect reduced-motion and data-saver preferences. Provide a poster image and accessible description.
- Avoid loading the video on low-bandwidth connections unless the visitor explicitly starts it.

## Campaign sequence

1. The Quiet Morning
2. A Moment of Care
3. Thoughts on Paper
4. A Place to Breathe
5. You Are Not Alone
6. AARAMORA Brand Reveal

Tagline: **A gentle place to begin again.**

## Current upload status

This manifest records the inspected local exports. The MP4 binary files have **not yet been uploaded to GitHub**. The GitHub connector available in this session supports text writes but no direct binary asset upload/release action. Upload the two unique MP4s from a local checkout using the commands below.

```powershell
$repoRoot = git rev-parse --show-toplevel
if (-not $repoRoot) { throw "Run this inside your local aaramora-platform clone." }

$mediaDir = "C:\viedo\AARAMORA_FINAL"
$targetDir = Join-Path $repoRoot "assets/brand-film"
$master = Join-Path $mediaDir "AARAMORA_MASTER_16_9.mp4"
$instagram = Join-Path $mediaDir "AARAMORA_INSTAGRAM_9_16.mp4"
$clean = Join-Path $mediaDir "AARAMORA_CLEAN_NO_ADDED_AUDIO.mp4"

foreach ($path in @($master, $instagram, $clean)) {
  if (-not (Test-Path -LiteralPath $path)) { throw "Missing media file: $path" }
}

New-Item -ItemType Directory -Force $targetDir | Out-Null
Copy-Item -LiteralPath $master -Destination (Join-Path $targetDir "aaramora-master-16x9.mp4") -Force
Copy-Item -LiteralPath $instagram -Destination (Join-Path $targetDir "aaramora-instagram-9x16.mp4") -Force

$masterHash = (Get-FileHash -LiteralPath $master -Algorithm SHA256).Hash
$cleanHash = (Get-FileHash -LiteralPath $clean -Algorithm SHA256).Hash
if ($masterHash -eq $cleanHash) {
  Write-Host "Clean file is identical to the landscape master; not adding a duplicate."
} else {
  Write-Warning "Clean file differs from the master. Inspect its audio stream with ffprobe before deciding whether to add it."
}

git -C $repoRoot add -- assets/brand-film
git -C $repoRoot status --short
git -C $repoRoot commit -m "Add AARAMORA brand film exports"
git -C $repoRoot push origin main
```

This stages the two unique campaign exports. The clean file is compared by SHA-256 first; if it differs, inspect its audio stream before adding it as a separate asset.
