#!/usr/bin/env python3
#
#  __init__.py
"""
wxPython GUI for saving icons to files.
"""
#
#  Copyright (c) 2019-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# generated by wxGlade 0.9.0 on Mon Feb 25 13:14:25 2019
#

__author__ = "Dominic Davis-Foster"
__copyright__ = "2019-2020 Dominic Davis-Foster"

__license__ = "GNU General Public License v3 or later (GPLv3+)"
__version__ = "0.1.7"
__email__ = "dominic@davis-foster.co.uk"

# stdlib
import enum
import os

# 3rd party
import wx  # type: ignore

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

wxWindowID = int

builtin_icons = [
		"ART_ADD_BOOKMARK",
		"ART_CDROM",
		"ART_CLOSE",
		"ART_COPY",
		"ART_CROSS_MARK",
		"ART_CUT",
		"ART_DELETE",
		"ART_DEL_BOOKMARK",
		"ART_ERROR",
		"ART_EXECUTABLE_FILE",
		"ART_FILE_OPEN",
		"ART_FILE_SAVE",
		"ART_FILE_SAVE_AS",
		"ART_FIND",
		"ART_FIND_AND_REPLACE",
		"ART_FLOPPY",
		"ART_FOLDER",
		"ART_FOLDER_OPEN",
		"ART_GOTO_FIRST",
		"ART_GOTO_LAST",
		"ART_GO_BACK",
		"ART_GO_DIR_UP",
		"ART_GO_DOWN",
		"ART_GO_FORWARD",
		"ART_GO_HOME",
		"ART_GO_TO_PARENT",
		"ART_GO_UP",
		"ART_HARDDISK",
		"ART_HELP",
		"ART_HELP_BOOK",
		"ART_HELP_FOLDER",
		"ART_HELP_PAGE",
		"ART_HELP_SETTINGS",
		"ART_HELP_SIDE_PANEL",
		"ART_INFORMATION",
		"ART_LIST_VIEW",
		"ART_MINUS",
		"ART_MISSING_IMAGE",
		"ART_NEW",
		"ART_NEW_DIR",
		"ART_NORMAL_FILE",
		"ART_PASTE",
		"ART_PLUS",
		"ART_PRINT",
		"ART_QUESTION",
		"ART_QUIT",
		"ART_REDO",
		"ART_REPORT_VIEW",
		"ART_TICK_MARK",
		"ART_TIP",
		"ART_UNDO",
		"ART_WARNING",
		]

artproviders = [
		"ART_TOOLBAR",
		"ART_MENU",
		"ART_BUTTON",
		"ART_FRAME_ICON",
		"ART_CMN_DIALOG",
		"ART_HELP_BROWSER",
		"ART_MESSAGE_BOX",
		"ART_OTHER",
		]


class FileTypesEnum(enum.Enum):
	"""
	An enumeration for supported filetypes
	"""

	# TODO: use autonumber enum for indices
	wildcard: str
	extension: str
	filetype_string: str
	ftype: int
	value: int

	BITMAP_TYPE_BMP = 1, 0, ".bmp", "BMP"
	BITMAP_TYPE_ICO = 3, 1, ".ico", "ICO"
	BITMAP_TYPE_CUR = 5, 2, ".cur", "CUR"
	BITMAP_TYPE_XBM = 7, 3, ".xbm", "XBM"
	BITMAP_TYPE_XBM_DATA = 8, 4, ".bmp", "XBM DATA"
	BITMAP_TYPE_XPM = 9, 5, ".xpm", "XBM"
	BITMAP_TYPE_XPM_DATA = 10, 6, ".xpm", "XPM DATA"
	BITMAP_TYPE_TIFF = 11, 7, ".tiff", "TIFF"
	BITMAP_TYPE_TIF = 11, 8, ".tiff", "TIFF"
	BITMAP_TYPE_GIF = 13, 9, ".gif", "GIF"
	BITMAP_TYPE_PNG = 15, 10, ".png", "PNG"
	BITMAP_TYPE_JPEG = 17, 11, ".jpg", "JPEG"
	BITMAP_TYPE_PNM = 19, 12, ".pnm", "PNM"
	BITMAP_TYPE_PCX = 21, 13, ".pcx", "PCX"
	BITMAP_TYPE_PICT = 23, 14, ".pict", "PICT"
	BITMAP_TYPE_ICON = 25, 15, ".ico", "ICON"
	BITMAP_TYPE_ANI = 27, 16, ".ani", "ANI"
	BITMAP_TYPE_IFF = 28, 17, ".iff", "IFF"
	BITMAP_TYPE_TGA = 29, 18, ".tga", "TGA"
	BITMAP_TYPE_MACCURSOR = 30, 19, ".*", "Mac Cursor"

	def __init__(self, *vals):
		pass

	def __new__(cls, ftype, index, extension, filetype_string):
		obj = object.__new__(cls)
		# index is canonical value
		obj._value_ = index
		obj.ftype = ftype
		obj.wildcard = f"{filetype_string} files (*{extension})|*{extension}"
		obj.extension = extension
		obj.filetype_string = filetype_string
		return obj

	def __int__(self):
		return self.ftype

	def __repr__(self):
		return f'<{self.__class__.__qualname__}.{self._name_}: {f"{self.value}, {self.wildcard}, ftype={self.ftype}"}>'


