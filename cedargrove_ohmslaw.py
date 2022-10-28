# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: MIT
"""
`cedargrove_ohmslaw`
================================================================================

A CircuitPython helper for calculating an Ohm's Law formula result from two
input parameters.

* Author(s): JG

Implementation Notes
--------------------
**Hardware:**

**Software and Dependencies:**
* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/CedarGroveStudios/CircuitPython_OhmsLaw.git"


def ohms_law(ohms=None, milliamperes=None, volts=None):
    """Ohm's Law calculator helper. When two numeric values are supplied (or two
    numeric values and a third = None value), the two numeric values are used
    to calculate and return the missing value."""

    if (ohms, milliamperes, volts).count(None) > 1:
        raise ValueError("At least two values must be provided.")

    # Calculate resistance in Ohms
    if ohms == None:
        return volts / (milliamperes / 1000.0)

    # Calculate current in milliamperes (mA)
    if milliamperes == None:
        return (volts / ohms) * 1000.0

    # Calculate voltage in volts
    if volts == None:
        return ohms * (milliamperes / 1000.0)

    raise ValueError("Too many values. Only two are needed.")
