# window.py
#
# Copyright 2023 francisco
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk
from .define import RES_PATH
from .components import ShortcutsWindow, ThemeSelector

@Gtk.Template(resource_path=f'{RES_PATH}/window.ui')
class CalculatorWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'CalculatorWindow'

    main_menu = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._setup();

    def _setup(self):
        self.main_menu.props.popover.add_child(ThemeSelector(), 'theme')
        self.set_help_overlay(ShortcutsWindow())
