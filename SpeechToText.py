import speech_recognition as sr
import pyaudio
import sys
# talkSpeechToText() function gets our voice by using computer microphone and
# it returns what we are saying to computer as a string
def talkSpeechToText():
    r=sr.Recognizer()

    pa = pyaudio.PyAudio()
    x = pa.get_default_input_device_info()
    xx = x['index']  # Json objesi dönüyor...

    with sr.Microphone(xx) as source:


        print("Say Something")
        r.adjust_for_ambient_noise(source,xx)
        audio=r.listen(source)
        '''r.energy_threshold = 500 '''
        '''Increasing the energy_threshold seemed to resolve this issue for me.
         It appears that under quiet conditions, my microphone returns an energy
          level of 300~ forcing the recorder to record indefinitely.'''
        print("will ask google")
        try:
            text = r.recognize_google(audio, language="tr-TR")
            print("Google thinks you said: \n"+text)
            return text
        except sr.UnknownValueError as e:
            e = sys.exc_info()[0]
            print(e)
            print("hata yakaladım")
        except:
            print('default olanh exceptte yakaladım')
