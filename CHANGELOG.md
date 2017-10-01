# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [1.2.1] - 2017-10-01
## Changed
- Running a service with an action input payload now flushes the output
  right after the print.
- File payload have a name and is now added to transport as a list of
  files instead of a dict.

## [1.2.0] - 2017-09-01
### Changed
- Callback for `Component.set_resource()` now receives the component as
  the first argument.
- Header methods are now case insensitive.

### Added
- Support for SDK process execution timeout per request.
- Request and response header related methods.
- `Api.has_variable()` was added to check if a variable exists.
- Request attributes support.

### Fixed
- Service schema resolution now supports services that contain
  "/" in their name.
- File parameters now work for service to service calls.

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
