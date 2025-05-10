<br />
<div align="center">
  <h3 align="center">Airport service</h3>

  <p align="center">
    Manage airport database
    <br />
    <a href="https://github.com/Windings-Lab/airport-service"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Windings-Lab/airport-service/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/Windings-Lab/airport-service/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#docker">Docker</a></li>
        <li><a href="#optional">Optional</a></li>
      </ul>
    </li>
    <li>
      <a href="#environment">Environment</a>
      <ul>
        <li><a href="#development">Development</a></li>
        <li><a href="#production">Production</a></li>
        <li><a href="#secret-key-generation">Secret key generation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Airport API portfolio demonstration


### Built With

* [![Django][Django]][Django-url]
* [![NeonTech][NeonTech]][NeonTech-url]
* [![PostgreSQL][Postgres]][Postgres-url]
* [![UV][UV]][UV-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3.13
* UV package manager

### Installation

1. Using UV package manager run commands:<br>
Look into UV documentation for more information
```sh
  uv sync --locked
```
2. Create .env file and fill everything
3. Run django server
```sh
  python manage.py runserver
```

### Docker

1. Create .env file and fill it. Do not include `SECRET_KEY` and `DB_PASS`
2. Export to the shell env variables `SECRET_KEY` and `DB_PASS`
3. Run docker-compose
```sh
  docker-compose up
```

### Optional

* Install database data
```sh
  python manage.py loaddata .\docs\dump.json;
```

* Login with
```
Email: admin@example.com
Password: 12345
```
* Exclude development packages like debug_toolbar. Look `pyproject.toml`
* ! ONLY FOR PRODUCTION
```sh
  uv sync --locked --no-dev
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Environment -->
## Environment

### Development
Using `SQLite`
```dotenv
# Django
DJANGO_SETTINGS_MODULE=app.settings.dev
SECRET_KEY
# Python
PYTHONUNBUFFERED=1
```
### Production
Using `PostgreSQL`
```dotenv
# Database
DB_HOST
DB_NAME
DB_PASS # Password
DB_PORT
DB_USER
# Django
DJANGO_SETTINGS_MODULE=app.settings.prod
SECRET_KEY
# Python
PYTHONUNBUFFERED=1
```
### Secret key generation
By default it will use django insecure key if not set. While using docker-compose it will force you to set `SECRET_KEY`
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Django]: https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[NeonTech]: https://img.shields.io/badge/Neon_Tech-Database-F6ef55c?style=flat
[NeonTech-url]: https://neon.tech/home
[Postgres]: https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[UV]: https://img.shields.io/badge/UV-Package_Manager-2f183c?style=flat&labelColor=251330
[UV-url]: https://docs.astral.sh/uv/