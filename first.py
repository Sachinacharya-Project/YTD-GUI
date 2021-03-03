from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from py_pack.music_downloader import download
Window.clearcolor = (34/255, 34/255, 34/244, 1)
Window.size = (550, 290)
Builder.load_file('kv/widgets.kv')
class MyLayout(Widget):
    def downloader(self):
        itemTopic = self.ids.url
        topic = itemTopic.text
        localType = self.ids.type
        npt = localType.text
        btn = self.ids.btn
        ctx = ''
        if str(npt).lower() == 'a' or 'audio' in str(npt).lower():
            ctx = 'audio'
        elif str(npt).lower() == 'v' or 'video' in str(npt).lower():
            ctx = 'video'
        else:
            localType.text = "Error: USE 'A' or 'V' (def. V)"
            ctx = 'video'
        btn.text = 'Downloading'
        x = download(topic, ctx)
        if x == True:
            btn.text = 'Download'
        localType.text = ''
        itemTopic.text = ''
class MainApplication(App):
    def build(self):
        self.title = "YouTube Downloader"
        self.icon = 'icons/download.jpg'
        return MyLayout()
if __name__ == '__main__':
    MainApplication().run()