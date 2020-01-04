using System;
using System.Collections.Generic;
using System.Linq;
using System.Diagnostics;
using System.Windows;
using Microsoft.Win32;

namespace music_enc{
	public partial class MainWindow: Window{
		public MainWindow(){
			InitializeComponent();
		}

		string cmd(string command){
			string stdout;
			var psi=new ProcessStartInfo("cmd");
			psi.Arguments=$"/c \"{command}\"";
			psi.UseShellExecute=false;
			psi.RedirectStandardError=true;
			psi.CreateNoWindow=true;
			using(var p=Process.Start(psi)){
				stdout=p.StandardError.ReadToEnd();
				p.WaitForExit();
			}
			return stdout;
		}

		void viewSelect(object sender,RoutedEventArgs e){
			var dialog=new OpenFileDialog();
			dialog.Filter="音楽ファイル|*.wav;*.mp3;*.m4a;*.ogg|全てのファイル|*.*";
			if(dialog.ShowDialog()==true) inputFile.Text=dialog.FileName;
		}

		void musicConvert(object sender,RoutedEventArgs e){
			var appCmd=$"ffmpeg -i \"{inputFile.Text}\" -y -vn -ac 2 -ar 44100 ";
			var mp3Cmd=$"-ab 256k -acodec libmp3lame -f mp3 \"{inputFile.Text}.mp3\"";
			var aacCmd=$"-ab 128k -acodec aac -strict experimental -f mp4 \"{inputFile.Text}.m4a\"";
			var oggCmd=$"-ab 128k -acodec libvorbis -f ogg \"{inputFile.Text}.ogg\"";
			var wavCmd=$"-acodec pcm_s16le -f wav \"{inputFile.Text}.wav\"";

			if(mp3_rdo.IsChecked==true) MessageBox.Show(cmd(appCmd+mp3Cmd));
			else if(aac_rdo.IsChecked==true) MessageBox.Show(cmd(appCmd+aacCmd));
			else if(ogg_rdo.IsChecked==true) MessageBox.Show(cmd(appCmd+oggCmd));
			else if(wav_rdo.IsChecked==true) MessageBox.Show(cmd(appCmd+wavCmd));
		}
	}
}
