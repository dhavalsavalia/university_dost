Install
=========

We are using Docker for both production and production.

.. note::  I highly recommand you to develop project on Linux machine. Ubuntu advised.
.. warning::  DO NOT USE WINDOWS. It sucks.


Pipenv Setup
-------------

Pipenv is must have packaging tool for any Python developer. It automatically generates virtual machines, create Pipfile and Pipfile.lock

Installation for pip
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash
   :linenos:

   $ pip install pipenv

Ubuntu
^^^^^^^

.. code-block:: bash
   :linenos:

   $ sudo apt install software-properties-common python-software-properties
   $ sudo add-apt-repository ppa:pypa/ppa
   $ sudo apt update
   $ sudo apt install pipenv


MacOS using brew
^^^^^^^^^^^^^^^^^

.. code-block:: bash
   :linenos:

   $ brew install pipenv


After installing pipenv go to your prefered project directory create pipenv

.. code-block:: bash
   :linenos:

   $ pipenv shell

pipenv will do all the heavylifting for you and automatically activate virtulenv for you.


Git Setup
----------

While you are in pipenv directory where Pipfile and Pipfile.lock files are clone our GitHub repository

.. code-block:: bash
   :linenos:

   $ git clone https://github.com/dhavalsavalia/university_dost.git

.. note::  It might ask you for your credentials. Enter your name, email and password and you are good to go.








Docker Setup
-------------

Follow the instructions to install the `Docker Engine <https://docs.docker.com/engine/installation/>`_ and the required Docker components - Engine, Machine, and Compose.

Installations for Mac and Ubuntu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* MacOS: `<https://docs.docker.com/docker-for-mac/install/>`_
* Ubuntu: `<https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_

Check the versions:

.. code-block:: bash
   :linenos:

   $ docker --version
   Docker version 18.03.1-ce, build 9ee9f40

   $ docker-compose --version
   docker-compose version 1.21.1, build 5a3f1a3

   $ docker-machine --version
   docker-machine version 0.14.0, build 89b8332


Docker Compose
^^^^^^^^^^^^^^^

Now we can fire everything up - e.g., Django and Postgres - via Docker Compose:

.. code-block:: bash
   :linenos:

    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml upeval