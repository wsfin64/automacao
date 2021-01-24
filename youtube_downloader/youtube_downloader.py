from pytube import YouTube


class DownloadError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class YoutubeDownloader:
    def __init__(self, link):
        self.__link = link
        self.__url = None
        self.__video = None

    @property
    def link(self):
        return self.__link

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, nova_url):
        self.__url = nova_url

    @property
    def video(self):
        return self.__video

    @video.setter
    def video(self, novo_video):
        self.__video = novo_video

    def link_vazio(self):
        if self.link == '':
            return True

    def download(self):
        if self.link_vazio():
            raise DownloadError('Você precisa informar uma url do Youtube!')
        else:
            self.url = YouTube(self.link)
            self.video = self.__url.streams.filter(progressive=True, file_extension='mp4')
            self.video.get_highest_resolution().download()


if __name__ == '__main__':
    while True:
        try:
            entrada_video = str(input('Informe a url do video: '))

            obj = YoutubeDownloader(entrada_video)

            print('Downloading...')
            obj.download()
            print('Download finalizado!')
            print(obj.url.title)

            continuar = input('Deseja baixar outro vídeo? [s/n]').lower()

            if continuar != 's':
                break

        except DownloadError as err:
            print(err)
        except Exception as err2:
            print(err2)
            print('Informe uma url valida!')
