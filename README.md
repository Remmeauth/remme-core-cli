# remme-core-cli

[![Release](https://img.shields.io/github/release/Remmeauth/remme-core-cli.svg)](https://github.com/Remmeauth/remme-core-cli/releases)
[![PyPI version shields.io](https://img.shields.io/pypi/v/remme-core-cli.svg)](https://pypi.python.org/pypi/remme-core-cli/)
[![Build Status](https://travis-ci.com/Remmeauth/remme-core-cli.svg?branch=develop)](https://travis-ci.com/Remmeauth/remme-core-cli)
[![codecov](https://codecov.io/gh/Remmeauth/remme-core-cli/branch/develop/graph/badge.svg)](https://codecov.io/gh/Remmeauth/remme-core-cli)

[![Downloads](https://pepy.tech/badge/remme-core-cli)](https://pepy.tech/project/remme-core-cli)
[![PyPI license](https://img.shields.io/pypi/l/remme-core-cli.svg)](https://pypi.python.org/pypi/remme-core-cli/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/remme-core-cli.svg)](https://pypi.python.org/pypi/remme-core-cli/)

  * [Getting started](#getting-started)
    * [Requirements](#getting-started-requirements)
    * [Installation](#installation)
  * [Usage](#usage)
    * [Configuration file](#configuration-file)
    * [Service](#service)
    * [Account](#account)
    * [Public key](#public-key)
  * [Development](#development)
    * [Requirements](#development-requirements)
    * [Docker](#docker)
  * [Production](#production)
  * [Contributing](#contributing)
    * [Request pull request's review](#request-pull-requests-review)
  
## Getting started

<h3 id="getting-started-requirements">Requirements</h4>

- Python 3.6 or 3.7 — install one of them with the [following reference](https://www.python.org/downloads).

### Installation

Install the package from the [PypI](https://pypi.org/project/remme-core-cli) through [pip](https://github.com/pypa/pip):

```bash
$ pip3 install remme-core-cli
```

## Usage

### Configuration file

Using the command line interface, you will have an option to declare the `node URL` to send commands to as illustrated below:

```bash
$ remme account get-balance \
      --address=1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf \
      --node-url=node-genesis-testnet.remme.io
```

You shouldn't declare `node URL` every time when you execute a command, use configuration file instead. Configuration file 
is required to be named `.remme-core-cli.yml` and located in the home directory (`~/`).

The configuration file have an optional section to declare `node URL` to send commands to:

```bash
node-url: node-genesis-testnet.remme.io
```

Try it out by downloading the example of the configuration file to the home directory.

```bash
$ curl -L https://git.io/fjYZS > ~/.remme-core-cli.yml
```

### Service

Get the version of the package — ``remme --version``:

```bash
$ remme --version
remme, version 0.1.0
```

Get all possible package's commands — ``remme --help``:

```bash
$ remme --help
Usage: remme [OPTIONS] COMMAND [ARGS]...

  Command line interface for PyPi version checking.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

...
```

### Account

Get balance of the account by its address — ``remme account get-balance``:

| Arguments | Type   |  Required | Description                                         |
| :-------: | :----: | :-------: | --------------------------------------------------- |
| address   | String |  Yes      | Get balance of the account by its address.          |
| node-url  | String |  No       | Apply the command to the specified node by its URL. |

```bash
$ remme account get-balance \
      --address=1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf \
      --node-url=node-genesis-testnet.remme.io
368440.0
```

### Public key

Get public key by account address — ``remme public-key get-single``:

| Arguments | Type   | Required | Description                                             |
| :-------: | :----: | :------: | ------------------------------------------------------- |
| address   | String |  Yes     | Get information about public key by public key address. |
| node-url  | String |  No      | Apply the command to the specified node by its URL.     |

```bash
$ remme public-key get-single \
      --address=a23be14785e7b073b50e24f72e086675289795b969a895a7f02202404086946e8ddc5b \
      --node-url=node-genesis-testnet.remme.io
{
    "address": "a23be1ae97d605bcbe61c312d9a443c010dbe7e6a0761e24b10d5368829ab0a7d36acc",
    "entity_hash": "13517cee1694346b584c08f5d84cc584b407043ef6a682942b1e18f0466cf1e2dede1756499ac8a2ee495cba258c609ea6147b4daa15225ba60ec5ffca419bd6",
    "entity_hash_signature": "6e081607aac18e63a44265e0054fb3e60d3791ac2292925c56d54df216396a3af42e96557a0da09b236cdb5970ca5272473dcc9d71f16978e09a26bfb5e96562d8002473cfdf29b4c04dcc97cd4fa9d768ea13bd04b7479fe2f5965cfb0f944848511c9f597eacd4a23a1fd66aabfa95f45130fae1ae2507e8ed8d8ee308c77a042c86bbc476e2d3ed46c4b3c2a86c87470bb94c6e266cfd44bc513d04e5523c7faf08887df4e37f2e31bda1bf403cb7bb3145602cd56dea7965e6e417d86620704a68013e95bbda6a81e3dfb86aa489fa060e78bf9edfc4329ffc1f8484ecc610fccb5302499e1f18d0e2584db9c23cdb4b0485ccda7cab17896b8fec28c851",
    "is_revoked": false,
    "is_valid": true,
    "owner_public_key": "03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad",
    "public_key": "30820122300d06092a864886f70d01010105000382010f003082010a028201010098ed61c659566b05d4017a0b59b7ce15f6be8432a470713cf3f0ac40b9ded6b65c227704c9bbde4f41a81a380c1ebadb771d1295418805eb16d514c0eb8a8747d08bb1cb5269d5ecb1152d64a8d8bb14836589f6babce22c2deac7dc6b80fcf285c74b67c5ccaf7464df47d10dccecf02d8c4ed9924a8f4ee0df8661d9378fdb0a42355eda8128e88f7871ac5ea7c2605afa1b2b400e1a13b9f9fcf037aa7defcfe2abdcc4b9635d8601d1755660c0838fb2e10c35a88e7b9c1fc89db58cb6fa701a8a80f3dbbf587c1af43e7029e4bc79a26012cb9534d66a818c68acb9707a1a1a7c02b781df4928540053693696fb058d1935fed35cf307c362e7f601710b0203010001",
    "type": "rsa",
    "valid_from": 1554753277,
    "valid_to": 1585857277
}
```

## Development

<h3 id="development-requirements">Requirements</h4>

- Docker — https://www.docker.com. Install it with the [following reference](https://docs.docker.com/install).

### Docker

Clone the project and move to project folder:

```bash
$ git clone https://github.com/Remmeauth/remme-core-cli && cd remme-core-cli
```

If you already worked with the project, you can clean it's container and images with the following command:

```bash
$ docker rm remme-core-cli -f || true && docker rmi remme-core-cli -f || true
```

Run the ``Docker container`` with the project source code in the background mode:

```bash
$ docker build -t remme-core-cli . -f Dockerfile.development
$ docker run -d -v $PWD:/remme-core-cli --name remme-core-cli remme-core-cli
```

Enter the container bash:

```bash
$ docker exec -it remme-core-cli bash
```

And now being in the container, you can develop the project. For instance, run tests and linters:

```bash
$ pytest -vv tests/
$ flake8 cli && flake8 tests/
```

When you have developed new functionality, check it with the following command. This command creates the ``Python package``
from source code instead of installing it from the ``PyPi``.

```bash
$ pip3 uninstall -y remme-core-cli && rm -rf dist/ remme_core_cli.egg-info && \
      python3 setup.py sdist && pip3 install dist/*.tar.gz
```

So after this command, you are free to execute the command line interface as if you installed in through ``pip3 install``:

```bash
$ remme --version
```

With the commands above you could test your features as if user will use it on own.

```bash
$ docker rm $(docker ps -a -q) -f
$ docker rmi $(docker images -q) -f
```

## Production

To build the package and upload it to [PypI](https://pypi.org) to be accessible through [pip](https://github.com/pypa/pip),
use the following commands. [Twine](https://twine.readthedocs.io/en/latest/) requires the username and password of the
account package is going to be uploaded to.

```build
$ python3 setup.py sdist
$ twine upload dist/*
username: remme
password: ********
```

## Contributing

Clone the project and install requirements:

```bash
$ git clone https://github.com/Remmeauth/remme-core-cli && cd remme-core-cli
$ pip3 install -r requirements.txt -r requirements-dev.txt -r requirements-tests.txt
```

When you make changes, ensure your code pass [the checkers](https://github.com/Remmeauth/remme-core-cli/blob/develop/.travis.yml#L16) and is covered by tests using [pytest](https://docs.pytest.org/en/latest).

If you are new for the contribution, please read:

* Read about pull requests — https://help.github.com/en/articles/about-pull-requests
* Read how to provide pull request — https://help.github.com/en/articles/creating-a-pull-request-from-a-fork
* Also the useful article about how to contribute — https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/

### Request pull request's review

If you want to your pull request to be review, ensure you:
- `have wrote the description of the pull request`,
- `have added at least 2 reviewers`,
- `continuous integration has been passed`.

![Example of the description and reviewers](https://habrastorage.org/webt/t1/py/cu/t1pycu1bxjslyojlpy50mxb5yie.png)

![Example of the CI which passed](https://habrastorage.org/webt/oz/fl/-n/ozfl-nl-jynrh7ofz8yuz9_gapy.png)
