# audio_cloze
Anki addon that changes the behavior of audio inside clozes to be consistent with that
of purely textual clozes.

With this addon:
Inactive clozes do not make any sound.  If an audio hint is desired for a cloze, 
place the audio in the hint for that cloze. Multiple sounds and text can be added to the 
answer or the hint.

With this addon inactive clozes do not make any sound. If an audio hint is desired 
for a cloze, place the audio in the hint for that cloze. Multiple sounds can be added 
to the answer or the hint.

The result is absolute control over the sounds played by any card generated from a multi 
cloze note.

This addon works very well in combination with Awesome TTS.

Note:  Anyone using a card deck that uses sound within clozes as this example will not get
an audio hint for each cloze.

    {{c1::Ens estan construint un edifici de vuit pisos[sound:catalan_020_S06.mp3]}} 
    {{c2::i de vista ja no en queda [sound:catalan_020_S07.mp3]}}!

For this card to behave as previously, It would need to be written like this.

    {{c1::Ens estan construint un edifici de vuit pisos[sound:catalan_020_S06.mp3]::[sound:catalan_020_S07.mp3]}} 
    {{c2::i de vista ja no en queda [sound:catalan_020_S07.mp3]::[sound:catalan_020_s06.mp3]}}!

