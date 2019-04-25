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
    * [Nodes](#nodes)
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

Install the package from the [PyPi](https://pypi.org/project/remme-core-cli) through [pip](https://github.com/pypa/pip):

```bash
$ pip3 install remme-core-cli
```

## Usage

### Nodes

You can use the following list of the addresses of the nodes to execute commands to:

- `node-genesis-testnet.remme.io`,
- `node-6-testnet.remme.io`,
- `node-1-testnet.remme.io`.

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
$ curl -L https://git.io/fj3Mi > ~/.remme-core-cli.yml
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

| Arguments | Type   |  Required | Description                          |
| :-------: | :----: | :-------: | ------------------------------------ |
| address   | String |  Yes      | Account address to get a balance by. |
| node-url  | String |  No       | Node URL to apply a command to.      |

```bash
$ remme account get-balance \
      --address=1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf \
      --node-url=node-genesis-testnet.remme.io
{
    "result": {
        "balance": 368440.0
    }
}
```

Transfer tokens to address — ``remme account transfer-tokens``:

| Arguments   | Type    |  Required | Description                                    |
| :---------: | :-----: | :-------: | ---------------------------------------------- |
| private-key | String  |  Yes      | Account's private key to transfer tokens from. |
| address-to  | String  |  Yes      | Account address to transfer tokens to.         |
| amount      | Integer |  Yes      | Amount to transfer.                            |
| node-url    | String  |  No       | Node URL to apply a command to.                |

```bash
$ remme account transfer-tokens \
      --private-key=1067b42e24b4c533706f7c6e62278773c8ec7bf9e78bf570e9feb58ba8274acc \
      --address-to=112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202 \
      --amount=1000 \
      --node-url=node-genesis-testnet.remme.io
{
    "result": {
        "batch_identifier": "aac64d7b10be4b93b8c345b5eca1dc870c6b3905485e48a0ca5f58928a88a42b7a404abb4f1027e973314cca95379b1ef375358ad1661d0964c1ded4c212810f"
    }
}
```

### Public key

Get a list of the addresses of the public keys by account address — ``remme public-key get-list``:

| Arguments | Type   | Required | Description                                                           |
| :-------: | :----: | :------: | --------------------------------------------------------------------- |
| address   | String | Yes      | Account address to get a list of the addresses of the public keys by. |
| node-url  | String | No       | Node URL to apply a command to.                                       |

```bash
$ remme public-key get-list \
      --address=1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf \
      --node-url=node-genesis-testnet.remme.io
{
    "result": {
        "public_key_addresses": [
            "a23be10b3aad1b4a98f338c71d6dcdb2aa2f296c7e31fb400615e335dc10dd1d4f62bf",
            "a23be14b362514d624c1985277005327f6fc40413fb090eee6fccb673a32c9809060ff"
        ]
    }
}
```

Get information about public key address by public key address — ``remme public-key get-info``:

| Arguments | Type   | Required | Description                                                |
| :-------: | :----: | :------: | ---------------------------------------------------------- |
| address   | String | Yes     | Public key address to get information about public key by. |
| node-url  | String | No      | Node URL to apply a command to.                            |

```bash
$ remme public-key get-info \
      --address=a23be149969381eadcacaf9e4e8914296f1107119cfe1b7d79c0e6027a02822dfd19b7 \
      --node-url=node-genesis-testnet.remme.io
{
    "result": {
        "public_key_info": {
            "address": "a23be1003e0b0a65edd19b057c5f9b20c7e0571ff07634b5936209048b00aefb711ba0",
            "entity_hash": "3409ab9912c4bbb900648f327f62a5d8a45ff5dc52f437aad44b75b5c4f7a95bcac6b7163ffbaa22bbf87dcb77805940e80fab785d95685e68b4f9e8f559a7ea",
            "entity_hash_signature": "71fd79a7d095a917fa37d720001c4ca81bb279919130685022136e579a2b11b610c734b024c6f0d5751ad5c9701aa902d7f0adf536d14f45cb2feb0ba20c347d13c0ff8c2de7f16d59c2952b45ed4378238e3fd1d2b6948e9ff61edf6049cc9c1464a4526f24f635140953acb2f29f76d5bdeb1fc15d99279e3a519a79a56fdf8a8cd522a757eb4e64e6f3ff18c13d7c179a5a0967b823e65884a125aa298dda8801db1f38fdb8aeff4d60a794d00d3f171649d2c3c200d101d3a59819a536a144b95457c41370abcfb05f6fd57d2e4c69bd9f4b14adcd1796e12a3036147d615e6e6d2e275e7e9eafd228ddaf2863bf5ea9a0b4e7411f388d35cbc993b5a446",
            "is_revoked": false,
            "is_valid": true,
            "owner_public_key": "02c172f9a27512c11e2d49fd41adbcb2151403bd1582e8cd94a5153779c2107092",
            "public_key": "30820122300d06092a864886f70d01010105000382010f003082010a0282010100c1bc4b0de0473683444c463a95a17c143962a20b5fb531bca52eef7a9b617e6232727048bf1209b0eb96aa37f85adb08dc1d3d1289bfb8b01721a2d46081db29a8bab3c25097a9a5aafbc465304f18463847008a8a6b5f35d440ef49638f88efcd4afda7cd9ea551561174d37d9947a08f8efa9314d88e78b3db071fc1d16a216fbea0cf29b559d304b52f505a60d9421119fc10bdbec899f1c43d6c2e05a285e50bc4f64bed8804012ef164f08f86f67182b3d5204654f1dc95a8db99e43a0d55a61b34e41a602f1638c623b84988724fff172aff9f658993939b2f4f3a179560ef261c6dfab40f005b96e042a61c23c2c282f03775b35bc359d5a6443db1cb0203010001",
            "type": "rsa",
            "valid_from": 1556123507,
            "valid_to": 1587659507
        }
    }
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
$ docker run -d --network host -v $PWD:/remme-core-cli --name remme-core-cli remme-core-cli
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

When you make changes, ensure your code:

* pass [the checkers](https://github.com/Remmeauth/remme-core-cli/blob/develop/.travis.yml#L16),
* is covered by tests using [pytest](https://docs.pytest.org/en/latest),
* follow team [code style](https://github.com/dmytrostriletskyi/nimble-python-code-style-guide).

If you are new for the contribution, please read:

* Read about pull requests — https://help.github.com/en/articles/about-pull-requests
* Read how to provide pull request — https://help.github.com/en/articles/creating-a-pull-request-from-a-fork
* Also the useful article about how to contribute — https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/

### Request pull request's review

If you want to your pull request to be review, ensure you:
1. [Branch isn't out-of-date with the base branch](https://habrastorage.org/webt/ux/gi/wm/uxgiwmnft08fubvjfd6d-8pw2wq.png).
2. [Have written the description of the pull request and have added at least 2 reviewers](https://camo.githubusercontent.com/55c309334a8b61a4848a6ef25f9b0fb3751ae5e9/68747470733a2f2f686162726173746f726167652e6f72672f776562742f74312f70792f63752f7431707963753162786a736c796f6a6c707935306d7862357969652e706e67).
3. [Continuous integration has been passed](https://habrastorage.org/webt/oz/fl/-n/ozfl-nl-jynrh7ofz8yuz9_gapy.png).
