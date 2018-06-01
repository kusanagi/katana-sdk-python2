# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Changed
- Modified "api" module to comply with SDK specs.

## [2.0.0] - 2018-03-01
### Added
- A configured file server must be available to make runtime calls
  that send file parameters.
- Added "log-level" support to runner.
- Implemented support for the Transport API.

### Changed
- Calls to `Api.done()` raise an exception now.
- Action schema entity's primary key field name is getted from the
  entity instead of the action.
- Removed `ActionSchema.get_primary_key()`
- Removed the "quiet" CLI flag.
- Logging changed to support the new Syslog based logging from KATANA.

## [1.3.0] - 2017-11-01
### Added
- Support for action tags defined in the configuration.
- Request ID to logs.
- Component and framework info was added to log prefix.

### Changed
- Runtime call default timeout to 10000.
- Parameter schema default value getter now returns None by default.

### Fixed
- Error payload handling during runtime calls

### Fixed
- Component.log() now includes the date and [SDK] prefix.

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
