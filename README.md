# Web Tech VK
> An educational project within the course on [_stepik.org_](https://stepik.org/154).

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- The project is a service for answering questions. The user of the service has the opportunity to register, ask a question, answer questions from other users. The user can also mark questions with the help of the "like" button, changing their rating

- The goal of the project is to gain practical skills in web backend development

- Since outdated versions are used for some of the technologies, the development of the project imitates work with legacy code well

## Technologies Used
- Python - version 3.4
- Django - version 2.0
- Gunicorn - version 20.1
- Nginx - version 1.14

## Setup
First of all you need to install some packages
```
sudo apt-get update
sudo apt-get install nginx
sudo apt-get install python3-venv
sudo apt-get install supervisor
```
Then you need to `git clone` the repository **_exacly_** in a directory `/home/box/web`
```
sudo git clone https://github.com/iBikkulov/web-tech-vk.git /home/box/web
```
The project has the following directory layout

    .
    ├── ask/                        # Django project
    │   ├── ask/                    # Project settings
    │   ├── gunicorn_start.sh       # Application-server utility
    │   ├── manage.py               # Django cmdline utility
    │   ├── qa/                     # Django application
    │   └── requirements.txt
    ├── conf/                       # Configuration files and scripts
    │   ├── ask_app/
    │   │   ├── supervisor.conf
    │   │   └── supervisor_start.sh
    │   └── nginx/
    │       ├── nginx.conf
    │       └── nginx_start.sh
    ├── public/                     # Static files
    ├── uploads/                    # Upload files
    ├── README.md
    └── init.sh                     # Startup utility

Next you need to create a virtual environment for the application and download all requirements
```
cd /home/box/web/ask
python3 -m venv ask_env
source ask_env/bin/activate
pip install -r requirements.txt
```
**_Note:_** It's recommended to name a virtual environment directory according to the following convention: `<appname>_env` 

Now it's all set! To start applications run `init.sh`
```
cd /home/box/web
sudo ./init.sh
```

## TODO
- Automate migrations (on start)
- Add troubleshoot with supervisord

## Acknowledgements
- This project was based on [this course](https://stepik.org/154).

## Contact
Created by [@iBikkulov](https://www.linkedin.com/in/ilya-bikkulov-251306234/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
