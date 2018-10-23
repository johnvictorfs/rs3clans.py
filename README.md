# rs3clans.py
[![PyPI](https://img.shields.io/pypi/v/rs3clans.svg)](https://pypi.org/project/rs3clans/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rs3clans.svg)](https://pypi.org/project/rs3clans/) [![Build Status](https://travis-ci.org/johnvictorfs/rs3clans.py.svg?branch=master)](https://travis-ci.org/johnvictorfs/rs3clans.py)

A Python 3 module wrapper for RuneScape 3 API

- [Change Log](CHANGELOG.md)

***
## Requirements:

- [`Python 3.6+`](https://www.python.org/)

- [`requests>=2.19.1`](http://docs.python-requests.org/en/master/)

***

## Setup with pip:

```bash
$ python3 -m pip install rs3clans
```

***

## Manual Setup:
*(Requires [`Git`](https://git-scm.com/))*
```bash
$ cd /your/projects/dir/
$ git clone https://github.com/johnvictorfs/rs3clans.py
$ cd rs3clans.py
$ python3 setup.py install
```

***

## Usage:

> Players

- Creating a Player object
    - Always check if a player actually exists before doing anything with it
```python
>>> from rs3clans import players
>>> player = players.Player(name='nriver')
>>> if player.exists:
...     pass
```

- Whether the player exists or not
```python
>>> player.exists
True
```

- Whether his Runemetrics Profile is Private or not
```python
>>> player.private_profile
False
```

- You can also pass the argument runemetrics as `False` if you don't want their runemetrics info to be set
    - This will make you unable to use some attributes from the Player class
```python
>>> player = players.Player(name='nriver', runemetrics=False)
```

- Getting a player's name
    - (if his Runemetrics Profile is private it will return the same name passed when creating object)
```python
>>> player.name
'NRiver'
```

- Getting a player's total Exp (requires Public Runemetrics Profile)
```python
>>> player.exp
1037291112
```

- Getting a player's Total Level (requires Public Runemetrics Profile)
```python
>>> player.total_level
```

- Getting a player's Combat Level (requires Public Runemetrics Profile)
```python
>>> player.combat_level
138
```

- Quests information about a player (requires Public Runemetrics Profile)
```python
>>> player.quests_not_started
32
>>> player.quests_started
5
>>> player.quests_complete
198
```

- Getting information on a specific skill of the player (requires Public Runemetrics Profile)
```python
>>> player.skill('agility').level
99
```

- Skill name is case-insensitive
```python
>>> player.skill('AtTaCk').rank
68311
```

- Can pass skill names as well as id
    - (8 = Woodcutting for example)
```python
>>> player.skill(8).exp
14054178.6
```

- Getting a player's title
```python
>>> player.title
'The Liberator'
```

- Verifying if a player's title is a suffix or not
```python
>>> player.suffix
True
```

- Getting a player's clan
```python
>>> player.clan
'Atlantis'
```

> Clans

- Creating a Clan object
    - Always check if a clan actually exists before doing anything with it
```python
>>> from rs3clans import clans
>>> try:
...     clan = clans.Clan('Atlantis')
... except clans.ClanNotFoundError:
...     print('Clan not found.')
```

- Getting a clan's total Exp
```python
>>> clan.exp
151349638333
```

- Getting information about a specific member in that clan
    - Clan.member attribute (dict) (requires case-sensitive name)
    - Clan.get_member() (method) (does not require case-sensitive name)
```python
>>> # Case-sensitive
>>> clan.member['NRiver']
{'rank': 'Overseer', 'exp': 1043065027}
>>> clan.member['NRiver']['rank']
'Overseer'
```

```python
>>> # Case-insensitive
>>> clan.get_member('nriver')
{'rank': 'Overseer', 'exp': 1043065027, 'name': 'NRiver'}
>>> clan.get_member('nRiVeR')['rank']
'Overseer'
```

- Getting the number of players in a clan
```python
>>> clan.count
499
```

- Getting the average Clan Exp per player in clan
```python
>>> clan.avg_exp
303305888.44288576
```

***

## Contributing:

- [Fork](https://github.com/johnvictorfs/rs3clans.py/fork) the repository

- Guidelines:
    - Follow Pep8 with the exception of `E501 (line too long)`

- Install Dev dependencies
    - With pipenv
        ```bash
        $ pipenv install --dev
        ```
    - Without pipenv
        ```bash
        $ pip install -r requirements-dev.txt
        ```

- Run the tests to make sure everything is ok
    ```bash
    $ pytest
    ```

- Send a GitHub Pull Request to the repository's [`master branch`](https://github.com/johnvictorfs/rs3clans.py/tree/master)

- Make your changes to the code in the directory `rs3clans.py/rs3clans/`

- Add necessary tests to the `rs3clans.py/tests/` directory ([`pytest docs`](https://docs.pytest.org/en/latest/))

- Run the tests again
    ```bash
    $ pytest
    ```

- Also run `flake8` just to check if the code style is also fine
    ```bash
    $ flake8 --ignore=E501
    ```

- If everything went fine then send a [Pull Request](https://github.com/johnvictorfs/rs3clans.py/pulls)

***