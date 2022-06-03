import asyncio
from ffmpeg import FFmpeg

#ffmpeg -hwaccel cuda -i %%i -c:v h264_nvenc -pix_fmt yuv420p -preset slow 
#-rc constqp/cbr/vbr -b:v 8M -maxrate:v 10M -c:a aac -b:a 224k 

ffmpeg = (FFmpeg()
            .option('y')
            .input('input.mp4')
             # Use a dictionary when an option name contains special characters
            .output('output.mp4',
                    {'c:v': 'h264',
                    'c:a': 'aac',
                    'b:a': '224k'},
                    pix_fmt='yuv420p',                                     
                    preset='slow',
                    #rc='constqp/cbr/vbr',
                    b='8M',
                    maxrate='10M',
                    )           
        )


@ffmpeg.on('start')
def on_start(arguments):
    print('arguments:', arguments)


@ffmpeg.on('stderr')
def on_stderr(line):
    print('stderr:', line)


@ffmpeg.on('progress')
def on_progress(progress):
    print(progress)


@ffmpeg.on('completed')
def on_completed():
    print('completed')


@ffmpeg.on('terminated')
def on_terminated():
    print('terminated')


@ffmpeg.on('error')
def on_error(code):
    print('error:', code)


asyncio.run(ffmpeg.execute())