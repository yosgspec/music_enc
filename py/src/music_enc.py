import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from os.path import abspath,dirname
import subprocess

def cmd(command):
	with subprocess.Popen(command,
			shell=True,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			stdin=subprocess.DEVNULL) as p:
		return p.communicate()[1]

class MusicEnc:
	def __init__(self,win):
		self.win=win

	def viewSelect(self,e):
		self.win.inputFile.set(askopenfilename(
			filetypes=[
				("音楽ファイル","*.wav;*.mp3;*.m4a;*.ogg"),
				("全てのファイル","*")]))
		
	def musicConvert(self,e):
		inputFile_get=self.win.inputFile.get()
		rdo=self.win.rdo.get()
		rdoId=self.win.rdoId

		appCmd=f"ffmpeg -i \"{inputFile_get}\" -y -vn -ac 2 -ar 44100 "
		mp3Cmd=f"-ab 256k -acodec libmp3lame -f mp3 \"{inputFile_get}.mp3\""
		aacCmd=f"-ab 128k -acodec aac -strict experimental -f mp4 \"{inputFile_get}.m4a\""
		oggCmd=f"-ab 128k -acodec libvorbis -f ogg \"{inputFile_get}.ogg\""
		wavCmd=f"-acodec pcm_s16le -f wav \"{inputFile_get}.wav\""

		if rdo==0: showinfo("",cmd(appCmd+mp3Cmd))
		elif rdo==1: showinfo("",cmd(appCmd+aacCmd))
		elif rdo==2: showinfo("",cmd(appCmd+oggCmd))
		elif rdo==3: showinfo("",cmd(appCmd+wavCmd))
		else : showinfo("",str(rdo))
