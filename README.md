# Setup Automator for SAP Business Technology Platform

[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/btp-setup-automator)](https://api.reuse.software/info/github.com/SAP-samples/btp-setup-automator) [![Release Docker Image](https://github.com/SAP-samples/btp-setup-automator/actions/workflows/docker-release-build-and-push.yml/badge.svg)](https://github.com/SAP-samples/btp-setup-automator/actions/workflows/docker-release-build-and-push.yml)[![Dev Docker Image](https://github.com/SAP-samples/btp-setup-automator/actions/workflows/docker-dev-build-and-push.yml/badge.svg)](https://github.com/SAP-samples/btp-setup-automator/actions/workflows/docker-dev-build-and-push.yml)

## Description

This repository provides the user with a script to **automate the setup** of an [SAP Business Technology Platform (SAP BTP) account](https://account.hana.ondemand.com/) and to **learn** how this is done with the various command line interfaces and tools that to run inside a [Docker](https://www.docker.com/) container.

This includes:

- Setup of your SAP BTP account
- Entitlement of services
- Subscriptions to applications and creation of service instances with service keys
- Addition of administrator users to global account and sub accounts
- Setup of roles and role collections, assignment of roles collections to users
- Deployment of complete applications
- Unrolling created setup

## Quick Overview

Get a quick overview & demo of the btp-setup-automator through this video:
[![Ask-the-expert video recording](https://img.youtube.com/vi/3pLNXsn-cLM/0.jpg)](https://www.youtube.com/watch?v=3pLNXsn-cLM)

## Documentation

Started a small helper for basic SAP BTP setups the tool has grown since its start. This documentation should support you in getting started quickly and then dive into the depths of the btp-setup-automator. The documentation has the following outline:

- [Basic setup](./docs/BASIC_SETUP.md) incl. the prerequisites
- [Basic configuration](./docs/OVERVIEW.md)
- [Detailed walk-though](./docs/README.md)
- [Detailed configuration](./docs/SAMPLECONFIG.md)
- [Overview of btpsa parameters](./docs/PARAMETERS_OVERVIEW)
- [FAQ](./docs/FAQ.md)

## Known Issues

Checkout [the issues section in this repo](https://github.com/SAP-samples/btp-setup-automator/issues) for known and current issues.

## How to get Support?

❓ - If you have *question* you may peruse the [Frequently Asked Questions](docs/FAQ.md) document. If you did not find your questions answered there you can [ask a question in SAP Community](https://answers.sap.com/questions/ask.html).

🐛 - If you find a bug, feel free to [create an bug report](https://github.com/SAP-samples/btp-setup-automator/issues/new?assignees=&labels=bug&template=bug-report.yml&title=%5BBUG%5D+%3Ctitle%3E).

🚀 - If you have an idea for improvement or a feature request, please open [feature-request](https://github.com/SAP-samples/btp-setup-automator/issues/new?assignees=&labels=enhancement&template=feature-request.yml&title=%5BFEATURE+REQUEST%5D+%3Ctitle%3E).

## Contributions

Checkout the [CONTRIBUTING.md file](CONTRIBUTING.md) for more details on how to contribute to this open source project.

> 📝 Tip - If you provide a pull request make sure that the basis of your work as well as the target for your pull request is the `dev` branch of this repository.

## Code of conduct

Checkout the [CODE_OF_CONDUCT.md file](CODE_OF_CONDUCT.md) for more details on the code of conduct for this open source project.

## License

Copyright (c) 2022 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
