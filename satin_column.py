#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _base import SetInkstitchAttr


class SatinColumn(SetInkstitchAttr):
    attr_name = "satin_column"
    attr_value = "True"


if __name__ == "__main__":
    SatinColumn().run()
