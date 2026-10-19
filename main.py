import Recorder, Lookup

while True:
    Recorded_word = Recorder.GetWord()

    if Recorded_word:
        Translated_Word = Lookup.Lookup(Recorded_word)
        print(Translated_Word)