class BitmapSaverFrame(wx.Frame):

	def __init__(
			self,
			parent,
			id: wxWindowID = wx.ID_ANY,
			title: str = "",
			pos: wx.Point = wx.DefaultPosition,
			size: wx.Size = wx.DefaultSize,
			style: str = wx.DEFAULT_FRAME_STYLE,
			name: str = wx.FrameNameStr,
			):
		args = (parent, id)
		kwds = dict(
				title=title,
				pos=pos,
				size=size,
				style=style,
				name=name,
				)

		# begin wxGlade: BitmapSaverFrame.__init__
		kwds["style"] = kwds.get(
				"style", 0
				) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
		wx.Frame.__init__(self, *args, **kwds)
		self.SetSize((467, 577))
		self.SetMinSize((467, 577))
		self.SetMaxSize((467, 577))
		self.SetSize((467, 577))
		self.size_spin_ctrl = wx.SpinCtrl(self, wx.ID_ANY, "16", min=1, max=512)
		self.icon_list_box = wx.ListBox(self, wx.ID_ANY, choices=[""])
		self.provider_list_box = wx.ListBox(self, wx.ID_ANY, choices=[""])
		self.filetype_list_box = wx.ListBox(self, wx.ID_ANY, choices=[""])
		self.close_button = wx.Button(self, wx.ID_ANY, "Close")
		self.save_button = wx.Button(self, wx.ID_ANY, "Save")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_LISTBOX, self.update_preview, self.icon_list_box)
		self.Bind(wx.EVT_LISTBOX, self.update_preview, self.provider_list_box)
		self.Bind(wx.EVT_LISTBOX, self.update_preview, self.filetype_list_box)
		self.Bind(wx.EVT_BUTTON, self.on_close, self.close_button)
		self.Bind(wx.EVT_BUTTON, self.on_save, self.save_button)
		# end wxGlade

		self.Bind(wx.EVT_SPINCTRL, self.update_preview, self.size_spin_ctrl)
		self.size_spin_ctrl.SetValue("16")
		self.size_spin_ctrl.SetMin(1)
		self.size_spin_ctrl.SetMax(512)
		# style=wx.TE_NO_VSCROLL | wx.TE_PROCESS_ENTER)

		self.size: int = 16
		self.icon: bytes = b''
		self.provider: bytes = b''
		self.filetype: FileTypesEnum = FileTypesEnum(0)
		self.filename: str = ''

		self.icon_list_box.Clear()
		self.icon_list_box.AppendItems(builtin_icons)

		self.icon_list_box.SetSelection(0)
		self.provider_list_box.Clear()
		self.provider_list_box.AppendItems(artproviders)

		self.provider_list_box.SetSelection(0)
		self.filetype_list_box.Clear()
		self.filetype_list_box.AppendItems([member.name for member in FileTypesEnum])
		self.filetype_list_box.SetSelection(0)
		self.update_preview()

	def __set_properties(self) -> None:
		# begin wxGlade: BitmapSaverFrame.__set_properties
		self.SetTitle("wxIconSaver")
		# end wxGlade
		_icon = wx.NullIcon
		_icon.CopyFromBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_BUTTON, wx.Size(64, 64)))
		self.SetIcon(_icon)

	def __do_layout(self) -> None:
		# begin wxGlade: BitmapSaverFrame.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_4 = wx.BoxSizer(wx.VERTICAL)
		sizer_3 = wx.BoxSizer(wx.VERTICAL)
		size_sizer = wx.BoxSizer(wx.HORIZONTAL)
		size_label = wx.StaticText(self, wx.ID_ANY, "Size")
		size_sizer.Add(size_label, 0, wx.ALIGN_CENTER | wx.ALL, 10)
		size_sizer.Add(self.size_spin_ctrl, 0, wx.ALIGN_CENTER, 0)
		sizer_1.Add(size_sizer, 1, wx.EXPAND, 0)
		icon_label = wx.StaticText(self, wx.ID_ANY, "Icon")
		sizer_3.Add(icon_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
		sizer_3.Add(self.icon_list_box, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT, 10)
		provider_label = wx.StaticText(self, wx.ID_ANY, "Provider")
		sizer_3.Add(provider_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
		sizer_3.Add(self.provider_list_box, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT, 10)
		sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
		filetype_label = wx.StaticText(self, wx.ID_ANY, "Filetype")
		sizer_4.Add(filetype_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
		sizer_4.Add(self.filetype_list_box, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT, 10)
		preview_label = wx.StaticText(self, wx.ID_ANY, "Preview")
		sizer_4.Add(preview_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
		preview_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap)
		sizer_4.Add(preview_bitmap, 0, 0, 0)
		sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
		sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
		sizer_5.AddStretchSpacer()
		sizer_5.Add(self.close_button, 0, wx.ALIGN_CENTER | wx.LEFT, 100)
		sizer_5.Add(self.save_button, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 5)
		sizer_5.AddStretchSpacer()
		sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		self.Layout()
		# end wxGlade
		# sizer_5.AddStretchSpacer()
		self.preview_bitmap = preview_bitmap

	def on_close(self, _) -> None:  # wxGlade: BitmapSaverFrame.<event_handler>
		self.Close()

	def on_save(self, event: wx.Event) -> None:  # wxGlade: BitmapSaverFrame.<event_handler>
		self.update_preview(self, event)

		# from https://wxpython.org/Phoenix/docs/html/wx.FileDialog.html
		filedlg = wx.FileDialog(
				self,
				f"Save {self.filetype.filetype_string} file",
				wildcard=self.filetype.wildcard,
				style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
				)

		if filedlg.ShowModal() == wx.ID_CANCEL:
			return  # the user changed their mind

		# save the current contents in the file
		self.filename = filedlg.GetPath()

		if os.path.splitext(self.filename)[-1] != self.filetype.extension:
			self.filename = self.filename + self.filetype.extension

		wx.ArtProvider.GetBitmap(
				self.icon,
				self.provider,
				wx.Size(self.size, self.size),
				).SaveFile(self.filename, self.filetype.ftype)

		filedlg.Destroy()

		event.Skip()

	def update_preview(self, *_) -> None:  # wxGlade: BitmapSaverFrame.<event_handler>

		self.size = int(self.size_spin_ctrl.GetValue())
		self.icon = bytes(f"wx{self.icon_list_box.GetString(self.icon_list_box.GetSelection())}", "utf-8")
		self.provider = bytes(
				f"wx{self.provider_list_box.GetString(self.provider_list_box.GetSelection())}_C",
				"utf-8",
				)

		filetype_raw_index = self.filetype_list_box.GetSelection()

		self.filetype = FileTypesEnum(filetype_raw_index)

		self.preview_bitmap.SetBitmap(
				wx.ArtProvider.GetBitmap(self.icon, self.provider, wx.Size(self.size, self.size))
				)


# end of class BitmapSaverFrame