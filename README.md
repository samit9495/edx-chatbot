edx-chatbot
============

Course based chatbot handler for Open-edx Platform

Installation
------------

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/SkillUpTech/edx-chatbot.git#egg=edx-chatbot


Add ``edxchatbot`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'edxchatbot',
    )


Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load edxchatbot_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py lms migrate edxchatbot --settings=production 


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.
