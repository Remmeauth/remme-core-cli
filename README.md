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

### Block

Get block by its identifier — ``remme block get-single``:

| Arguments | Type   |  Required | Description                                         |
| :-------: | :----: | :-------: | --------------------------------------------------- |
| id        | String |  Yes      | Identifier of the block to fetch by.                |
| node-url  | String |  No       | Apply the command to the specified node by its URL. |

```bash
$ remme block get-single \
      --id=4a7897650db9863aca34874778e6c5802f86c3df0e22b39cfea730bc83654357037a422f8ef51ac85a9bc61d2484bd0f37be10cfc861588c41dc6f1bbfd92cde \
      --node-url=node-6-testnet.remme.io
{
    "result": {
        "batches": [
            {
                "header": {
                    "signer_public_key": "02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135",
                    "transaction_ids": [
                        "ce8dd0946326072eb4c70818d7d0df32ebd80b3a24525306ff92e8caa8c886ee571d8ba9f01c73c2c4aaab7960c0ef88865ace6dd9274dd378649f5b9da7c820"
                    ]
                },
                "header_signature": "b684d527666cce92ea57d8e14d467ee3cec5515759e1d0a78df65dbcd2a5ff993f95c8efac7c35a6380cbce81941119e98b72956278e663b9fa04e396bb7849f",
                "trace": false,
                "transactions": [
                    {
                        "header": {
                            "batcher_public_key": "02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135",
                            "dependencies": [],
                            "family_name": "block_info",
                            "family_version": "1.0",
                            "inputs": [
                                "00b10c0100000000000000000000000000000000000000000000000000000000000000",
                                "00b10c00"
                            ],
                            "nonce": "",
                            "outputs": [
                                "00b10c0100000000000000000000000000000000000000000000000000000000000000",
                                "00b10c00"
                            ],
                            "payload_sha512": "ef5953af5e24047f92cea476c6706da72b6207ac89077cb314d6d518a1293433955c0a5012c52c4acb34e2220ac8fcc33f83b33ab847631f0471f10dcdf0a54f",
                            "signer_public_key": "02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135"
                        },
                        "header_signature": "ce8dd0946326072eb4c70818d7d0df32ebd80b3a24525306ff92e8caa8c886ee571d8ba9f01c73c2c4aaab7960c0ef88865ace6dd9274dd378649f5b9da7c820",
                        "payload": "CtICCAESgAExNTJmM2JlOTFkODIzODUzOGE4MzA3N2VjOGNkNWQxZDkzNzc2N2MwOTMwZWVhNjFiNTkxNTFiMGRmYTdjNWExNzlhNjZmMTc2Y2UyM2MxNGE2N2Q4NDUxY2VjMjg1MmM4ZmY2MGZlOWU4OTYzYzNlZDExNWJkNjA3ODg5OGRhMBpCMDJkMWZiZGE1MGRiY2QwZDNjMjg2YTZhOWZhNzFhYTdjZTJkOTcxNTliOTBkZGQ0NjNlMDgxNjQyMmQ2MjFlMTM1IoABNGFlNmYzOWY0ZDZlNWJiNDhmYzA0Y2Y0MGJhNzEwMTNmYzA0NGZlNTdjOWE3Njg3ZjRlMTNkZjhjZDQ4ODQ1OTA4YTAxNjAzOTRlN2RjNjRjNDc5YTg0YzVkYmYwZmUzYzVlZTZkNmIxMDhlNzZjODYyNzQ4NzkxMWZjNjgxYWUokIr35QU="
                    }
                ]
            },
            ...
        ],
        "header": {
            "batch_ids": [
                "b684d527666cce92ea57d8e14d467ee3cec5515759e1d0a78df65dbcd2a5ff993f95c8efac7c35a6380cbce81941119e98b72956278e663b9fa04e396bb7849f",
                "cd11713211c6eb2fe4adc0e44925c1f82e9300e0b8827bd3c73d8be10e61cd2b1e8da810078845ca1665b4adf7f691ad731ab4cea0fc994c55a8863b30220c6e"
            ],
            "block_num": "2",
            "consensus": "RGV2bW9kZVrz+4RUt+Xyzhofvok/lkMcK3ZtAh/zcO/6gbPJPLPw",
            "previous_block_id": "4ae6f39f4d6e5bb48fc04cf40ba71013fc044fe57c9a7687f4e13df8cd48845908a0160394e7dc64c479a84c5dbf0fe3c5ee6d6b108e76c8627487911fc681ae",
            "signer_public_key": "02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135",
            "state_root_hash": "54eeacdf8fe3262862782110d4396b60f4b8c3863ff1b1b208fa996b6bb24a0f"
        },
        "header_signature": "4a7897650db9863aca34874778e6c5802f86c3df0e22b39cfea730bc83654357037a422f8ef51ac85a9bc61d2484bd0f37be10cfc861588c41dc6f1bbfd92cde"
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
