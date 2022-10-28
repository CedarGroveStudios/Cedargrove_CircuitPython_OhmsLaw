Introduction
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/CedarGroveStudios/CircuitPython_OhmsLaw/workflows/Build%20CI/badge.svg
    :target: https://github.com/CedarGroveStudios/CircuitPython_OhmsLaw/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A CircuitPython helper for calculating an Ohm's Law formula result from two input parameters.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install cedargrove_ohmslaw

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    >>> from cedargrove_ohmslaw import ohms_law
    >>> ohms_law(ohms=1000, volts=3.3)
    3.3  # current in milliamperes
    >>> ohms_law(volts=5, milliamperes=100)
    50.0  # resistance in ohms
    >>> ohms_law(milliamperes=5, ohms=2000)
    10.0  # voltage in volts


Documentation
=============
API documentation for this library can be found `here <https://github.com/CedarGroveStudios/Cedargrove_CircuitPython_OhmsLaw/blob/main/media/pseudo_rtd_cedargrove_ohmslaw.pdf>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/CedarGroveStudios/CircuitPython_OhmsLaw/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
