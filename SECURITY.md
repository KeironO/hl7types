# Security Policy

## Supported versions

The following versions of `hl7types` are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.9.x   | :white_check_mark: |
| < 0.9.0 | :x:                |

## Reporting a vulnerability

If you discover a security vulnerability in `hl7types`, please report it privately.

**Do not open a public issue.** Instead, send an email to:

- **Keiron O'Shea** <keiron@keiron.xyz>

Please include:

- A clear description of the vulnerability.
- Steps to reproduce the issue, or a proof-of-concept if possible.
- The affected version(s).
- Any suggested remediation, if you have one.

You can expect an initial response within **7 days**. We will work with you to validate the issue and agree on a disclosure timeline before any public announcement is made.

## Disclosure policy

Once a vulnerability is confirmed, we will:

1. Develop and test a fix.
2. Prepare a security release and release notes describing the vulnerability in general terms.
3. Request a CVE if the vulnerability warrants one.
4. Coordinate public disclosure after a fix is available.

We credit reporters who wish to be named in the release notes and security advisory.

## Security-related design decisions

- XML parsing uses [`defusedxml`](https://github.com/tiran/defusedxml) to mitigate XML external entity and entity expansion attacks.
- Generated HL7 model code is treated as untrusted input during decoding and is validated against Pydantic schemas.
