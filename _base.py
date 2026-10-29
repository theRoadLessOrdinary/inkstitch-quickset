"""
Shared base for the inkstitch-quickset extensions.

Each concrete extension sets exactly one Ink/Stitch namespaced attribute to
a fixed value on every selected element, with no dialog - meant to be run
via a keyboard shortcut for speed. When a group (or layer) is selected, the
value goes on every shape inside it, at any depth, instead of on the group.
Uses the fully-qualified Clark-notation attribute name (not a bare
"inkstitch:x" prefix), same reason documented in rung_rail_satin.py: inkex
doesn't know the "inkstitch" prefix and silently writes the wrong namespace
otherwise.
"""
import inkex

INKSTITCH_NS = "{http://inkstitch.org/namespace}"

# Shapes Ink/Stitch can stitch. Clones (svg:use) are set only when selected
# directly, since a clone inside a group stitches with its source's settings.
SHAPE_TYPES = (
    inkex.PathElement,
    inkex.Rectangle,
    inkex.Circle,
    inkex.Ellipse,
    inkex.Line,
    inkex.Polyline,
    inkex.Polygon,
)

# Group contents that are never stitched directly.
SKIP_TYPES = (inkex.Defs, inkex.ClipPath, inkex.Mask)


def targets(node):
    """The node itself, or every shape inside it if it is a group."""
    if not isinstance(node, inkex.Group):
        return [node]
    found = []
    for child in node:
        if isinstance(child, SKIP_TYPES):
            continue
        if isinstance(child, inkex.Group):
            found.extend(targets(child))
        elif isinstance(child, SHAPE_TYPES):
            found.append(child)
    return found


class SetInkstitchAttr(inkex.EffectExtension):
    attr_name = None
    attr_value = None

    def effect(self):
        if self.attr_name is None:
            raise inkex.AbortExtension("attr_name not set - subclass bug.")

        sel = list(self.svg.selection)
        if not sel:
            raise inkex.AbortExtension("Nothing selected.")

        done = set()
        for node in sel:
            for target in targets(node):
                if target in done:
                    continue
                done.add(target)
                target.set(f"{INKSTITCH_NS}{self.attr_name}", self.attr_value)
