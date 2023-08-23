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
