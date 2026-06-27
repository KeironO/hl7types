# Changelog

All notable changes to hl7types are documented here.

## [0.9.0] :  2026-06-27

### Changes

- Update changelog
- Updated noxfile to include 3.14
- Extended ci/cd tox to include python 3.14
- 68: intelligent dt dtm parserer (#69)

### Chores

- Chore(deps-dev): bump pytest from 9.0.3 to 9.1.0
- Chore(deps-dev): bump ruff from 0.15.15 to 0.15.17
- Chore(deps-dev): bump pyright from 1.1.409 to 1.1.410
- Chore(deps-dev): bump hatchling from 1.29.0 to 1.30.1
- Chore(deps-dev): bump ruff from 0.15.17 to 0.15.18
- Chore(deps-dev): bump ruff from 0.15.18 to 0.15.19 (#65)
- Chore(deps-dev): bump pytest from 9.1.0 to 9.1.1 (#62)
- Chore(deps-dev): bump pyright from 1.1.410 to 1.1.411 (#66)
- Chore(deps-dev): bump ruff from 0.15.19 to 0.15.20 (#67)

## [0.8.0] :  2026-06-15

### Bug Fixes

- Fixed global private calls from old version
- Fixed ruff on __init__.py in hl7

### Changes

- Update changelog
- Added uv lock and began smoketests
- Smoke-tests added
- Version 0.8.0
- Glob removed from github action, worked fine on act runner!
- Forgot about active flag to keep venv seperated
- Python 3.12 problems solved due to X | Y union syntax producing a different type at runtime

## [0.7.4] :  2026-06-15

### Changes

- Update changelog
- Added pep-561 support and bumped version

## [0.7.3] :  2026-06-14

### Bug Fixes

- Fixed ET import since moved over to defusedxml

### Changes

- Changelog-new (#47)
- Update changelog.yml
- Update changelog (#48)
- Added defusedxml support
- Simplified pyright runs
- Improved typechecking on error builder
- Cleaned up types to resolve pyright issues
- Bumped version to 0.7.3

## [0.7.1] :  2026-06-13

### Bug Fixes

- Fixed issue with changelog (#44)
- Fixed issue with docstring and wrote small test to ensure pid3 handling (#45)

### Changes

- Added changelog (#43)
- Remove changelog build (#46)

## [0.7.0] :  2026-06-09

### Changes

- Clean up (#39)

## [0.6.0] :  2026-06-07

### Changes

- Model changes (#32)
- Model changes (#37)

## [0.5.1] :  2026-06-06

### Changes

- Expand-scope (#30)
- Bumped-version-to-0.5.1 (#31)

## [0.5.0] :  2026-06-05

### Testing

- Testing (#29)

## [0.4.4] :  2026-06-04

### Bug Fixes

- Fixed docs up and pushed version (#27)

### Changes

- Hl7-profile-conformance (#24)
- Block unblock (#26)

## [0.4.3] :  2026-06-02

### Changes

- Dump of docs (#23)

## [0.4.2] :  2026-06-01

### Changes

- Better validation of datatypes (#21)

## [0.4.1] :  2026-05-31

### Documentation

- Docstring updated (#19)

## [0.4.0] :  2026-05-31

### Changes

- Znd mishandling (#18)

## [0.3.3] :  2026-05-31

### Changes

- Lazy import fixes two electric boogaloo (#17)

## [0.3.2] :  2026-05-31

### Changes

- Cleaned up encoder to deal with registry decoding and encoding … (#16)

## [0.3.1] :  2026-05-31

### Changes

- Added readthedocs (#12)
- Lazy import fixes (#15)

## [0.3.0] :  2026-05-30

### Changes

- The registry (#11)

## [0.2.0] :  2026-05-30

### Changes

- Basemodel fixes (#10)

## [0.1.4] :  2026-05-29

### Changes

- Create dependabot.yml
- Update dependabot.yml
- Strict parsing (#7)

## [0.1.3] :  2026-05-28

### Changes

- More tests added and improved tooling (#5)

## [0.1.2] :  2026-05-28

### Changes

- Added basic testing from laptop, need much more (#4)

## [0.1.1] :  2026-05-28

### Changes

- Made less restrictive and bumped version

## [0.1.0] :  2026-05-28

### Bug Fixes

- Fixed fixtures stuff

### Changes

- Initial commit
- Initial dump of code, need major refactoring
- Added basemodel hack
- Added xml export too
- Added README
- Added precommit with ruff
- Lets see what happens
- Build and release

