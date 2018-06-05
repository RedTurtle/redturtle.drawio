.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=================
Redturtle draw.io
=================

.. image:: https://travis-ci.org/RedTurtle/redturtle.drawio.svg?branch=master
   :target: https://travis-ci.org/RedTurtle/redturtle.drawio


A simple integration with draw.io

Features
--------

Allows to embed draw.io iframes in a special content-type


Usage
-----

There is a new available conten-type where you can insert the iframe embed
code generated from a draw.io project.

We use iframe because we encountered some problems with other export formats:

- svg and images doesn't support zoom
- html uses an external js resource that is incompatible with Plone5 requirejs structure


Translations
------------

This product has been translated into

- Italian


Installation
------------

Install redturtle.drawio by adding it to your buildout::

    [buildout]

    ...

    eggs =
        redturtle.drawio


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/RedTurtle/redturtle.drawio/issues
- Source Code: https://github.com/RedTurtle/redturtle.drawio

Credits
=======

Developed with the support of:

* `Azienda USL Ferrara`__

  .. image:: http://www.ausl.fe.it/logo_ausl.gif
     :alt: Azienda USL's logo

* `S. Anna Hospital, Ferrara`__

  .. image:: http://www.ospfe.it/ospfe-logo.jpg
     :alt: S. Anna Hospital logo


All of them supports the `PloneGov initiative`__.

__ http://www.ausl.fe.it/
__ http://www.ospfe.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/


License
-------

The project is licensed under the GPLv2.
