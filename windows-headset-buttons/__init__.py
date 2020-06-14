# windows-headset-buttons
# Copyright (C) 2019 jack01. Released under the MIT License (see LICENSE for details).

import sounddevice, struct, win32api, signal, threading

VK_MEDIA_NEXT_TRACK = 0xB0;
VK_MEDIA_PLAY_PAUSE = 0xB3;
VK_MEDIA_PREV_TRACK = 0xB1;

sample_rate = 1024
stream_block_size = 64
press_amplitude_threshold = -10000
press_duration_threshold = 0.1875
multi_press_interval = 0.375

press_duration_blocks = sample_rate / stream_block_size * press_duration_threshold
multi_press_blocks = sample_rate / stream_block_size * multi_press_interval

class Sampler:
    def __init__(self):
        self.stream = sounddevice.RawInputStream(
            samplerate=sample_rate,
            blocksize=stream_block_size,
            channels=1,
            callback=self.stream_callback,
            dtype='int16'
        )
        self.stream.start()
        self.press_timer = 0
        self.multi_press_timer = 0
        self.press_count = 0
        self.triggered = False

    def stream_callback(self, indata, frames, time, status):
        peak = min([x[0] for x in struct.iter_unpack('h', indata)])

        if self.multi_press_timer > 0 and self.multi_press_timer < multi_press_blocks:
            self.multi_press_timer += 1
        elif self.multi_press_timer >= multi_press_blocks:
            self.pressed(self.press_count)
            self.multi_press_timer = 0
            self.press_count = 0

        if peak < press_amplitude_threshold and self.press_timer == 0:
            self.press_timer += 1
            self.press_count += 1
            self.multi_press_timer = 1
        elif self.press_timer > 0 and self.press_timer < press_duration_blocks:
            self.press_timer += 1
        else:
            self.press_timer = 0

    def pressed(self, count):
        print(count)
        if count == 2:
            win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, 0, 0)
        elif count == 3:
            win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, 0, 0)

def main():
    sampler = Sampler()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    threading.Event().wait()

if __name__ == '__main__':
    main()
