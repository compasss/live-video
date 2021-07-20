import subprocess
from .realurl.huya import get_real_url as get_real_url_hu_ya
from .realurl.douyin import get_real_url as get_real_url_dou_yin

class VideoHistoryService:
    def execList(self, url):
        data = subprocess.check_output(['annie', '-i', '-j', url])
        return data


class LiveUrlService:
    def get_urls(self, room_id, live_type='huya'):
        if live_type == 'huya':
            data = get_real_url_hu_ya(room_id)
        else:
            data = get_real_url_hu_ya(room_id)
        return data

