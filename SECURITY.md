# Security and privacy

This repository is an early static prototype. It is not a service for receiving, storing or processing user health information.

## Do not submit
- API keys, access tokens, passwords or private keys.
- Real mental-health messages, diaries, screening answers, crisis disclosures or medical records.
- Identifiable research-participant or lived-experience co-design data.

## Reporting
Do not create a public issue containing sensitive data or a suspected exploitable vulnerability. Contact the repository owner privately through GitHub's security reporting or other private channel.

## Current prototype data behaviour
The current `index.html` uses in-memory UI state only and has no backend, analytics, external scripts or persistence. The Quick Exit action navigates to `about:blank`; it does not erase browser history, network logs or activity recorded by a shared device. Verify the deployed code and network behaviour before making any stronger privacy promise.