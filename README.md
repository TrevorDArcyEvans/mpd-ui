# (Yet Another) Raspberry Pi Music Player
A very simplistic, Raspberry Pi Zero based mp3 player featuring:
* [Music Player Daemon](https://www.musicpd.org/) + [Music Player Client](https://www.musicpd.org/clients/mpc/)
* randomised playlist
* only 3 buttons:
 * play/pause (toggles play/pause)
 * previous (like the song and want to hear it again)
 * next (hate the song and want to hear something else)
* LCD display showing current song

There are two scripts which are run on system start:
* MusicMonitor.py
 * polls buttons for what to do
* WhatsPlaying.py
 * scrolls current song across LCD display

Now if I coloured it white and called it something like, _iShuffle_, I could make a fortune...
