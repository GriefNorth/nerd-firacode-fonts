# Packaging template: basic single-family fonts packaging.
#
# SPDX-License-Identifier: MIT
#
# This template documents the minimal set of spec declarations, necessary to
# package a single font family, from a single dedicated source archive.
#
# It is part of the following set of packaging templates:
# “fonts-0-simple”: basic single-family fonts packaging
# “fonts-1-full”:   less common patterns for single-family fonts packaging
# “fonts-2-multi”:  multi-family fonts packaging
# “fonts-3-sub”:    packaging fonts, released as part of something else
#
# A font family is composed of font files, that share a single design, and
# differ ONLY in:
# — Weight        Bold, Black…
# – Width∕Stretch Narrow, Condensed, Expanded…
# — Slope/Slant   Italic, Oblique
# Optical sizing  Caption…
#
# Those parameters correspond to the default axes of OpenType variable fonts:
# https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg#registered-axis-tags
# The variable fonts model is an extension of the WWS model described in the
# WPF Font Selection Model whitepaper (2007):
# https://msdnshared.blob.core.windows.net/media/MSDNBlogsFS/prod.evol.blogs.msdn.com/CommunityServer.Components.PostAttachments/00/02/24/90/36/WPF%20Font%20Selection%20Model.pdf
#
# Do not rely on the naming upstream chose, to define family boundaries, it
# will often be wrong.
#
# Declaration order is chosen to limit divergence between those templates, and
# simplify cut and pasting.
#
Version:        3.2.1
Release:        1%{?dist}
URL:            https://github.com/ryanoasis/nerd-fonts

# The identifier of the entity, that released the font family.
%global foundry           Nerd Fonts
# The font family license identifier. Adjust as necessary. The OFL is our
# recommended font license.
%global fontlicense       OFL
#
# The following directives are lists of space-separated shell globs
#   – matching files associated with the font family,
#   – as they exist in the build root,
#   — at the end of the %build stage:
# – legal files (licensing…)
%global fontlicenses      LICENSE
# – documentation files
#%%global fontdocs          *.txt
# – exclusions from the ”fontdocs” list
%global fontdocsex        %{fontlicenses}

# The human-friendly font family name, whitespace included, restricted to the
# the Basic Latin Unicode block.
%global fontfamily        FiraCode Nerd Font
%global fontsummary       Free monospaced font with programming ligatures
#
# More shell glob lists:
# – font family files
%global fonts             *.ttf
# – fontconfig files
%global fontconfs         %{SOURCE10}
#
# A multi-line description block for the generated package.
%global fontdescription   %{expand:
Fira Code is a free monospaced font containing ligatures for common programming
multi-character combinations. This is just a font rendering feature: underlying
code remains ASCII-compatible. This helps to read and understand code faster.
}

Source0:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/FiraCode.zip
# Adjust as necessary. Keeping the filename in sync with the package name is a good idea.
# See the fontconfig templates in fonts-rpm-templates for information on how to
# write good fontconfig files and choose the correct priority [number].
Source10:       60-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -c
%{__rm} -vfr ./*Windows*.ttf

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sat May 11 2024 GriefNorth <grief.north@gmail.com> - 3.2.1-1
- Bump version 3.2.1
* Sat Apr 19 2023 Astrawan Wayan <astrawan@icloud.com> - 2.3.3-1
- Bump version 2.3.3
* Sun Nov 13 2022 Astrawan Wayan <astrawan@icloud.com> - 2.2.2-1
- Initial package
