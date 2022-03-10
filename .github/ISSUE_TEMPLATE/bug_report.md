---
name: Bug report
about: Report a bug in tutor-contrib-retirement
title: ''
labels: ''
assignees: ''

---

# Summary

Replace this with a short summary (one sentence or short paragraph) of the issue you are seeing.

## What I did

Explain the steps you undertook that led to the unexpected behavior you are observing. Please include relevant documentation snippets, such as the `RETIREMENT_*` settings from Tutor’s `config.yml`.

It’s OK to remove or mask credentials, but otherwise try to err on the side of sharing more rather than less information.

## What I expected to happen

Explain how you expected Tutor to behave with your configuration.

## What actually happened

Explain how Tutor behaved differently than you expected.

## My environment

Please add some information about the environment that you’re working in. At a minimum, include these items:

* Tutor version: (Insert the Tutor version you are using.)
* `tutor-contrib-retirement` version: (Insert the plugin version you are using. If you installed from Git, enter the tag or branch name, or the commit reference.)
* Output of the retirement command/CronJob: (In Tutor local, this is the output of the `tutor local retire-users`. In Kubernetes, you can get the output by `kubectl -n <your-namespace> logs <retirement-pod-name>`)

Additionally, you might also want to add any of the items below, if you think they might be relevant to the bug:

* Kubernetes versions: (If you are reporting a bug that applies to deploying this plugin with `tutor k8s`, add your `kubectl version` output. Otherwise, remove this item.)
* Docker/Podman version: (If you are running `tutor local`, the output of `docker version` might be relevant.)

Make sure to redact any sensitive information regarding your users and products.

## Additional context

If there’s any other context you’d like to share, please add it here. Otherwise, you can delete this section.