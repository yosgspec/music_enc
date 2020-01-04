#module
#include "hspext.as"
#defcfunc cmd str command
	sdim v,4096
	sdim p,32000

	pipeexec p,"cmd /c \""+command+"\"",1
	if stat: mes "err"
	repeat
		pipeget v
		if stat=0: break
		wait 1
	loop
	return p
#global

#module
#defcfunc fileDialog
	dialog "wav;*.mp3;*,ogg;*.m4a",16,"音楽ファイル"
	if 0=stat: return ""
	return refstr
#global

*viewSelect
	objprm inputFile_id,fileDialog()
return
	
*musicConvert
	appCmd="ffmpeg -i \""+inputFile+"\" -y -vn -ac 2 -ar 44100 "
	mp3Cmd="-ab 256k -acodec libmp3lame -f mp3 \""+inputFile+".mp3\""
	aacCmd="-ab 128k -acodec aac -strict experimental -f mp4 \""+inputFile+".m4a\""
	oggCmd="-ab 128k -acodec libvorbis -f ogg \""+inputFile+".ogg\""
	wavCmd="-acodec pcm_s16le -f wav \""+inputFile+".wav\""

	sendmsg objinfo(mp3_id,2),$F0
	if stat: dialog cmd(appCmd+mp3Cmd): return
	sendmsg objinfo(aac_id,2),$F0
	if stat: dialog cmd(appCmd+aacCmd): return
	sendmsg objinfo(ogg_id,2),$F0
	if stat: dialog cmd(appCmd+oggCmd): return
	sendmsg objinfo(wav_id,2),$F0
	if stat: dialog cmd(appCmd+wavCmd): return
return
