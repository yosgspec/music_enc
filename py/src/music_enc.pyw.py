import tkinter as tk
import copy
from enum import IntEnum
import music_enc
from tkinter.scrolledtext import ScrolledText

class MainWindow(tk.Frame):
	def __init__(self,root):
		event=music_enc.MusicEnc(self)

		style={
			"bg":{"background":"#3399FF"}
		}
		btnStyle={
			"foreground":"#000099",
			"background":"#AACCFF",
			"font":("Meiryo UI",11),
		}
		rdoStyle=copy.copy(btnStyle)
		rdoStyle["background"]="#3399FF"

		root.title("音楽ファイル変換")
		root.geometry("260x110")
		root.resizable(0,0)
		root.option_add("*font",("Meiryo UI",16))
		root.config(bg=style["bg"]["background"])

		super().__init__(root,cnf=style["bg"])
		self.pack(pady=10)

		selectFile=tk.Frame(self,cnf=style["bg"])

		self.inputFile=tk.StringVar()
		inputFile=tk.Entry(selectFile,
			textvariable=self.inputFile,
			font=("Meiryo UI",11),
			width=20)
		inputFile.pack(side="left",fill="both")

		viewSelect=tk.Button(selectFile,
			cnf=btnStyle,
			text="参照",
			width=5)
		viewSelect.pack(side="left",fill="x")
		viewSelect.bind("<ButtonRelease>",event.viewSelect)

		selectFile.pack(padx=10,anchor="w",fill="x")

		self.rdoId={
			"mp3":0,
			"aac":1,
			"ogg":2,
			"wav":3
		}

		rdo=tk.Frame(self,cnf=style["bg"])
		self.rdo=tk.IntVar()
		self.rdo.set(self.rdoId["mp3"])

		mp3_rdo=tk.Radiobutton(rdo,
			cnf=rdoStyle,
			variable=self.rdo,
			text="MP3",
			value=self.rdoId["mp3"])
		mp3_rdo.pack(side="left")
		aac_rdo=tk.Radiobutton(rdo,
			cnf=rdoStyle,
			variable=self.rdo,
			text="AAC",
			value=self.rdoId["aac"])
		aac_rdo.pack(side="left")
		ogg_rdo=tk.Radiobutton(rdo,
			cnf=rdoStyle,
			variable=self.rdo,
			text="OGG",
			value=self.rdoId["ogg"])
		ogg_rdo.pack(side="left")
		wav_rdo=tk.Radiobutton(rdo,
			cnf=rdoStyle,
			variable=self.rdo,
			text="WAV",
			value=self.rdoId["wav"])
		wav_rdo.pack(side="left")

		rdo.pack(padx=10,anchor="w")

		musicConvert=tk.Button(self,
			cnf=btnStyle,
			text="変換")
		musicConvert.pack(padx=10,anchor="w",fill="x")
		musicConvert.bind("<ButtonRelease>",event.musicConvert)

MainWindow(root=tk.Tk()).mainloop()
