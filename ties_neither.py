#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _base import SetInkstitchAttr


class TiesNeither(SetInkstitchAttr):
    attr_name = "ties"
    attr_value = "3"


if __name__ == "__main__":
    TiesNeither().run()
