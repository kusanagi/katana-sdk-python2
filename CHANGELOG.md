# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.1.1] - Unreleased
### Changed
- Callback for `Component.set_resource()` now receives the component as
  the first argument.
- Header methods are now case insensitive.

### Added
- Support for SDK process execution timeout per request.
- Request and response header related methods.
- `Api.has_variable()` was added to check if a variable exists.

## [1.1.0] - 2017-06-01
### Added
- Added support to get service return value in response middlewares.
- Added getter for origin duration to transport.
- Added "binary" type support for parameters and return value.

### Changed
- Updated CONTRIBUTING.md and README.md

## [1.0.1] - 2017-04-28
### Added
- Version wildcards support for single '*' to match all.
- Added support to run a component server and handle a single request
  where the payload is send from the CLI in a JSON file (#72).

### Changed
- The wildcard ('*') in the last version part now matches any character.
- `HttpActionSchema.get_method()` now returns method names in lower case.

### Fixed
- Engine variables now works with request and response middlewares.

## [1.0.0] - 2017-03-07
- Initial release.
