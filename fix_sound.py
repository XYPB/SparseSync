import os
from glob import glob
import subprocess
from utils.utils import which_ffmpeg

def attach_audio_to_video(origin_path, wav_path, dest):
    cmd = f'{which_ffmpeg()} -i {origin_path} -i {wav_path} -hide_banner -loglevel panic -map 0:v -map 1:a -c:v copy -shortest -y {dest}'
    subprocess.call(cmd.split())
    return

if __name__ == '__main__':
    audios = glob('./tmp/*.wav')
    audios_name = [a.split('/')[-1].replace('.wav', '') for a in audios]
    for i in range(3):
        videos = glob(f'logs/CondAVTransformer_VNet_randshift_2s_GH_vqgan_no_earlystop_multiple/2sec_full_generated_video_{i}_wr/*.mp4')
        for v in videos:
            assert v.split('/')[-1].replace('.mp4', '') in audios_name
            a = os.path.join('tmp', v.split('/')[-1].replace('.mp4', '.wav'))
            assert os.path.exists(a)
            os.makedirs(f'logs/CondAVTransformer_VNet_randshift_2s_GH_vqgan_no_earlystop_multiple/2sec_full_generated_video_{i}', exist_ok=True)
            dest = os.path.join(f'logs/CondAVTransformer_VNet_randshift_2s_GH_vqgan_no_earlystop_multiple/2sec_full_generated_video_{i}', v.split('/')[-1])
            # print(v, a, dest)
            # exit()
            attach_audio_to_video(v, a, dest)

