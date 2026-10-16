#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _base import SetInkstitchAttr


class TrimAfterTrue(SetInkstitchAttr):
    attr_name = "trim_after"
    attr_value = "True"


if __name__ == "__main__":
    TrimAfterTrue().run()
