# -*- coding: utf-8 -*-
"""همهٔ ژنراتورهای src/ را به ترتیب درست اجرا می‌کند.

ترتیب اهمیت دارد:
  ۱) صفحه‌های تولیدی مستقل  (a16, chess, sec, serv)
  ۲) انتقال آرتبوردهای آرتیفکت و پرکردن راهنمای پروژه‌ها  (port)
  ۳) صفحه‌های کتاب و تزریقشان در Books.dc.html  (books) — بعد از port
  ۴) کتابخانه، که ارجاع‌های همهٔ صفحه‌های دیگر را جمع می‌کند  (lib) — آخر از همه

  python3 tools/gen/run.py            همه
  python3 tools/gen/run.py sec books  فقط این دو
"""
import os, subprocess, sys

GEN = os.path.dirname(os.path.abspath(__file__))

STEPS = [
    ('a16',   ['a16/page.py']),
    ('chess', ['chess/page.py']),
    ('sec',   ['sec/logic.py', 'sec/page.py']),
    ('serv',  ['serv/logic.py', 'serv/page.py']),
    ('port',  ['port.py', 'lessons.py']),
    ('books', ['books/page.py']),
    ('lib',   ['lib/collect.py', 'lib/logic.py', 'lib/page.py']),
]

want = sys.argv[1:]
fail = 0
for name, scripts in STEPS:
    if want and name not in want:
        continue
    for s in scripts:
        print('\n── %s' % s)
        r = subprocess.run([sys.executable, os.path.join(GEN, s)], cwd=GEN)
        if r.returncode:
            fail += 1
            print('   ✗ شکست خورد')
print('\n%s' % ('همه‌چیز ساخته شد' if not fail else '%d گام شکست خورد' % fail))
sys.exit(1 if fail else 0)
