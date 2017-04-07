# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Version wildcards support for single '*' to match all.
- Added support to run a component server and handle a single request
  where the payload is send from the CLI in a JSON file (#72).

### Changed
- The wildcard ('*') in the last version part now matches any character.
- `HttpActionSchema.get_method()` now returns method names in lower case.

## [1.0.0] - 2017-03-07
- Initial release
