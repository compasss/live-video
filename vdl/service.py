import subprocess
from .realurl.huya import get_real_url


class VideoHistoryService:
    def execList(self, url):
        data = subprocess.check_output(['annie', '-i', '-j', url])
        return data


class LiveUrlService:
    def get_urls(self, room_id):
        data = get_real_url(room_id)
        return data

