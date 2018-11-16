# rs3clans.py Change Log

[![PyPI](https://img.shields.io/pypi/v/rs3clans.svg)](https://pypi.org/project/rs3clans/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rs3clans.svg)](https://pypi.org/project/rs3clans/) [![Build Status](https://travis-ci.org/johnvictorfs/rs3clans.py.svg?branch=master)](https://travis-ci.org/johnvictorfs/rs3clans.py)

***

### 1.0.6

- Changed all `__str__` methods to just `__repr__` methods that are more concise.
```python3
>>> # Old
>>> import rs3clans
>>> print(rs3clans.Player('nriver')
>>> Name: NRiver Clan: Atlantis Exists: True

>>> # New
>>> import rs3clans
>>> rs3clans.Player('nriver')
>>> Player(name='NRiver', clan='Atlantis', exists=True)
```

***

### 1.0.5
- `Clan` objects can now be iterated through as if you were iterating over `Clan.member.items()` (requires `set_dict` parameter when creating `Clan` object to be `True` (`True` by default))
    - Example:
        ```python3
        >>> clan = rs3clans.Clan('atlantis')
        >>> for member in clan:
        ...     print(member)
        ...
        ('Pedim', {'rank': 'Owner', 'exp': 962627411})
        ('Tusoroxo', {'rank': 'Deputy Owner', 'exp': 1157686923})
        ('Acriano', {'rank': 'Overseer', 'exp': 1857267476})
        ('Cogu', {'rank': 'Overseer', 'exp': 1576814120})
        ('Black bullet', {'rank': 'Overseer', 'exp': 909580894})
        ('NRiver', {'rank': 'Overseer', 'exp': 1043065027})
        (...)
        >>> clan = rs3clans.Clan('atlantis', set_dict=False)
        >>> for member in clan:
        ...     print(member)
        >>> 
        ```

- Now using requests for every `Player` method, instead of using urllib for one, no usage changes here

- Now the creation of a `Player` or `Clan` object raises `ConnectionError` if it isn't possible to connect to one or more of RS3's API's used
    - Also added the following attributes so the status codes of each request made in those objects can be diagnosed:
        - `Clan.hiscores_status_code`
        - `Player.runemetrics_status_code`
        - `Player.runemetrics_status_code`
    ```python3
    >>> import rs3clans
    >>> try:
    ...     clan = rs3clans.Clan('atlantis')
    ... except ConnectionError:
    ...     print("Error when connecting to RS3's Clan API")
    ...     print(f"Status Code: {clan.hiscores_status_code}")
    ... except rs3clans.ClanNotFoundError:
    ...     print(f"Error. Clan {clan.name} does not exist")
    ...
    >>> try:
    ...     player = rs3clans.Player('nriver', runemetrics=True)
    ... except ConnectionError:
    ...     print("Error when connecting to RS3's Player API")
    ...     print(f"Status Code from Runemetrics API: {player.runemetrics_status_code}")
    ...     print(f"Status Code from Player Details API: {player.runemetrics_status_code}")
    ...
    >>> 
    ```

***

### 1.0.4
- Fixed `Player.exists()` method always returning False unless `runemetrics` argument was passed as true or `Player.set_runemetrics_info()` was called

***

### 1.0.3
- `Clan.get_member(name)` method now returns the name of the player found in the dict as below:
    ```python3
    >>> from rs3clans import Clan
    >>> clan = Clan('atlantis')
    >>> clan.get_member('nriver')
    {'rank': 'Overseer', 'exp': 1043065027, 'name': 'NRiver'}
    ```

***

### 1.0.2
- Fixed `Clan.get_member(name)` not working with names that had spaces on them

***

### 1.0.1
- Added continuous integration with tests using [`Travis CI`](https://travis-ci.org)
    - [Project URL](https://travis-ci.org/johnvictorfs/rs3clans.py)

- Lots of changes to Documentation

***

### 1.0.0
- Added `runemetrics` (bool, default=True) argument to `Player`
    - If True, `Player.set_runemetrics_info()` will be ran by default

- Added the following attributes to `Player`:
    ```python3
    Player.quests_not_started  # Number of quests the Player has not started
    Player.quests_started  # Number of quests the Player has started
    Player.quests_complete  # Number of quests the Player has completed
    Player.skill_values  # Dictionary with information about the Player skill values
    ```

- Added a `Skill` object with the following attributes:
    ```python3
    Skill.name
    Skill.xp  # Aliased as Skill.exp
    Skill.level
    Skill.rank
    Skill.id
    ```

- Added a `Player.skill(skill_name)` method that returns information of that skill about the Player, it returns a `Skill` object
    - `skill_name` can be the Skill ID or Name (case-insensitive)
    ```python3
    >>> from rs3clans import Player
    >>> player = Player('nriver')
    >>> player.skill('agility').level
    99
    # Skill name is case-insensitive
    >>> player.skill('AtTaCk').rank
    68311
    # ID 8 is Woodcutting
    >>> player.skill(8).exp
    14054178.6
    ```

- Added Unit Testing to project (using [`pytest`](https://docs.pytest.org/en/latest/))
    - [Tests folder](/tests/) 
    - Tests still needs a lot of refining
