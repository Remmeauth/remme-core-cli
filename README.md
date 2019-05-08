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
    * [Atomic Swap](#atomic-swap)
    * [Node](#node)
    * [Public key](#public-key)
    * [State](#state)
    * [Transaction](#transaction)
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

You can use the following list of the addresses of the nodes to execute commands to:

- `node-genesis-testnet.remme.io`,
- `node-6-testnet.remme.io`,
- `node-1-testnet.remme.io`.

### Configuration file

*Disclaimer!* Configuration file is supported only on Unix operating systems and isn't supported on Windows.

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

Get information about atomic swap by its identifier — ``remme atomic-swap get-info``:

| Arguments | Type   | Required | Description                                       |
| :-------: | :----: | :------: | ------------------------------------------------- |
| id        | String | Yes      | Swap identifier to get information about swap by. |
| node-url  | String | No       | Node URL to apply a command to.                   |

```bash
$ remme atomic-swap get-info \
      --id=033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808 \
      --node-url=node-genesis-testnet.remme.io
{
    "result": {
        "information": {
            "amount": "10.0000",
            "created_at": 1556803765,
            "email_address_encrypted_optional": "",
            "is_initiator": false,
            "receiver_address": "112007484def48e1c6b77cf784aeabcac51222e48ae14f3821697f4040247ba01558b1",
            "secret_key": "",
            "secret_lock": "0728356568862f9da0825aa45ae9d3642d64a6a732ad70b8857b2823dbf2a0b8",
            "sender_address": "1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf",
            "sender_address_non_local": "0xe6ca0e7c974f06471759e9a05d18b538c5ced11e",
            "state": "OPENED",
            "swap_id": "033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808"
        }
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

### State

Get a state by its address — ``remme state get``:

| Arguments | Type   | Required | Description                        |
| :-------: | :----: | :------: | ---------------------------------- |
| address   | String | Yes      | Account address to get a state by. |
| node-url  | String | No       | Node URL to apply a command to.    |

```bash
$ remme state get \
      --address=000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c12840f169a04216b7 \
      --node-url=node-6-testnet.remme.io
{
    "result": {
        "state": {
            "data": "CmwKJnNhd3Rvb3RoLnNldHRpbmdzLnZvdGUuYXV0aG9yaXplZF9rZXlzEkIwMmE2NTc5NmYyNDkwOTFjMzA4NzYxNGI0ZDljMjkyYjAwYjhlYmE1ODBkMDQ1YWMyZmQ3ODEyMjRiODdiNmYxM2U=",
            "head": "95d78133eb98628d5ff17c7d1972b9ab03e50fceeb8e199d98cb52078550f5473bb001e57c116238697bdc1958eaf6d5f096f7b66974e1ea46b9c9da694be9d9"
        }
    }
}
```

### Transaction

Get a list of transactions — ``remme transaction get-list``:

| Arguments   | Type   |  Required | Description                                            |
| :---------: | :----: | :-------: | -----------------------------------------------------  |
| ids         | String |  No       | Identifiers to get a list of transactions by.          |
| start       | String |  No       | Transaction identifier to get a list transaction starting from.|
| limit       | Integer|  No       | Maximum amount of transactions to return.              |
| head        | String |  No       | Block identifier to get a list of transactions from.   |
| reverse     | Bool   |  No       | Parameter to reverse result.                           |
| node-url    | String |  No       | Node URL to apply a command to.                        |
| family-name | String |  No       | List of transactions by its family name.               |

```bash
$ remme transaction get-list \
    --ids='568a1094e574747c757c1f5028d9b929105984e509c4f2f3cb76e5f46f03ca4c3681ca0eeca86a4bd4bb5a3eaaa52fd73b08ebc5d5d85fbb1957b064f8b71972, 
    d9b891d3efdd51cd47156ad2083bf5cabd5b35bb2ebe66813996d1a0f783e58721bbc50917ff284a40696f24058ef1e22e48600abf37d500ace78eadf7f4ecff' \
    --start=568a1094e574747c757c1f5028d9b929105984e509c4f2f3cb76e5f46f03ca4c3681ca0eeca86a4bd4bb5a3eaaa52fd73b08ebc5d5d85fbb1957b064f8b71972 \
    --limit=2 \
    --head=39566f24561727f5ab2d19eb23612f1a38ff5f0cf9491caa0275261706a7cf8b080d38da0a38fa5b1cbef0cced889fdf6da679cc616a9711380f76b33e53efdf \
    --reverse \
    --family-name=account \
    --node-url=node-6-testnet.remme.io
{
    "result": {
        "data": [
            {
                "header": {
                    "batcher_public_key": "03d4613540ce29cd1f5f28ea9169a5cb5853bd53dede635903af9383bc9ffaf079",
                    "dependencies": [],
                    "family_name": "account",
                    "family_version": "0.1",
                    "inputs": [
                        "112007db16c75019f59423da4de3cd5c79609989d7dc1697c9975307ea846e1d4af91f",
                        "1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf"
                    ],
                    "nonce": "99ccdbcfeb008e2c8407870b7033117e316b4b12df4173f3e2ffd510676e524a77ac64a0b65e6c7889a797fbd4e4462830548f455497e2362dde1bbf35d5372f",
                    "outputs": [
                        "112007db16c75019f59423da4de3cd5c79609989d7dc1697c9975307ea846e1d4af91f",
                        "1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf"
                    ],
                    "payload_sha512": "1f0313cb9cd67559c1d33d61104882b3ebca80dfcd091d5ae3b0ee99bd27723af591551dfeea43be05e2b24a2f9a54adc6c357b60fc5c5720b161c5ff9d10ae1",
                    "signer_public_key": "03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad"
                },
                "header_signature": "d9b891d3efdd51cd47156ad2083bf5cabd5b35bb2ebe66813996d1a0f783e58721bbc50917ff284a40696f24058ef1e22e48600abf37d500ace78eadf7f4ecff",
                "payload": "CAASTQgAEkYxMTIwMDdkYjE2Yzc1MDE5ZjU5NDIzZGE0ZGUzY2Q1Yzc5NjA5OTg5ZDdkYzE2OTdjOTk3NTMwN2VhODQ2ZTFkNGFmOTFmGOgH"
            }
        ],
        "head": "39566f24561727f5ab2d19eb23612f1a38ff5f0cf9491caa0275261706a7cf8b080d38da0a38fa5b1cbef0cced889fdf6da679cc616a9711380f76b33e53efdf",
        "paging": {
            "limit": 2,
            "next": "",
            "start": "568a1094e574747c757c1f5028d9b929105984e509c4f2f3cb76e5f46f03ca4c3681ca0eeca86a4bd4bb5a3eaaa52fd73b08ebc5d5d85fbb1957b064f8b71972"
        }
    }
}
```

Get a transaction by identifier — ``remme transaction get``:

| Arguments   | Type   |  Required | Description                       |
| :---------: | :----: | :-------: | --------------------------------  |
| id          | String |  Yes      | Identifier to get transaction by. |
| node-url    | String |  No       | Node URL to apply a command to.   |

```bash
$ remme transaction get \
    --id=64d032fbaae9bc59f9e5484ec6f52cbceef567923456039a26a1cfb8bc9ee2431ac2b5de43efce28ef11820a3734dab9fa56db57a1b2fbdc2323036cceeab6ab \
    --node-url=node-6-testnet.remme.io
{
    "result": {
        "data": {
            "header": {
                "batcher_public_key": "03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad",
                "dependencies": [],
                "family_name": "consensus_account",
                "family_version": "0.1",
                "inputs": [
                    "116829",
                    "112007",
                    "0000007ca83d6bbb759da9cde0fb0dec1400c54773f137ea7cfe91e3b0c44298fc1c14",
                    "0000007ca83d6bbb759da9cde0fb0dec1400c5034223fb6c3e825ee3b0c44298fc1c14",
                    "0000007ca83d6bbb759da9cde0fb0dec1400c5e64de9aa6a37ac92e3b0c44298fc1c14",
                    "00b10c0100000000000000000000000000000000000000000000000000000000000000",
                    "00b10c00",
                    "fd0e4f0000000000000000000000000000000000000000000000000000000000000000"
                ],
                "nonce": "b8baa6c54ab9463590627c18fb9c10ed",
                "outputs": [
                    "116829",
                    "112007",
                    "fd0e4f0000000000000000000000000000000000000000000000000000000000000000"
                ],
                "payload_sha512": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
                "signer_public_key": "03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad"
            },
            "header_signature": "64d032fbaae9bc59f9e5484ec6f52cbceef567923456039a26a1cfb8bc9ee2431ac2b5de43efce28ef11820a3734dab9fa56db57a1b2fbdc2323036cceeab6ab",
            "payload": ""
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
