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
    * [Node](#node)
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

### Atomic Swap

Get public key of atomic swap — ``remme atomic-swap get-public-key``:

| Arguments | Type   | Required | Description                     |
| :-------: | :----: | :------: | ------------------------------- |
| node-url  | String | No       | Node URL to apply a command to. |

```bash
$ remme atomic-swap get-public-key --node-url=node-6-testnet.remme.io
{
    "result": {
        "public_key": "03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad"
    }
}
```

### Node

Get node configurations — ``remme node get-configs``:

| Arguments | Type   |  Required | Description                     |
| :-------: | :----: | :-------: | ------------------------------- |
| node-url  | String |  No       | Node URL to apply a command to. |

```bash
$ remme node get-configs --node-url=node-genesis-testnet.remme.io
{
    "result": {
        "configurations": {
            "node_address": "1168296ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf",
            "node_public_key": "03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad"
        }
    }
}
```

Get the node's peers — ``remme node get-peers``:

| Arguments | Type   |  Required | Description                     |
| :-------: | :----: | :-------: | ------------------------------- |
| node-url  | String |  No       | Node URL to apply a command to. |

```bash
$ remme node get-peers --node-url=node-genesis-testnet.remme.io
{
    "result": {
        "peers": [
            "tcp://node-22-testnet.remme.io:8800",
            "tcp://node-9-testnet.remme.io:8800",
            "tcp://node-29-testnet.remme.io:8800"
        ]
    }
}
```

Get node information — ``remme node get-info``:

| Arguments | Type   | Required | Description                     |
| :-------: | :----: | :------: | ------------------------------- |
| node-url  | String | No       | Node URL to apply a command to. |

```bash
$ remme node get-info --node-url=node-27-testnet.remme.io
{
    "result": {
        "information": {
            "is_synced": true,
            "peer_count": 3
        }
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
        "addresses": [
            "a23be10b3aad1b4a98f338c71d6dcdb2aa2f296c7e31fb400615e335dc10dd1d4f62bf",
            "a23be14b362514d624c1985277005327f6fc40413fb090eee6fccb673a32c9809060ff"
        ]
    }
}
```

Get information about public key by its address — ``remme public-key get-info``:

| Arguments | Type   | Required | Description                                                |
| :-------: | :----: | :------: | ---------------------------------------------------------- |
| address   | String | Yes      | Public key address to get information about public key by. |
| node-url  | String | No       | Node URL to apply a command to.                            |

```bash
$ remme public-key get-info \
      --address=a23be17addad8eeb5177a395ea47eb54b4a646f8c570f4a2ecc0b1d2f6241c6845181b \
      --node-url=node-genesis-testnet.remme.io
{
    "result": {
        "information": {
            "address": "a23be10d215132aee9377cfe26b6d301d32da070a799c227fb4701103e5626d48cd6ba",
            "entity_hash": "1edd6d5b1c722a83e03b17180b888d89ec4c079a0044f074b7c8bb2720cad8ba4e97a80c7edbd24c1824f5312dfd8a0877453394a63410b52c1f16e1d60ef754",
            "entity_hash_signature": "1322ca51fb6d33e44d2b6c028eb668b5712a5277bbdea089112203e8e950d1c7d02d446291865a2f5fca4c6767fb84583e53205df850f1fc05ea6f22c736635f425b0159881f7f998da52378bf08353d87d2a2c226a7ababea9a245e69be06d54c573a42c3be907ca49589a67b5e9cc4d8ed12cea8546b2df531fd9620f4dc71869d8fa0bfcbef239d9a6e2e3bf12bcac4fd562b22ff408d7b077b75d8e59af0348264a7c9e7e61b4c5f844636a0fbbcfae61955efdf10323a992ea2a1734eb0ee7952519b00e696a02e7460771b0e0887e011b709e88abfda896b68150c08dcf6b4bf7c70f996f6031c13311056ab935ce1fdf63d3f19b5a3ca6ae604c4f12b",
            "is_revoked": false,
            "is_valid": true,
            "owner_public_key": "03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad",
            "public_key": "30820122300d06092a864886f70d01010105000382010f003082010a02820101008b29cc5ec32dab21b48b63faf2fd00f88879b9d4286c3cde6218d19263ea8226fce499039968c5f9736149e298bbc56680b516f2d83507d88fb95771445ca3c59bcdbb31bb5993a4e5dfcd2c4bc86328ec76e95e2f4582f9cac8223a2f16a2b14c4358b6fb105e37baf9daa9bd5b708ab204d8015a1ce782e28024eae1801151616c90a3b1aa1916d5b8dd021b3aa4cec77450660841f8619a7234c6199d01ccd43b1d6ff7fa5f50bf80bc06b682b126bdca0753a6830b7a95afca79442ec64fd09ddcc34627dcbdad0c5e66317db98d0e1c24c3f992b83f4b0f97e2b0300a2cb51e33eccf060f26b4e19a88f15216f8c17be5f5e023a1f260f7c93a2a4523ed0203010001",
            "type": "rsa",
            "valid_from": 1556118334,
            "valid_to": 1587222334
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
