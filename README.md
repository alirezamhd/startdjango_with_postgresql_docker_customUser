
<div>
  <a href="https://instagram.com/alirezaa_mhd/">
    <img src="https://img.shields.io/badge/Instagram-purple?style=for-the-badge&logo=Instagram&logoColor=white" alt="instagram Badge"/>
  </a>
  <a href="https://t.me/alirezaa_mhd/">
    <img src="https://img.shields.io/badge/Telegram-blue?style=for-the-badge&logo=Telegram&logoColor=white" alt="telegram badge"/>
  </a>
</div>

# startdjango_with_postgresql_docker_customUser

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="django" alt="django" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original-wordmark.svg" title="docker" alt="docker" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original-wordmark.svg" title="postgres" alt="postgres" width="40" height="40"/>&nbsp;
</div>

This project is for easier and faster preparation of the project with Django, which is first connected to postgreSQL and then implemented on the docker.

# How this work?

first clone the project in your project file:

```
git clone https://github.com/alirezamhd/startdjango_with_postgresql_docker_customUser.git
```

- Make sure the docker is installed and running on your system

Then in the project directory run this command:

```
docker-compose up --build
```
## install new package

you can use code below for add new package:

```
docker-compose exec web pip install <yourPackage>
```

or for use manage.py:

```
docker-compose exec web python manage.py <yourCommand>
```

- note: Finally, add your installed packages to the requirements.txt

