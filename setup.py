#!/usr/bin/env python
# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import pathlib
import shutil
import sys

# 3rd party
from setuptools import setup

sys.path.append('.')

extras_require = {}

# stdlib
from textwrap import dedent

with open("wxIconSaver.desktop", 'w', encoding="UTF-8") as desktop:
	desktop.write(
			dedent(
					f"""\
[Desktop Entry]
Version=0.1.7
Name=wxIconSaver
Comment=wxPython GUI for saving icons to files.
Exec=wxIconSaver
Icon=document-save
Terminal=False
Type=Application
Categories=Utility;Application;
"""
					)
			)

repo_root = pathlib.Path(__file__).parent
install_requires = (repo_root / "requirements.txt").read_text(encoding="UTF-8").split('\n')

setup(
		data_files=[("share/applications", ["wxIconSaver.desktop"])],
		description="wxPython GUI for saving icons to files.",
		extras_require=extras_require,
		install_requires=install_requires,
		name="wxiconsaver",
		py_modules=[],
		)

shutil.rmtree("wxIconSaver.egg-info", ignore_errors=True)
