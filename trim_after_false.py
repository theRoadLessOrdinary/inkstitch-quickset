#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _base import SetInkstitchAttr


class TrimAfterFalse(SetInkstitchAttr):
    attr_name = "trim_after"
    attr_value = "False"


if __name__ == "__main__":
    TrimAfterFalse().run()
