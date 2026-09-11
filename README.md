# Abyss — an Omarchy theme

Blue-black depths, cool blue selections, antique gold focus.

Dark enough for a room with the lights off, but not flat: the background sits at
`#06090b` while panels and popups step up through `#0B1219` and `#101C26`, so the
UI keeps its depth without any borders shouting. Everything that has focus —
cursor, active tab, active border, progress — is antique gold `#C2A46D`.
Selections are a cold blue `#25445B`, so "what is selected" and "what is focused"
never look like the same thing.

## Install

```bash
omarchy theme install https://github.com/yohan-correia/omarchy-abyss-theme.git
omarchy theme set abyss
```

The repo name matters: Omarchy strips `omarchy-` and `-theme`, so this installs
as the theme `abyss`.

## What's in it

| File | What it colors |
|---|---|
| `colors.toml` | Terminal palette, Hyprland borders, base 16 colors |
| `shell.toml` | Omarchy shell — bar, menu, launcher, controls |
| `vscode.json` | Points VS Code at the `Abyss` extension |
| `backgrounds/` | Four wallpapers |

### Palette

| Role | Hex |
|---|---|
| Background | `#06090b` |
| Panels | `#0B1219` |
| Raised surfaces | `#101C26` |
| Foreground | `#D8DFE5` |
| Focus / accent (gold) | `#C2A46D` |
| Selection (blue) | `#25445B` |
| Borders | `#253643` |

## VS Code

The Omarchy theme sets `vscode.json` to select the `Abyss` extension, which is
not on the Marketplace. Install it from the bundled build:

```bash
code --install-extension vscode/abyss-theme-1.0.0.vsix
```

Then pick **Abyss** under Color Theme. To rebuild it after editing
`colors.toml`, run `python vscode/build.py` — the builder reads the palette from
the theme's own `colors.toml`, so the editor and the terminal never drift apart.

## Wallpapers

The four backgrounds are AI-generated, and are released under the same license
as the rest of the repo.

## Not included

This theme covers the terminal, Hyprland, the Omarchy shell and VS Code. It does
not ship `neovim.lua`, `icons.theme`, `preview.png` or `unlock.png` — Omarchy
falls back to its defaults for those. Pull requests welcome.

## License

MIT — see [LICENSE](LICENSE).
