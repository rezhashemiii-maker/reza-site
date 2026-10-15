#!/usr/bin/env python3
"""تست محدود تعاملات خروجی استاتیک؛ بدون اتصال به سایت زنده یا ارسال فرم."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import argparse
import re

from playwright.sync_api import expect, sync_playwright


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', nargs='?', default='dist')
    args = parser.parse_args()
    output = Path(args.output).resolve()
    if not (output / 'index.html').is_file():
        raise SystemExit('ابتدا خروجی سایت را بسازید.')

    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(output)))
    Thread(target=server.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{server.server_port}'
    try:
        with sync_playwright() as playwright:
            # نسخهٔ نصب‌شدهٔ Playwright در CI اولویت دارد؛ Chromium سیستم مسیر جایگزین است.
            try:
                browser = playwright.chromium.launch(headless=True)
            except Exception:
                browser = playwright.chromium.launch(executable_path='/usr/bin/chromium', headless=True)
            with browser:
                page = browser.new_page(viewport={'width': 1280, 'height': 900})
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                # تست نباید به شبکهٔ فونت یا سرویس بیرونی وابسته باشد.
                page.route('https://fonts.googleapis.com/**', lambda route: route.abort())
                page.route('https://fonts.gstatic.com/**', lambda route: route.abort())

                for file, total, filter_name, filtered in [
                    ('glossary.html', 285, r'۲۴ واژه', 24),
                    ('ideas.html', 100, r'سلامت و پزشکی', 10),
                ]:
                    page.goto(f'{base}/{file}', wait_until='load')
                    expect(page.locator('#q')).to_be_visible()
                    headings = page.locator('h3')
                    baseline = headings.count()
                    assert baseline >= total, f'{file}: پیش‌رندر فهرست ناقص است'
                    static_headings = baseline - total
                    page.locator('#q').fill('zzzxxyy-no-result-20261016')
                    expect(headings).to_have_count(static_headings)
                    page.locator('#q').fill('')
                    expect(headings).to_have_count(baseline)
                    page.get_by_role('button', name=re.compile(filter_name)).click()
                    expect(headings).to_have_count(static_headings + filtered)
                    print(f'PASS {file}: جست‌وجو، پاک‌کردن جست‌وجو و فیلتر')

                page.goto(f'{base}/demo.html', wait_until='load')
                before = page.locator('main').inner_text()
                page.get_by_role('button', name=re.compile('روز بعد')).click()
                expect(page.locator('main')).not_to_have_text(before)
                page.locator('#p-price').fill('200000')
                expect(page.locator('#p-price')).to_have_value('200000')
                page.get_by_role('button', name='بازنشانی', exact=True).click()
                expect(page.locator('#p-price')).to_have_value('185000')
                print('PASS demo.html: روز بعد، ورودی و بازنشانی')

                page.set_viewport_size({'width': 375, 'height': 812})
                for file in ['index.html', 'contact.html']:
                    page.goto(f'{base}/{file}', wait_until='load')
                    expect(page.locator('h1')).to_be_visible()
                    expect(page.locator('header')).to_be_visible()
                    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'{file}: اسکرول افقی در موبایل'
                expect(page.locator('a[href="mailto:rez.hashemiii@gmail.com"]').first).to_be_visible()
                expect(page.locator('header [aria-current="page"]')).to_have_attribute('href', 'contact.html')
                assert '[لینک LinkedIn]' not in page.content()
                expect(page.locator('a[href="https://github.com/rezhashemiii-maker"]').first).to_be_visible()
                print('PASS index.html/contact.html: نمایش موبایل، عنوان، منو و لینک تماس')
                assert not errors, 'خطای JavaScript مرورگر: ' + '; '.join(errors)
                print('تست محدود مرورگر موفق بود: ۵ صفحه، بدون خطای JavaScript')
    finally:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    main()
