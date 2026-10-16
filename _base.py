"""
Shared base for the inkstitch-quickset extensions.

Each concrete extension sets exactly one Ink/Stitch namespaced attribute to
a fixed value on every selected element, with no dialog - meant to be run
via a keyboard shortcut for speed. Uses the fully-qualified Clark-notation
attribute name (not a bare "inkstitch:x" prefix), same reason documented in
rung_rail_satin.py: inkex doesn't know the "inkstitch" prefix and silently
writes the wrong namespace otherwise.
"""
import inkex

INKSTITCH_NS = "{http://inkstitch.org/namespace}"


class SetInkstitchAttr(inkex.EffectExtension):
    attr_name = None
    attr_value = None

    def effect(self):
        if self.attr_name is None:
            raise inkex.AbortExtension("attr_name not set - subclass bug.")

        sel = list(self.svg.selection)
        if not sel:
            raise inkex.AbortExtension("Nothing selected.")

        for node in sel:
            node.set(f"{INKSTITCH_NS}{self.attr_name}", self.attr_value)
