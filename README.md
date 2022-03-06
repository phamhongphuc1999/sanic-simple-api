<h1 align="center">
  :sparkles::sparkles::sparkles:SANIC SIMPLE API:sparkles::sparkles::sparkles:
</h1>
<p align="center">
    :fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire:
</p>

## What’s In This Document

---
- [Quickstart](#quickstart)

---
## :rocket: Quickstart <a name="quickstart"></a>
Project provide two mode environments is development and production, the development environment used when development process and the production environment used to deployed in server
You can run the project on your local environment with these steps:
1. **Setup python virtual environment and install libraries**
- *To create virtual environment, run command:*

    ```shell
    python3 -m venv venv
    ```
    Or you can use Add Interpreter in PyCharm

- *Activity virtual environment in ubuntu:*
    ```shell
    source venv/bin/activate
    ```
- *Install libraries*
    ```shell
    pip3 install -r requirements/production.txt
    ```

2. **Start Trava API in `development` mode** <br />
    To start API with development environment, simply you run

    ```shell
    make rundev
    ```
   
    If you want to run project in production, you run following:
    
    ```shell
    make runpro
    ```
- to get more information, you can run:
    ```shell
    make help
    ```
