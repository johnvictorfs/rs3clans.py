# rs3clans.py Change Log

### 1.0.3
- `Clan.get_member(name)` method now returns the name of the player found in the dict as below:
    ```python3
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
    >>> import rs3clans
    >>> player = rs3clans.Player('nriver')
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
