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
    * [Transactions](#transactions)
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

### Transactions

Get list of transactions — ``remme transactions get-list``:

| Arguments   | Type   |  Required | Description                                            |
| :---------: | :----: | :-------: | -----------------------------------------------------  |
| ids         | String |  No       | List transaction by its identifier.                    |
| start       | String |  No       | Id to start paging (inclusive).                        |
| limit       | Integer|  No       | Number of transaction to return.                       |
| head        | String |  No       | Id of head block.                                      |
| reverse     | String |  No       | Reverse result.                                        |
| node-url    | String |  No       | Apply the command to the specified node by its URL.    |
| family-name | String |  No       | List transaction by its family name.                   |

```bash
$ remme transactions get-list \
    --limit=3 \
    --ids=13e46c3b07848b3a38be301b13a0a0b1f73b53766345b64eea1746031bb9672f5e6a34e123f56ce2a1af8523741d996c6f4c3cbf7bd75511547bcc4297d3c5cc \
    --start=13e46c3b07848b3a38be301b13a0a0b1f73b53766345b64eea1746031bb9672f5e6a34e123f56ce2a1af8523741d996c6f4c3cbf7bd75511547bcc4297d3c5cc \
    --head=792bef7ace0c13e47ddc28328952ed0494d28ecabacec961808b2c7bf93f765f5df2e8e32d1487fdb2d24b5cd0cde0ea2902a019243b9917793d3c26e834d8cf \
    --family_name=account
{
   "head": "792bef7ace0c13e47ddc28328952ed0494d28ecabacec961808b2c7bf93f765f
            5df2e8e32d1487fdb2d24b5cd0cde0ea2902a019243b9917793d3c26e834d8cf",
   "paging": {
      "limit": 3,
      "start": "13e46c3b07848b3a38be301b13a0a0b1f73b53766345b64eea1746031bb9672f
                5e6a34e123f56ce2a1af8523741d996c6f4c3cbf7bd75511547bcc4297d3c5cc",
      "next": ""
   },
   "data": []
}
```

Get single transaction by id — ``remme transactions get-single``:

| Arguments   | Type   |  Required | Description                                            |
| :---------: | :----: | :-------: | -----------------------------------------------------  |
| identifier  | String |  Yes      | Transaction by its identifier.                         |
| node-url    | String |  No       | Apply the command to the specified node by its URL.    |

```bash
$ remme transactions get-single \
    --identifier=13e46c3b07848b3a38be301b13a0a0b1f73b53766345b64eea1746031bb9672f5e6a34e123f56ce2a1af8523741d996c6f4c3cbf7bd75511547bcc4297d3c5cc 
{
   "data": {
      "header": {
         "batcher_public_key": "02a65796f249091c3087614b4d9c292b00b8eba580d045ac2fd781224b87b6f13e",
         "family_name": "sawtooth_settings",
         "family_version": "1.0",
         "inputs": [
            "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b",
            "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c12840f169a04216b7",
            "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1918142591ba4e8a7",
            "000000a87cb5eafdcca6a8f82af32160bc53119b8878ad4d2117f2e3b0c44298fc1c14"
         ],
         "outputs": [
            "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b",
            "000000a87cb5eafdcca6a8f82af32160bc53119b8878ad4d2117f2e3b0c44298fc1c14"
         ],
         "payload_sha512": "9d20b85d9683f3a8a83107bf282a90ca53ea4dc892ee8dd0bf116982e0a220a5245dd6b4614a715d826ce83bad1b35e1b9210424382555cde78b87002c0bf6b7",
         "signer_public_key": "02a65796f249091c3087614b4d9c292b00b8eba580d045ac2fd781224b87b6f13e",
         "dependencies": [],
         "nonce": ""
      },
      "header_signature": "13e46c3b07848b3a38be301b13a0a0b1f73b53766345b64eea1746031bb9672f5e6a34e123f56ce2a1af8523741d996c6f4c3cbf7bd75511547bcc4297d3c5cc",
      "payload": "CAESbAopc2F3dG9vdGgudmFsaWRhdG9yLmJsb2NrX3ZhbGlkYXRpb25fcnVsZXMSK05vZlg6MSxibG9ja19pbmZvO1hhdFk6YmxvY2tfaW5mbywwO2xvY2FsOjAaEjB4ZDI5MWEyNmJhOGQzMWI3MA=="
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
