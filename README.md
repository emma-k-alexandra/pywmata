# WMATA

WMATA is an easy to use Python interface to the [Washington Metropolitan Area Transit Authority API](https://developer.wmata.com).

## Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Getting Started](#getting-started)
  - [Design](#design)
  - [Using `MetroRail`](#using-MetroRail)
  - [Using `MetroBus`](#using-MetroBus)
- [Testing](#testing)
- [Dependencies](#dependencies)
- [Contact](#contact)
- [License](#license)

## Requirements

- Python 3.8

## Installation

```bash
pip install wmata
```

## Usage

### Getting Started

```python
from wmata import MetroRail, Station

client = MetroRail(api_key)

trains = client.next_trains(Station["A01"])
```

### Design

WMATA breaks the WMATA API into two components: `MetroRail` and `MetroBus`.



#### `MetroRail`

Provides access to all MetroRail related endpoints.

##### Using `MetroRail`

```python
import wmata

client = wmata.MetroRail(api_key)

trains = client.next_trains(wmata.Station["A01"])
```

#### `MetroBus`

Provides access to all MetroBus related endpoints.



##### Using `MetroBus`

```python
from wmata import MetroBus

client = MetroBus(api_key)

routes = client.routes()
```

## Testing

Run

```bash
python setup.py test
```

Tests use VCRpy to avoid network requests.



## Dependencies

- Requests
  
  

### Dev Dependencies

- VCRpy



## Contact

Feel free to email questions and comments to [emma@emma.sh](mailto:emma@emma.sh)



## License

WMATA is released under the MIT license. [See LICENSE](https://github.com/emma-k-alexandra/pywmata/blob/master/LICENSE) for details.
