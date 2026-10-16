#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _base import SetInkstitchAttr


class TiesBoth(SetInkstitchAttr):
    attr_name = "ties"
    attr_value = "0"


if __name__ == "__main__":
    TiesBoth().run()
