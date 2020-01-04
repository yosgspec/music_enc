"use strict";

const {exec}=require("child_process");

const cmd=command=>new Promise(resolve=>
	exec(command,(err,stdout,stderr)=>resolve(stderr)));

const mp3_rdo=document.getElementById("mp3_rdo");
const aac_rdo=document.getElementById("aac_rdo");
const ogg_rdo=document.getElementById("ogg_rdo");
const wav_rdo=document.getElementById("wav_rdo");

function myAlert(msg){
	nw.Window.open("./myAlert.html",{
		title:"",
		width:480,
		height:480,
		position:"center",
		focus:true
	},win=>{
		win.once("loaded",()=>
			win.window.document.body.innerText=msg)
	});
}

async function musicConvert(){
	var appCmd=`ffmpeg -i "${inputFile.value}" -y -vn -ac 2 -ar 44100 `;
	var mp3Cmd=`-ab 256k -acodec libmp3lame -f mp3 "${inputFile.value}.mp3"`;
	var aacCmd=`-ab 128k -acodec aac -strict experimental -f mp4 "${inputFile.value}.m4a"`;
	var oggCmd=`-ab 128k -acodec libvorbis -f ogg "${inputFile.value}.ogg"`;
	var wavCmd=`-acodec pcm_s16le -f wav "${inputFile.value}.wav"`;

	if(mp3_rdo.checked) myAlert(await cmd(appCmd+mp3Cmd));
	else if(aac_rdo.checked) myAlert(await cmd(appCmd+aacCmd));
	else if(ogg_rdo.checked) myAlert(await cmd(appCmd+oggCmd));
	else if(wav_rdo.checked) myAlert(await cmd(appCmd+wavCmd));
}
