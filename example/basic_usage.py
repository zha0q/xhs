import datetime
import json
from time import sleep

from playwright.sync_api import sync_playwright

from xhs import DataFetchError, XhsClient, help


def sign(uri, data=None, a1="", web_session=""):
    for _ in range(10):
        try:
            with sync_playwright() as playwright:
                stealth_js_path = "/Users/reajason/ReaJason/xhs/tests/stealth.min.js"
                chromium = playwright.chromium

                # 如果一直失败可尝试设置成 False 让其打开浏览器，适当添加 sleep 可查看浏览器状态
                browser = chromium.launch(headless=True)

                browser_context = browser.new_context()
                browser_context.add_init_script(path=stealth_js_path)
                context_page = browser_context.new_page()
                context_page.goto("https://www.xiaohongshu.com")
                browser_context.add_cookies([
                    {'name': 'a1', 'value': a1, 'domain': ".xiaohongshu.com", 'path': "/"}]
                )
                context_page.reload()
                # 这个地方设置完浏览器 cookie 之后，如果这儿不 sleep 一下签名获取就失败了，如果经常失败请设置长一点试试
                sleep(1)
                encrypt_params = context_page.evaluate("([url, data]) => window._webmsxyw(url, data)", [uri, data])
                return {
                    "x-s": encrypt_params["X-s"],
                    "x-t": str(encrypt_params["X-t"])
                }
        except Exception:
            # 这儿有时会出现 window._webmsxyw is not a function 或未知跳转错误，因此加一个失败重试趴
            pass
    raise Exception("重试了这么多次还是无法签名成功，寄寄寄")


if __name__ == '__main__':
    cookie = "abRequestId=001e4c22-98ac-5d7a-b700-cb35ffa1f2ce; a1=19681665cdcpu7qp32um2pajo16uvza06w7kk64rv30000270199; webId=05b93491e6b09eaa10fba0b0c7561e9b; gid=yjKYyKKKfSKYyjKYyKK2SEK4fSU7WAUqJ76JWFhU0VlyKTq87hu08T888JW8yjj8D8KWDiyS; customerClientId=356571325614448; webBuild=4.62.3; web_session=040069b36e452512f89e793c2d3a4bd4adb509; xsecappid=xhs-pc-web; acw_tc=0a5088c817469372628202288e7b066569acdc2785b9f4782f5b4951d66746; loadts=1746937651177; websectiga=2845367ec3848418062e761c09db7caf0e8b79d132ccdd1a4f8e64a11d0cac0d; sec_poison_id=57b93fa3-5c0c-45e0-8f2e-28c8b7dc33a8; unread={%22ub%22:%22681cc682000000000f033e75%22%2C%22ue%22:%22681f4163000000000f031154%22%2C%22uc%22:25}"

    xhs_client = XhsClient(cookie, sign=sign)
    print(datetime.datetime.now())

    for _ in range(10):
        # 即便上面做了重试，还是有可能会遇到签名失败的情况，重试即可
        try:
            note = xhs_client.get_note_by_id("6505318c000000001f03c5a6", "xsec_token of the note")
            print(json.dumps(note, indent=4))
            print(help.get_imgs_url_from_note(note))
            break
        except DataFetchError as e:
            print(e)
            print("失败重试一下下")
