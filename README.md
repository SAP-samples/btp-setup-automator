# Setup Automator for SAP Business Technology Platform

[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/btp-setup-automator)](https://api.reuse.software/info/github.com/SAP-samples/btp-setup-automator) [![Release Docker Image](https://github.com/SAP-samples/btp-setup-automator/actions/workflows/docker-release-build-and-push.yml/badge.svg)](https://github.com/SAP-samples/btp-setup-automator/actions/workflows/docker-release-build-and-push.yml)[![Dev Docker Image](https://github.com/SAP-samples/btp-setup-automator/actions/workflows/docker-dev-build-and-push.yml/badge.svg)](https://github.com/SAP-samples/btp-setup-automator/actions/workflows/docker-dev-build-and-push.yml)

## ⚠ ARCHIVED - NO MAINTENANCE ⚠

📢 **Please be aware that with tool is no longer maintained and the repository is archived**

As an alternative for the btp-setup-automator we recommend to use the [Terraform Provider for SAP BTP](https://github.com/SAP/terraform-provider-btp) as tool for the setup of infrastructure on the SAP BTP available in the [Hashicorp Terraform registry](https://registry.terraform.io/providers/SAP/btp/latest).


### Description

This repository provides the user with a script to **automate the setup** of an [SAP Business Technology Platform (SAP BTP) account](https://account.hana.ondemand.com/) and to **learn** how this is done with the various command line interfaces and tools that run inside a [Docker](https://www.docker.com/) container. It uses  JSON configuration files to automate this setup of SAP BTP accounts or do other administrative tasks.

This includes:

- Setup of your SAP BTP account
- Entitlement of services
- Subscriptions to applications and creation of service instances with service keys
- Addition of administrator users to global account and sub accounts
- Setup of roles and role collections, assignment of roles collections to users
- Deployment of complete applications
- Unrolling created setup

### Quick Overview

Get a quick overview & demo of the btp-setup-automator through this video:
[![Ask-the-expert video recording](https://img.youtube.com/vi/3pLNXsn-cLM/0.jpg)](https://www.youtube.com/watch?v=3pLNXsn-cLM)

### Documentation

Started as a small helper for basic SAP BTP setups the tool has grown since its start. This documentation should support you in getting started quickly and then dive into the depths of the btp-setup-automator. The documentation has the following outline:

- [Overview](./docs/OVERVIEW.md)
- [Basic setup](./docs/BASIC_SETUP.md) incl. the prerequisites
- [Detailed walk-through](./docs/README.md)
- [Detailed configuration](./docs/SAMPLECONFIG.md)
- [Overview of btpsa parameters](./docs/PARAMETERS_OVERVIEW.md)
- [FAQ](./docs/FAQ.md)

### Code of conduct

Checkout the [CODE_OF_CONDUCT.md file](CODE_OF_CONDUCT.md) for more details on the code of conduct for this open source project.

### License

Copyright (c) 2023 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
