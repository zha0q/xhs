import datetime
import json

import requests

import xhs.help
from xhs import XhsClient


def sign(uri, data=None, a1="", web_session=""):
    # 填写自己的 flask 签名服务端口地址
    res = requests.post("http://localhost:5005/sign",
                        json={"uri": uri, "data": data, "a1": a1, "web_session": web_session})
    signs = res.json()
    return {
        "x-s": signs["x-s"],
        "x-t": signs["x-t"]
    }


if __name__ == '__main__':
    cookie = "abRequestId=001e4c22-98ac-5d7a-b700-cb35ffa1f2ce; a1=19681665cdcpu7qp32um2pajo16uvza06w7kk64rv30000270199; webId=05b93491e6b09eaa10fba0b0c7561e9b; gid=yjKYyKKKfSKYyjKYyKK2SEK4fSU7WAUqJ76JWFhU0VlyKTq87hu08T888JW8yjj8D8KWDiyS; customerClientId=356571325614448; webBuild=4.62.3; web_session=040069b36e452512f89e793c2d3a4bd4adb509; xsecappid=xhs-pc-web; acw_tc=0a5088c817469372628202288e7b066569acdc2785b9f4782f5b4951d66746; loadts=1746937651177; websectiga=2845367ec3848418062e761c09db7caf0e8b79d132ccdd1a4f8e64a11d0cac0d; sec_poison_id=57b93fa3-5c0c-45e0-8f2e-28c8b7dc33a8; unread={%22ub%22:%22681cc682000000000f033e75%22%2C%22ue%22:%22681f4163000000000f031154%22%2C%22uc%22:25}"
    xhs_client = XhsClient(cookie, sign=sign)
    # get note info
    note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")
    print(datetime.datetime.now())
    print(json.dumps(note_info, indent=2))
    print(xhs.help.get_imgs_url_from_note(note_info))
