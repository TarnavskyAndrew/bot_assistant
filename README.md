# My Python Projects

Welcome to my repository with Python projects!  
Here I learn, practice and improve my coding skills.

---

<details>
<summary>Bot Assistant — Personal CLI Helper</summary>


*A Python console bot for contact management, with backup support, data validation and multilingual support.*


## Features

- Add, change, delete contacts
- Number validation
- Support for multiple phone numbers with region codes
- Display all contacts
- Add and show birthdays, see upcoming ones
- Multilingual: English and Ukrainian
- Automatic backup and restore
- Personalized greeting based on last visit
- Random "good mood" message with each greeting
- Extensible architecture
- Command line support

## Supported Commands
Use the `help` command inside the bot to view all available commands.

### Functional Overview

Bot Assistant is a command-line personal assistant that allows you to manage your contact book efficiently. 
Here's what it can do:

| Command                              | Description                                                |
|--------------------------------------|------------------------------------------------------------|
| `hello`                              | Greet based on last visit time + joke of the day           |
| `add <name> <phone>`                 | Add a new contact with a phone number                      |
| `change <name> <old> <new>`          | Change an existing contact's phone number                  |
| `phone <name>`                       | Show the phone number(s) of a contact                      |
| `all`                                | Display all contacts in the address book                   |
| `add-birthday <name> <YYYY-MM-DD>`   | Add a birthday for a contact                               |
| `show-birthday <name>`               | Show the birthday of a contact                             |
| `birthdays`                          | Show upcoming birthdays within the next 7 days             |
| `delete <name>`                      | Delete a contact                                           |
| `help`                               | Display available commands and usage instructions          |
| `lang`                               | Change the interface language (UA / EN)                    |
| `restore`                            | Restore the contact book from the last backup              |
| `exit` or `close`                    | Exit the assistant and save all data                       |
---


## Project structure

```python
└── root_package/
    ├── pyproject.toml
    ├── poetry.lock
    ├── Dockerfile
    ├── README.md
    ├── CHANGELOG.md
    ├── src/
    │   └── bot_assistant/
    │       ├── main.py
    │       ├── models/
    │       ├── views/
    │       ├── handlers/
    │       ├── utils/
    │       └── data/
    ├── tests/
    ├── dev_tools/
    ├── logs/
    ├── .vscode/
    ├── .dockerignore
    ├── .gitignore
    └── bot_diagram.svg
```


## Project status

The project is in progress and will be improved.

---
</details>


<details>
<summary>Bot Assistant — Run the bot</summary>

---

### Run the bot

```bash
git clone https://github.com/TarnavskyAndrew/bot_assistant
```

```bash
pip install poetry
```
```bash
poetry install
```
```bash
poetry shell
```
```bash
poetry run run-bot
```

---

### Run with Docker

You can run the bot in an isolated Docker container:

#### 1. Build the Docker image
```bash
docker build -t tarnavsky/bot_assistant:latest .
```

#### Or pull the pre-built image
```bash
docker pull tarnavsky/bot_assistant:latest
```

#### 2. Run the bot interactively
```bash
docker run -it tarnavsky/bot_assistant:latest
```

> Make sure you're in the root project directory and Docker is installed and running.

```bash
https://hub.docker.com/repository/docker/tarnavsky/bot_assistant
```

---
</details>


<details>
<summary>Bot Assistant — Changelog</summary>

---
<details>
<summary>[1.2.0] - 2025-06-10</summary>

## [1.2.0] - 2025-06-10
### Added
`hello` command enhancements:
- Greets user based on last visit timestamp
- Displays a random joke or motivational message
- Random "good mood" message with each greeting
- Includes help prompt for user guidance
### Changed
- Improved translation coverage for EN / UA
- Refined logging for startup and greetings

---
</details>


<details>
<summary>[1.1.0] - 2025-06-05</summary>

## [1.1.0] - 2025-06-05
### Added
- Logging for help and other core commands
- Centralized translation support via translate.py
### Changed
Refactored `help` command:
- Displayed in clean, aligned tabular format
- Multilingual descriptions and usage examples

---
</details>


<details>
<summary>[1.0.0] - 2025-06-01</summary>

## [1.0.0] - 2025-06-01
### Added
- Initial implementation of CLI assistant
- Basic command set:
 `add`, `change`, `phone`, `all`, `help`, `delete`, `exit`
- Birthday and restore support
- Data persistence with addressbook.pkl
- Language switching between Ukrainian and English

---
</details>
</details>

