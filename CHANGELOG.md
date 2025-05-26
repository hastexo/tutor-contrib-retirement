## Version 5.2.1 (2025-05-26)

* [Chore] Create a new patch release for a convenient `sumac.3` upgrade.

## Version 5.2.0 (2025-04-15)

* [Enhancement] Allow to override the Dockerfile base image.

## Version 5.1.0 (2025-01-03)

* [Enhancement] Support Tutor 19 and Open edX Sumac.

## Version 5.0.0 (2024-10-07)

* Drop support for Python 3.8.

When updating your plugin to this version, you'll need to rebuild the image.

## Version 4.0.0 (2024-08-06)

* [BREAKING CHANGE] Add support for Tutor 18 and Open edX Redwood.
  The Tubular repository has been deprecated and the relevant scripts
  have been moved to the `edx-platform` repository (https://github.com/openedx/axim-engineering/issues/881); the plugin now installs the scripts from there.

## Version 3.4.0 (2024-08-01)

* [Bug fix] Complete the removal of (not-ever-working) support for the Ecommerce service, by also removing references to that service from the `openedx-lms-common-settings` patch.
* [Bug fix] Remove references to the mailing API (which in turn was removed from the LMS in Ironwood).
* [Bug fix] Remove references to the (not-ever-working) Discovery service.
* [Bug fix] Run the retirement pipeline for course enrollments prior to that for forum posts.

## Version 3.3.1 (2024-07-03)

* [Bug fix] Drop support for retiring users in the [Open edX E-Commerce Service](https://github.com/openedx/ecommerce).
  Per the discussion in [Issue #36](https://github.com/hastexo/tutor-contrib-retirement/issues/36), account retirement for the E-Commerce Service "will never" work and "has never" worked, thus this is not a breaking change.

## Version 3.3.0 (2024-04-05)

* [Enhancement] Support Python 3.12.

## Version 3.2.0 (2024-01-12)

* [Enhancement] Support Tutor 17 and Open edX Quince.

## Version 3.1.0 (2023-11-20)

* [Enhancement] Support the Open edX `palm.4` release.

## Version 3.0.0 (2023-10-25)

* [Enhancement] Support the Open edX `palm.3` release. Drop
  compatibility with Open edX Olive.

## Version 2.1.0 (2023-08-23)

* [Enhancement] Support Tutor 16 and Open edX Palm, Python 3.10, and Python 3.11.

## Version 2.0.0 (2023-03-20)

* [BREAKING CHANGE] Add support for Tutor 15 and Open edX Olive.
  Tutor version 15.0.0 includes changes to the implementation of
  custom commands and thus requires changes in this plugin as well
  that are not backwards compatible.
  From version 2.0.0 this plugin only supports Tutor versions
  from 15.0.0 and Open edX Olive release.

## Version 1.0.0 (2022-08-09)

* [BREAKING CHANGE] Support Tutor 14 and Open edX Nutmeg. This entails
  a configuration format change from JSON to YAML, meaning that from
  version 1.0.0 this plugin only supports Tutor versions from 14.0.0
  (and with that, only Open edX versions from Nutmeg).

## Version 0.1.0 (2022-06-29)
￼
￼* Use Tutor v1 plugin API

## Version 0.0.1 (2022-03-09)

**Experimental. Do not use in production.**

* Add a Kubernetes CronJob that runs the retirement pipeline based on
  the schedule defined in the `K8S_CRONJOB_SCHEDULE` configuration
  parameter.
* Add `retire-users` command to `tutor local` to run the retirement pipeline
* Add retirement-job service
* Add basic testing via tox
* Initial Git import
