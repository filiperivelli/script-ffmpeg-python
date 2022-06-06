import asyncio
from ffmpeg import FFmpeg
import os

#ffmpeg -hwaccel cuda -i %%i -c:v h264_nvenc -pix_fmt yuv420p -preset slow 
#-rc constqp/cbr/vbr -b:v 8M -maxrate:v 10M -c:a aac -b:a 224k 
class FFmpegH265ToH264:     
    def __init__(self,file:str):
        self.input_file = file
        self.output_file = self._getOutputFile()
        self.ffmpeg = (FFmpeg()
                    .option('y')
                    .input(self.input_file, hwaccel='cuda')
                    # Use a dictionary when an option name contains special characters
                    .output(self.output_file,
                            {'c:v': 'h264_nvenc',
                            'c:a': 'aac',
                            'b:a': '224k',
                            'b:v':'8M',
                            'maxrate:v':'10M'},                           
                            pix_fmt='yuv420p',                                     
                            preset='slow',
                            rc='constqp/cbr/vbr'
                            )           
                )

        @self.ffmpeg.on('start')
        def on_start(arguments):
            print('arguments:', arguments)


        @self.ffmpeg.on('stderr')
        def on_stderr(line):
            print('stderr:', line)


        @self.ffmpeg.on('progress')
        def on_progress(progress):
            print(progress)


        @self.ffmpeg.on('completed')
        def on_completed():
            print('completed')


        @self.ffmpeg.on('terminated')
        def on_terminated():
            print('terminated')


        @self.ffmpeg.on('error')
        def on_error(code):
            print('error:', code)

    def _getOutputFile(self):
        output_name = os.path.basename(self.input_file).replace('265','264')
        output_name = os.path.join(os.path.dirname(self.input_file),output_name)
        return output_name

    def run(self):
        asyncio.run(self.ffmpeg.execute())