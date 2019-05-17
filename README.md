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
      * [Ubuntu 16.04 & 18.04](#ubuntu-1604--1804)
      * [MacOS](#macos)
    * [Installation](#installation)
  * [Usage](#usage)
    * [Configuration file](#configuration-file)
    * [Service](#service)
    * [Account](#account)
    * [Node Account](#node-account)
    * [Block](#block)
    * [Atomic Swap](#atomic-swap)
    * [Batch](#batch)
    * [Node](#node)
    * [Public key](#public-key)
    * [State](#state)
    * [Transaction](#transaction)
    * [Receipt](#receipt)
  * [Development](#development)
    * [Requirements](#development-requirements)
    * [Docker](#docker)
  * [Production](#production)
  * [Contributing](#contributing)
    * [Request pull request's review](#request-pull-requests-review)
  
## Getting started

<h3 id="getting-started-requirements">Requirements</h4>

#### Ubuntu 16.04 & 18.04

If you have `16.04` version, install system requirements with the following terminal commands:

```bash
$ apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa -y && \
          apt-get install -y build-essential automake libtool pkg-config \
          libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
```

If `18.04`, then use the following terminal commands:

```bash
$ apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa -y && \
          apt-get install -y build-essential automake libtool pkg-config libsecp256k1-dev \
          libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
```

Now, for both of versions, install `Python 3.6` (also, we support 3.7):

```bash
$ apt-get update && apt-get install -y python3.6 python3.6-dev python3-pip python3-setuptools python3.6-venv
```

And make it as default `python3` with the following command:

```bash
$ rm /usr/bin/python3 && sudo ln -s /usr/bin/python3.6 /usr/bin/python3
```

#### MacOS

Install `Python 3.7` (also, we support 3.6):

```
$ brew install python3
```

Install system requirements with the following terminal command:

```bash 
$ brew install automake pkg-config libtool libffi gmp
```

## Installation

Install the package from the [PyPi](https://pypi.org/project/remme-core-cli) through [pip](https://github.com/pypa/pip):

```bash
$ pip3 install remme-core-cli
```

## Usage

You can use the following list of the addresses of the nodes to execute commands to:

- `node-genesis-testnet.remme.io`,
- `node-6-testnet.remme.io`,
- `node-1-testnet.remme.io`.

Also, you can use the following IP-addresses (development servers):

- `159.89.104.9`,
- `165.22.75.163`.

They work based on a bit different codebase. So, if you have errors using a domain name, use IP-address instead. But, keep in mind that development servers don't consist in the public test network.

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

| Arguments | Type   | Required | Description                          |
| :-------: | :----: | :------: | ------------------------------------ |
| address   | String | Yes      | Account address to get a balance by. |
| node-url  | String | No       | Node URL to apply a command to.      |

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

| Arguments   | Type    | Required | Description                                    |
| :---------: | :-----: | :------: | ---------------------------------------------- |
| private-key | String  | Yes      | Account's private key to transfer tokens from. |
| address-to  | String  | Yes      | Account address to transfer tokens to.         |
| amount      | Integer | Yes      | Amount to transfer.                            |
| node-url    | String  | No       | Node URL to apply a command to.                |

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

### Node Account

Get information about the node account by its address — ``remme node-account get``:

| Arguments | Type   | Required | Description                                                    |
| :-------: | :----: | :------: | -------------------------------------------------------------- |
| address   | String | Yes      | Node account address to get information about node account by. |
| node-url  | String | No       | Node URL to apply a command to.                                |

```bash
$ remme node-account get \
      --address=1168290a2cbbce30382d9420fd5f8b0ec75e953e5c695365b1c22862dce713fa1e48ca \
      --node-url=node-1-testnet.remme.io
{
    "result": {
        "balance": "0.0000",
        "last_defrost_timestamp": "0",
        "min": true,
        "node_state": "OPENED",
        "reputation": {
            "frozen": "250000.4100",
            "unfrozen": "51071032.5900"
        },
        "shares": [
            {
                "block_num": "552",
                "block_timestamp": "1556178213",
                "defrost_months": 0,
                "frozen_share": "5440",
                "reward": "0"
            },
        ],
    },
}
```

### Block

Get a list of blocks — ``remme block get-list``:

| Arguments | Type    | Required | Description                                        |
| :-------: | :-----: | :------: | -------------------------------------------------- |
| ids       | String  | No       | Identifiers to get a list of blocks by.            |
| limit     | Integer | No       | Maximum amount of blocks to return.                |
| head      | Integer | No       | Block identifier to get a list of transactions to. |
| ids-only  | Bool    | No       | The flag to get a list of blocks' identifiers.     |
| reverse   | Bool    | No       | Parameter to reverse result.                       |
| node-url  | String  | No       | Node URL to apply a command to.                    |

```bash
$ remme block get-list \
      --ids='fe56a16dab009cc96e7125c647b6c71eb1063818cf8dece283b125423ecb184f7f1e61802bf66382da904698413f80831031f8a1b29150260c3fa4db537fdf4c,
      56100bf24eed12d2f72fe3c3ccf75fe2f53d87c224d9dda6fb98a1411070b06a40fcf97fccc61cb9c88442953af6ae50344ad7773f1becc6bae108443c18c551' \
      --head=fe56a16dab009cc96e7125c647b6c71eb1063818cf8dece283b125423ecb184f7f1e61802bf66382da904698413f80831031f8a1b29150260c3fa4db537fdf4c \
      --limit=2 \
      --reverse \
      --node-url=node-genesis-testnet.remme.io
{
    "result": [
        {
            "batches": [
                {
                    "header": {
                        "signer_public_key": "02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135",
                        "transaction_ids": [
                            "6593d21046519022ba32c98e934d7dfc81e8b4edf6c064dbf70feb13db4310873ec00816bce8660cafd4fa2a8c80d0147d63cf616c624babd03142c694272017"
                        ]
                    },
                    "header_signature": "fa2d1a209ad04fd2ad7fb5183976e647cc47b4c08e2e578097afc2566a0284e760eb3f2ff8f72f290765211d4da3341f23091cc7a16805025a17c04a90818a44",
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
                                "payload_sha512": "1b2cdc6ecfb575b926abea76b44e6988617e945e0f3d84b7624ee228cf35252a7cd186eabe5126c5f967ff54d0b1001e2c07716a7d9e00b5710e836400a913d5",
                                "signer_public_key": "02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135"
                            },
                            "header_signature": "6593d21046519022ba32c98e934d7dfc81e8b4edf6c064dbf70feb13db4310873ec00816bce8660cafd4fa2a8c80d0147d63cf616c624babd03142c694272017",
                            "payload": "CtMCCLwBEoABOWI4Y2NhODk3Nzk2NDJiYWEyMGMwZWUyZjEzOWVlMGNlMWNjYjEwMjY5OTVjNDY3NDYzZDEzOTI0ZDg3YTg3NjNlODMzOWI2YzIyMzNmMTZiY2I5ZDVjNjEwMzVmNzAzY2FiNjBiNzQxMGJlMjJkZjkzNWEyYWE4YmIzNGE1NTcaQjAyZDFmYmRhNTBkYmNkMGQzYzI4NmE2YTlmYTcxYWE3Y2UyZDk3MTU5YjkwZGRkNDYzZTA4MTY0MjJkNjIxZTEzNSKAAWZkNzgwY2UwNzY0MGJhNDExMjI0ODY5MTU4MWE1OTU4NDVmZTc2MmJmM2ZlYjQ5Yjg0Mzk3NGFhZTU3ODQ3OGM2YmY1MTg3MzllY2RjNDlkNzAxOTM4M2QzYmQ5ZTNhYTZmYTBhZjgzODRiNDQ5MThmMGJmZjM3NDAyYjUxMGIyKMzfgeYF"
                        }
                    ]
                },
                ...
            ],
            "header": {
                "batch_ids": [
                    "fa2d1a209ad04fd2ad7fb5183976e647cc47b4c08e2e578097afc2566a0284e760eb3f2ff8f72f290765211d4da3341f23091cc7a16805025a17c04a90818a44",
                    "661492181b838636b11ee347312bf5346b4231e0510c5c5bec27ea999ea389a66a1264696ea53e3b30e29b03192154bed8d160f035706da4f0da7f0be107a2b2"
                ],
                "block_num": "189",
                "consensus": "RGV2bW9kZdG76dVw7Q7VRgkNr6HxHnnJxNwI+iySmLepFZPJXvDa",
                "previous_block_id": "fd780ce07640ba4112248691581a595845fe762bf3feb49b843974aae578478c6bf518739ecdc49d7019383d3bd9e3aa6fa0af8384b44918f0bff37402b510b2",
                "signer_public_key": "02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135",
                "state_root_hash": "693d08c1520c9c1b2dba54ae147bf689f6209f74e304f8ed44e1ec818a08072e"
            },
            "header_signature": "fe56a16dab009cc96e7125c647b6c71eb1063818cf8dece283b125423ecb184f7f1e61802bf66382da904698413f80831031f8a1b29150260c3fa4db537fdf4c"
        },
        ...
    ]
}      
```

Get a list of blocks' identifiers (can be combined with other parameters like `--limit`):

```bash
$ remme block get-list --ids-only --node-url=node-6-testnet.remme.io
{
    "result": [
        "b757c74fbcd57ae12577b71490878affb6b688434c2e20170138760e72e937ca1bb3d6773e2ef37b5151ed74dcb663114a181072e0870e7a4d452c58659a6dbb",
        "585f23725d1236e90e2b961b0c0c1404aba0ba5a96e4d85cd2f048b1d61b027669153e3618c84fc09a8041f8e149b97d50a89ee7761d0458cd57c63d5f354cbd",
        ...
    ]
}
```

Get information about the block by its identifier — ``remme block get``:

| Arguments | Type   | Required | Description                                            |
| :-------: | :----: | :------: | ------------------------------------------------------ |
| id        | String | Yes      | Identifier of the block to fetch information about by. |
| node-url  | String | No       | Node URL to apply a command to.                        |

```bash
$ remme block get \
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
            {
                "header": {
                    "signer_public_key": "02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135",
                    "transaction_ids": [
                        "e112670497e184e7b3d7fab962440fe4be7e905ce7c73712a1a7ca9c65fba00b23fcf62cc640944bdac3c7ab1414d5d5c6fe3edf2f755d3dbca982b3d83394e2"
                    ]
                },
                "header_signature": "cd11713211c6eb2fe4adc0e44925c1f82e9300e0b8827bd3c73d8be10e61cd2b1e8da810078845ca1665b4adf7f691ad731ab4cea0fc994c55a8863b30220c6e",
                "trace": false,
                "transactions": [
                    {
                        "header": {
                            "batcher_public_key": "02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135",
                            "dependencies": [],
                            "family_name": "account",
                            "family_version": "0.1",
                            "inputs": [
                                "112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202",
                                "112007a90f66c661b32625f17e27177034a6d2cb552f89cba8c78868705ae276897df6"
                            ],
                            "nonce": "7d5445ee5559645bd72db237a0b448bec64c33c70be214e974da7ad0f523278cbb0c77c4a690ff751b68c318437ece2aef6eb29518a41c5ec8037218ed6fbf0d",
                            "outputs": [
                                "112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202",
                                "112007a90f66c661b32625f17e27177034a6d2cb552f89cba8c78868705ae276897df6"
                            ],
                            "payload_sha512": "bb0e5d9898c92b9b922a4de677ed6cab106ed5c90e975941cd5d1e22ce6f0d397b812c7152796b410a9cfe1d3fd4af080c6ee88c9548fc8393e7a55cae596b8c",
                            "signer_public_key": "02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135"
                        },
                        "header_signature": "e112670497e184e7b3d7fab962440fe4be7e905ce7c73712a1a7ca9c65fba00b23fcf62cc640944bdac3c7ab1414d5d5c6fe3edf2f755d3dbca982b3d83394e2",
                        "payload": "EksSRjExMjAwN2Q3MWZhN2UxMjBjNjBmYjM5MmE2NGZkNjlkZTg5MWE2MGM2NjdkOWVhOWU1ZDlkOWQ2MTcyNjNiZTZjMjAyMDIY6Ac="
                    }
                ]
            }
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

### Batch

Get a batch by identifier — ``remme batch get``:

| Arguments | Type   | Required | Description                     |
| :-------: | :----: | :------: | ------------------------------- |
| id        | String | Yes      | Identifier to get a batch by.   |
| node-url  | String | No       | Node URL to apply a command to. |

```bash
$ remme batch get \
      --id=61a02b6428342c4ac2bb0d9d253d48fd229d9b0a1344b2c114f22f127e7bfaeb3e2be19574fbd48776b71bbdb728ee1eedab2c2a4f0b951251899470318cee9d \
      --node-url=node-6-testnet.remme.io
{
    "result": {
        "header": {
            "signer_public_key": "029de6b8d982a714b5e781e266a4f1e0ef88ba1ef6bd4a96e7b7f21da164d84cda",
            "transaction_ids": [
                "73b913d679d7ec5ccd6658909b71ebdbdef5d01ea510c620639f519812efa76e66710d1d2f932f6e23775f907e5ed6c41d80b1fe227dd3316ac82452d20487c8"
            ]
        },
        "header_signature": "61a02b6428342c4ac2bb0d9d253d48fd229d9b0a1344b2c114f22f127e7bfaeb3e2be19574fbd48776b71bbdb728ee1eedab2c2a4f0b951251899470318cee9d",
        "trace": false,
        "transactions": [
            {
                "header": {
                    "batcher_public_key": "029de6b8d982a714b5e781e266a4f1e0ef88ba1ef6bd4a96e7b7f21da164d84cda",
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
                    "payload_sha512": "0104c4f12d1bc53ee1d14a71a036305cfc2b82b41cee52cc6d7b9d0905d5fa0aa0db8d01e28531676b319552ce2a33e719386cb3eb5b938d8996abfa64bd3488",
                    "signer_public_key": "029de6b8d982a714b5e781e266a4f1e0ef88ba1ef6bd4a96e7b7f21da164d84cda"
                },
                "header_signature": "73b913d679d7ec5ccd6658909b71ebdbdef5d01ea510c620639f519812efa76e66710d1d2f932f6e23775f907e5ed6c41d80b1fe227dd3316ac82452d20487c8",
                "payload": "CtMCCNkzEoABMDk1YmM0MjQ4YjU4NjYzMTllNGE5YWQ2YzZkMWFkNGI3MDA5OTFmNmJjMGVjMGRlN2UwNGJhMTAxNGYxYTU3ZTI4OWE1MmE0MjVhNzc3ZTg3YjgzMzFjMjVkNmU4NTIwNmY1ZGZmNjk1ZGFiMTI0Yzc3YjQ2OWNhMzhhNDFjY2QaQjAyZjU3OWQ3NzU0ZTg3YmYwZTRlZDJlNTBmYjEzNmI4ZTM1NTg2OGU0ODMwODkwZTE0MjRlOWZmZGVhZjZiZTE2MyKAATQzMjA5ODdiYzU3YTJjMmZlYTMzNWFkM2UxZTFmNGU0NDk3YTJhYmM2MmFhYzdlZDIwY2RmZmY5NWFhY2JiMDgyNGU2ZTBmMGFiNGI4MmQxOGExOWEyYTVmMDE3OGE2Mjk0MDIyNjhmODExNzAyZmUxZTk0MzFmZmExMGEyNWI2KMTIreYF"
            }
        ]
    }
}
```

Get a batch status by its identifier — ``remme batch get-status``:

| Arguments | Type   | Required | Description                          |
| :-------: | :----: | :------: | ------------------------------------ |
| id        | String | Yes      | Identifier to get a batch status by. |
| node-url  | String | No       | Node URL to apply a command to.      |

```bash
$ remme batch get-status \
      --id=61a02b6428342c4ac2bb0d9d253d48fd229d9b0a1344b2c114f22f127e7bfaeb3e2be19574fbd48776b71bbdb728ee1eedab2c2a4f0b951251899470318cee9d \
      --node-url=node-6-testnet.remme.io
{
    "result": "COMMITTED"
}
```

Get a list of batches — ``remme batch get-list``:

| Arguments | Type    | Required | Description                                              |
| :-------: | :-----: | :------: | -------------------------------------------------------- |
| ids       | String  | No       | Identifiers to get a list of batches by.                 |
| start     | String  | No       | Batch identifier to get a list of batches starting from. |
| limit     | Integer | No       | Maximum amount of batches to return.                     |
| head      | String  | No       | Block identifier to get a list of batches from.          |
| reverse   | Bool    | No       | Parameter to reverse result.                             |
| ids-only  | Bool    | No       | The flag to get a list of batches' identifiers.          |
| node-url  | String  | No       | Node URL to apply a command to.                          |

```bash
$ remme batch get-list \
      --ids='6bd3382e3deef34d0bc63a7b450c88c7ae00152f5168c7b4dc4357feff6d52175209919cd0710441fa2768f4c12adf97143440ef8414bb5144b9459d78ff3e0e, 7a5daba99d5757adc997ea6a0b1b83263b3c16604dbd83c0153dc01c9fd780af4b570338c2ec60e086b1db58a4397a4dc661d6c93b0a7250fe75642e15b26e81' \
      --start=6bd3382e3deef34d0bc63a7b450c88c7ae00152f5168c7b4dc4357feff6d52175209919cd0710441fa2768f4c12adf97143440ef8414bb5144b9459d78ff3e0e \
      --limit=2 \
      --head=57a7944497ca41f424932ae6b70897e7086652ab98450d4aba6a02a2d891501460947812a41028b8041f087066df6dc7e1100c4b0e5cc94bb58b002f6950eb02 \
      --reverse \
      --node-url=node-6-testnet.remme.io
{
    "result": [
        {
            "header": {
                "signer_public_key": "03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad",
                "transaction_ids": [
                    "376efc69c217a0b9deb545348ca32664ce61b3e35706252d1d0374bdb93b10e62abc35fc16a3d19f0d8346ddbadc1c0974af6b4364f98ffea66de72cfb11b238"
                ]
            },
            "header_signature": "ed0fc04a114e87ae7d2046db667bb82cf5a9bbab9b51024c4192b569a997785260ea5f4ad55ac4e2a167a04d50806b00f35b2a553bb4072bb5a36be7ba49b9be",
            "trace": false,
            "transactions": [
                {
                    "header": {
                        "batcher_public_key": "03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad",
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
                        "payload_sha512": "7b11153de66545d8c8847004425f9c5815483636688e79fd2bfbb6d979218fbeb7ccdcb244241d8d52ea38a1b1d62c5d178cf74c3c7b5f496936059c616163e2",
                        "signer_public_key": "03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad"
                    },
                    "header_signature": "376efc69c217a0b9deb545348ca32664ce61b3e35706252d1d0374bdb93b10e62abc35fc16a3d19f0d8346ddbadc1c0974af6b4364f98ffea66de72cfb11b238",
                    "payload": "CtMCCLwbEoABYmZiNzhkNGQxMWQyZjQzOWRlZjkzNTc2Y2YyN2M0NGVhZTNmYmMyM2Q2ODAwNmUyNGRlYmJmZGYxZWRiNmQ4MDY5MDExYzYxNWZjNjk4NGMxM2EzZDJjMDMyYzFhZTY2NWYzNmZjZTUxOWVjZTdlOGI2YmFjMGMxYWRlMTgxYWYaQjAzNzM4ZGYzZjRhYzM2MjFiYThlODk0MTNkM2ZmNGFkMDM2YzNhMGE0ZGJiMTY0YjY5NTg4NWFhYjZhYWI2MTRhZCKAAThmMjJkYjUyNTUyYzQ3MjE4ZTc0ZmE4OGExZTU2NGJhZTE1YjYwMmY0ZTI3ZTZiYTYwOWI0NzM4YjY0ZTllZTYzYzcwMjM4MjI3ZWU0NTU1OTVhNjMzYTIzOWU5ZGZiMWNiMGMxNWI1MzVhZGJkYTZmMGE2Yjk3MmU3ZWU3MWQyKLvr4eYF"
                }
            ]
        }
    ]
}
```

Get a list of batches' identifiers (can be combined with other parameters like `--limit`):

```bash
$ remme batch get-list --ids-only --node-url=node-6-testnet.remme.io
{
    "result": [
        "6bd3382e3deef34d0bc63a7b450c88c7ae00152f5168c7b4dc4357feff6d52175209919cd0710441fa2768f4c12adf97143440ef8414bb5144b9459d78ff3e0e",
        "7a5daba99d5757adc997ea6a0b1b83263b3c16604dbd83c0153dc01c9fd780af4b570338c2ec60e086b1db58a4397a4dc661d6c93b0a7250fe75642e15b26e81",
        ...
    ]
}
```

### Node

Get the node configurations — ``remme node get-configs``:

| Arguments | Type   | Required | Description                     |
| :-------: | :----: | :------: | ------------------------------- |
| node-url  | String | No       | Node URL to apply a command to. |

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

| Arguments | Type   | Required | Description                     |
| :-------: | :----: | :------: | ------------------------------- |
| node-url  | String | No       | Node URL to apply a command to. |

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

Get the initial stake of the node — ``remme node get-initial-stake``:

| Arguments | Type   | Required | Description                     |
| :-------: | :----: | :------: | ------------------------------- |
| node-url  | String | No       | Node URL to apply a command to. |

```bash
$ remme node get-initial-stake --node-url=node-27-testnet.remme.io
{
    "result": 250000
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

Get a list of states — ``remme state get-list``:

| Arguments | Type    | Required | Description                                  |
| :-------: | :-----: | :------: | -------------------------------------------- |
| address   | String  | No       | Account address to get a list of states by.  |
| limit     | Integer | No       | Maximum amount of transactions to return.    |
| head      | String  | No       | Block identifier to get a list of states to. | 
| reverse   | Bool    | No       | Parameter to reverse result.                 |
| node-url  | String  | No       | Node URL to apply a command to.              |

```bash
$ remme state get-list \
    --address=00001d0024b20fbe284cdaca250b30f40c30c3999e2cafbace268f2f26d9d493a4d09b \
    --limit=1 \
    --head=d3b9c12f76bf33ed0fb70df9f0ab9af9b3e29a6c9cf3e446fb2d799bdae07a92721cc52a0f3c683a972d562abae6a041d09a90c4157fce9bd305036e1cb15149 \
    --reverse \
    --node-url=node-6-testnet.remme.io
{
    "result": [
        {
            "address": "00001d0024b20fbe284cdaca250b30f40c30c3999e2cafbace268f2f26d9d493a4d09b",
            "data": "CmkKH25vZGVfYWNjb3VudF9wZXJtaXNzaW9uc19wb2xpY3kSRggBEkIwMzczOGRmM2Y0YWMzNjIxYmE4ZTg5NDEzZDNmZjRhZDAzNmMzYTBhNGRiYjE2NGI2OTU4ODVhYWI2YWFiNjE0YWQ="
        }
    ]
}
```

### Transaction

Get a list of transactions — ``remme transaction get-list``:

| Arguments   | Type    | Required | Description                                                     |
| :---------: | :-----: | :------: | --------------------------------------------------------------  |
| ids         | String  | No       | Identifiers to get a list of transactions by.                   |
| start       | String  | No       | Transaction identifier to get a list transaction starting from. |
| limit       | Integer | No       | Maximum amount of transactions to return.                       |
| head        | String  | No       | Block identifier to get a list of transactions from.            |
| reverse     | Bool    | No       | Parameter to reverse result.                                    |
| ids-only    | Bool    | No       | The flag to get a list of transactions' identifiers.            |
| family-name | String  | No       | List of transactions by its family name.                        |
| node-url    | String  | No       | Node URL to apply a command to.                                 |

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

Get a list of transactions' identifiers (can be combined with other parameters like `--limit`):

```bash
$ remme transaction get-list --ids-only --node-url=node-6-testnet.remme.io
{
    "result": [
        "eb662acc48d313c9bba4a72359b0462d607bba8fc66aeb3d169d02fafd21849b6bf8bea8396b54b6fc907e1cce2a386f76bd19889d0f3e496b45b8440b161ebc",
        "206a3767f368c1db9d07b273f80d4824d201ae61b9ced8a6aeedac58032c5557544ac622d5e3fd59f6d9873d97af1c6114d0131b4b1a191cbba7d5a8aa5a3caf",
        "63ed3259b6067525ae241a12f66b5be1e1502cdbd6f475b139bf94cf4ba842643577835fcef0482d25190243b8dfab3a1f9913f7fd0edc425ad0c19333d8bd4b",
        ...
    ]
}
```

Get a transaction by identifier — ``remme transaction get``:

| Arguments | Type   | Required | Description                       |
| :-------: | :----: | :------: | --------------------------------- |
| id        | String | Yes      | Identifier to get transaction by. |
| node-url  | String | No       | Node URL to apply a command to.   |

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

### Receipt

Get a list of the transaction's receipts by identifiers — ``remme receipt get``:

| Arguments | Type   | Required | Description                                             |
| :-------: | :----: | :------: | ------------------------------------------------------- |
| ids       | String | True     | Identifiers to get a list of transaction's receipts by. |
| node-url  | String | No       | Node URL to apply a command to.                         |

```bash
$ remme receipt get \
      --ids='e79a883581c184787360de8607c5f970cdeeaa684af3e50d8532aa9dd07afa8e7fc92f0dc509b41b9695e795704bdd50455bebd1ed327a5330710ba40698b492, 
      6593d21046519022ba32c98e934d7dfc81e8b4edf6c064dbf70feb13db4310873ec00816bce8660cafd4fa2a8c80d0147d63cf616c624babd03142c694272017' \
      --node-url='159.89.104.9'
{
    "result": [
        {
            "data": [],
            "events": [],
            "id": "e79a883581c184787360de8607c5f970cdeeaa684af3e50d8532aa9dd07afa8e7fc92f0dc509b41b9695e795704bdd50455bebd1ed327a5330710ba40698b492",
            "state_changes": [
                {
                    "address": "00b10c0100000000000000000000000000000000000000000000000000000000000000",
                    "type": "SET",
                    "value": "CL0BGIACIKwC"
                },
                {
                    "address": "00b10c00000000000000000000000000000000000000000000000000000000000000bd",
                    "type": "SET",
                    "value": "CL0BEoABZmQ3ODBjZTA3NjQwYmE0MTEyMjQ4NjkxNTgxYTU5NTg0NWZlNzYyYmYzZmViNDliODQzOTc0YWFlNTc4NDc4YzZiZjUxODczOWVjZGM0OWQ3MDE5MzgzZDNiZDllM2FhNmZhMGFmODM4NGI0NDkxOGYwYmZmMzc0MDJiNTEwYjIaQjAyZDFmYmRhNTBkYmNkMGQzYzI4NmE2YTlmYTcxYWE3Y2UyZDk3MTU5YjkwZGRkNDYzZTA4MTY0MjJkNjIxZTEzNSKAAWZlNTZhMTZkYWIwMDljYzk2ZTcxMjVjNjQ3YjZjNzFlYjEwNjM4MThjZjhkZWNlMjgzYjEyNTQyM2VjYjE4NGY3ZjFlNjE4MDJiZjY2MzgyZGE5MDQ2OTg0MTNmODA4MzEwMzFmOGExYjI5MTUwMjYwYzNmYTRkYjUzN2ZkZjRjKIzggeYF"
                }
            ]
        },
        ...
    ]
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
$ coverage run -m pytest -vv tests
$ coverage report -m && coverage xml
$ flake8 cli && flake8 tests/
$ bash <(curl -s https://linters.io/isort-diff) cli tests
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
