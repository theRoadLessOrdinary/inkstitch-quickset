# Ink/Stitch Quickset

Six one-click Inkscape extensions that set common [Ink/Stitch](https://inkstitch.org) settings on every selected object, without opening Ink/Stitch's Params dialog.

| Menu entry | Sets | Extension ID |
|---|---|---|
| **Ties: Before** | lock stitch at the start only | `maps_edge.inkstitch_ties_before` |
| **Ties: After** | lock stitch at the end only | `maps_edge.inkstitch_ties_after` |
| **Ties: Both** | lock stitches at start and end | `maps_edge.inkstitch_ties_both` |
| **Ties: Neither** | no lock stitches | `maps_edge.inkstitch_ties_neither` |
| **Trim After: True** | trim the thread after the object | `maps_edge.inkstitch_trim_after_true` |
| **Trim After: False** | no trim after the object | `maps_edge.inkstitch_trim_after_false` |

Menu: **Extensions > Map's Edge Tools > Embroidery > Stitch Settings**. They are also buttons on the [Map's Edge Tool Panel](https://github.com/theRoadLessOrdinary/maps-edge-panel), where the four Ties entries are labeled "Lock Stitches".

## Using them

Select the objects, then pick the entry. Each one writes a single Ink/Stitch attribute on each selected object: `inkstitch:ties` (Before = 1, After = 2, Both = 0, Neither = 3) or `inkstitch:trim_after` (True or False). These are the same values Ink/Stitch's own Params dialog writes. The attribute goes on the selected object itself; objects inside a selected group are not changed.

None of them has a dialog, so each can be bound to a key in **Edit > Preferences > Interface > Keyboard Shortcuts** (search for its name).

## Requirements

- Inkscape 1.x (developed and used on Inkscape 1.4.4, Flatpak, on Linux; other platforms have not been tried)
- Ink/Stitch installed, to stitch the results

## Install

Copy the files in this repository into a folder of their own inside Inkscape's user extensions directory, then restart Inkscape. To find that directory, open **Edit > Preferences > System** and look at **User extensions**. Typical locations:

| Install type | User extensions folder |
|---|---|
| Linux (native) | `~/.config/inkscape/extensions/` |
| Linux (Flatpak) | `~/.var/app/org.inkscape.Inkscape/config/inkscape/extensions/` |
| macOS | `~/Library/Application Support/org.inkscape.Inkscape/config/inkscape/extensions/` |
| Windows | `%APPDATA%\inkscape\extensions\` |

For example, on native Linux:

```bash
git clone https://github.com/theRoadLessOrdinary/inkstitch-quickset.git \
    ~/.config/inkscape/extensions/inkstitch-quickset
```

Keep `_base.py` in the same folder: every entry uses it.

To uninstall, delete the folder and restart Inkscape.
