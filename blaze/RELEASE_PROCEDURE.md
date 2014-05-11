﻿Blaze Release Procedure
=======================

This document describes the steps to follow to release
a new version of Blaze.

1. Update version numbers in the following locations:

 * /setup.py, in the setup(...) call.
 * /README.md where it mentions the current release.
 * /blaze/__init__.py

1. Confirm the dependencies and their version numbers in
   /docs/installing
   /requirements.txt

   In particular, `blz`, `dynd-python`, etc
   will typically be released concurrently with `blaze`,
   so they need to be updated to match.

1. Update the release notes /docs/source/releases.rst
   You may use a github URL like https://github.com/ContinuumIO/blaze/compare/0.4.2...master for assistance.

1. Build and update the documentation in gh-pages.

1. Verify build is working on all platforms. The
   jenkins builder internal to Continuum can assist
   with this.

1. Tag the release version.

1. Release email to blaze-dev@continuum.io.

1. Update this release procedure document to reflect
   what needed to be done for the release.
