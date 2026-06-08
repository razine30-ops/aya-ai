from kivy.app import App
from kivy.uix.label import Label

class AyaAiApp(App):
    def build(self):
        return Label(text='مرحبا! Aya AI معاك. مرحبا بك.')

if __name__ == '__main__':
    AyaAiApp().run()
