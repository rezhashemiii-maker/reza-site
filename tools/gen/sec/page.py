# -*- coding: utf-8 -*-
import io, os
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paths import SRC  # noqa: E402
HERE = os.path.dirname(os.path.abspath(__file__))
logic = io.open(os.path.join(HERE, 'logic.js'), encoding='utf-8').read().strip()
CARD = 'background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px;'

PAGE = '''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>پنجاه سال دفاع — نقشهٔ آثاری که معماری امنیت را ساختند</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&amp;display=swap">
<style>
  body{margin:0;font-family:'Vazirmatn',system-ui,sans-serif;background:#F5F3EE;color:#16181C;-webkit-font-smoothing:antialiased}
  a{color:#2F5233;text-decoration:none}
  a:hover{color:#1F3A22}
  button{font-family:inherit;cursor:pointer;border:none}
  html{scroll-behavior:smooth}
  [id]{scroll-margin-top:92px}
  ::selection{background:#E7ECE4;color:#1F3A22}
  input{font-family:inherit;font-size:15px;color:#16181C;background:#FFFFFF;border:1px solid #D9D5C9;border-radius:12px;padding:13px 16px;width:100%;box-sizing:border-box}
  input:focus{outline:2px solid #2F5233;outline-offset:1px}
</style>
</helmet>

<div style="width: 100%; min-height: 100vh; background: #F5F3EE; direction: rtl;">

  <header style="position: sticky; top: 0; z-index: 40; border-bottom: 1px solid #E4E1D6; background: rgba(245,243,238,0.94); backdrop-filter: blur(10px);">
    <div style="max-width: 1120px; margin: 0 auto; padding: 14px 24px; display: flex; align-items: center; gap: 14px; flex-wrap: wrap;">
      <a href="Main.dc.html#writing" style="font-size: 13.5px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <nav style="display: flex; gap: 2px; margin-inline-start: auto; flex-wrap: wrap;">
        <a href="#s1" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۱ خط زمان</a>
        <a href="#s2" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۲ شتاب</a>
        <a href="#s3" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۳ کتابخانه</a>
        <a href="#s4" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۴ آینده</a>
        <a href="#s5" style="font-size: 12.5px; color: #45494F; padding: 6px 9px; border-radius: 999px;">۰۵ روش</a>
      </nav>
    </div>
  </header>

  <main>

    <!-- ============ هیرو ============ -->
    <section style="max-width: 1120px; margin: 0 auto; padding: 60px 24px 10px;">
      <p style="font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: #2F5233; margin: 0 0 16px;">پروژهٔ تحقیقاتی، {{totalFa}} اثر، {{spanFa}} سال · از ۱۹۷۳ تا امروز</p>
      <h1 style="font-size: clamp(30px, 5vw, 50px); line-height: 1.38; font-weight: 800; margin: 0 0 20px; letter-spacing: -0.01em;">پنجاه سال دفاع</h1>
      <p style="font-size: 18.5px; line-height: 1.95; color: #45494F; max-width: 64ch; margin: 0 0 18px;">امنیت اطلاعات یک رشتهٔ مهندسی نبود؛ ساخته شد. در این نقشه <b>{{totalFa}} اثر</b> — کتاب، مقاله، استاندارد و چارچوب — را به ترتیب تاریخ کنار هم گذاشته‌ام و برای هرکدام نوشته‌ام <b>دقیقاً چه چیزی را جلو برد</b>.</p>
      <p style="font-size: 16px; line-height: 2; color: #45494F; max-width: 64ch; margin: 0 0 16px;">خطِ داستان ساده است و در نمودار پایین دیده می‌شود: نیم قرن تلاش برای ساختن یک مرز قابل‌دفاع، و بعد فروپاشی تدریجی خودِ مفهوم مرز — اول با ابر و موبایل، و حالا با سامانه‌هایی که ورودی و دستور را از هم تشخیص نمی‌دهند.</p>
      <p style="font-size: 14.5px; line-height: 1.9; color: #666158; max-width: 64ch; margin: 0 0 30px;">{{mlFa}} اثر از این فهرست دربارهٔ امنیتِ خودِ یادگیری ماشین است و {{mlRecentFa}} تای آن‌ها فقط از ۲۰۱۳ به بعد منتشر شده‌اند. بخش ۰۴ دربارهٔ همین است.</p>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="#s3" style="font-size: 14.5px; font-weight: 700; color: #FFFFFF; background: #2F5233; padding: 13px 26px; border-radius: 10px;">رفتن به کتابخانه</a>
        <a href="#s4" style="font-size: 14.5px; font-weight: 700; color: #16181C; background: #FFFFFF; border: 1px solid #E4E1D6; padding: 13px 26px; border-radius: 10px;">آینده: هوش مصنوعی و معماری امنیت</a>
      </div>
    </section>

    <!-- ============ ۰۱ خط زمان ============ -->
    <section id="s1" style="max-width: 1120px; margin: 0 auto; padding: 44px 24px 10px;">
      <p style="font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: #2F5233; margin: 0 0 12px;">۰۱ — خط زمان</p>
      <h2 style="font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 14px;">نیم قرن، در یک نگاه</h2>
      <p style="font-size: 15.5px; line-height: 1.95; color: #45494F; max-width: 70ch; margin: 0 0 8px;">بالای خط جداکننده، <b style="color: #A32222;">{{evCountFa}} رویداد</b> نشسته‌اند: حمله‌ها و افشاگری‌هایی که مسیر رشته را عوض کردند. پایینش هر نقطه یک اثر است — جای افقی‌اش سال انتشار، خطِ افقی‌اش دسته، و <b>اندازه‌اش برآورد من از میزان اثرگذاری</b>، نه یک سنجهٔ اندازه‌گیری‌شده.</p>
      <p style="font-size: 13.5px; line-height: 1.9; color: #666158; max-width: 70ch; margin: 0 0 20px;">نشانگر را روی هر نقطه نگه دار تا نامش را ببینی. فیلترهای بخش ۰۳ روی نقطه‌های پایین اثر می‌گذارند؛ رویدادهای بالا همیشه می‌مانند، چون زمینه‌اند نه داده.</p>

      <div style="''' + CARD + ''' padding: 22px 24px 16px; margin-bottom: 14px;">
        <div style="display: flex; gap: 8px 16px; flex-wrap: wrap; margin-bottom: 14px;">
          <span style="display: inline-flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 700; color: #A32222;"><svg viewBox="0 0 16 16" style="width: 13px; height: 13px;"><path d="M 8 2 L 14 8 L 8 14 L 2 8 Z" fill="#A32222"></path></svg>حمله‌ها</span>
          <sc-for list="{{lanes}}" as="l" hint-placeholder-count="6">
            <span style="display: inline-flex; align-items: center; gap: 6px; font-size: 12px; color: #45494F;"><span style="width: 10px; height: 10px; border-radius: 50%; background: {{l.color}}; flex-shrink: 0;"></span>{{l.name}}</span>
          </sc-for>
        </div>
        <svg viewBox="0 0 1000 {{plotH}}" style="width: 100%; height: auto; display: block;" role="img" aria-label="خط زمان شش دستهٔ ادبیات امنیت از ۱۹۷۳ تا امروز، با ردیف حمله‌ها در بالا؛ هر نقطه یک کتاب، مقاله یا استاندارد است و اندازه‌اش برآورد اثرگذاری">
          <sc-for list="{{ticks}}" as="t" hint-placeholder-count="6">
            <line x1="{{t.x}}" y1="4" x2="{{t.x}}" y2="{{t.y2}}" stroke="#EAE7DE" stroke-width="1"></line>
          </sc-for>
          <sc-for list="{{events}}" as="e" hint-placeholder-count="19">
            <path d="{{e.d}}" fill="#A32222" fill-opacity="0.9" stroke="#FFFFFF" stroke-width="1.5"><title>{{e.tip}}</title></path>
          </sc-for>
          <line x1="{{plotX0}}" y1="{{sepY}}" x2="{{plotX1}}" y2="{{sepY}}" stroke="#E4E1D6" stroke-width="1"></line>
          <sc-for list="{{lanes}}" as="l" hint-placeholder-count="6">
            <line x1="{{l.x0}}" y1="{{l.lineY}}" x2="{{l.x1}}" y2="{{l.lineY}}" stroke="#EFECE3" stroke-width="1"></line>
          </sc-for>
          <sc-for list="{{dots}}" as="d" hint-placeholder-count="20">
            <circle cx="{{d.cx}}" cy="{{d.cy}}" r="{{d.r}}" fill="{{d.color}}" fill-opacity="0.85" stroke="#FFFFFF" stroke-width="2"><title>{{d.tip}}</title></circle>
          </sc-for>
        </svg>
        <div style="position: relative; height: 20px; margin-top: 4px;">
          <sc-for list="{{ticks}}" as="t" hint-placeholder-count="6">
            <span style="position: absolute; left: {{t.pct}}%; transform: translateX(-50%); font-size: 11.5px; color: #666158; font-variant-numeric: tabular-nums;">{{t.label}}</span>
          </sc-for>
        </div>
        <div style="display: flex; gap: 10px 20px; flex-wrap: wrap; align-items: center; margin-top: 14px; padding-top: 14px; border-top: 1px solid #F0EEE7;">
          <span style="display: inline-flex; align-items: center; gap: 7px; font-size: 12px; color: #45494F;"><svg viewBox="0 0 16 16" style="width: 14px; height: 14px;"><path d="M 8 2 L 14 8 L 8 14 L 2 8 Z" fill="#A32222"></path></svg>رویداد</span><span style="font-size: 11.5px; color: #666158; margin-inline-start: 8px;">اندازهٔ نقطه = برآورد اثرگذاری:</span>
          <span style="display: inline-flex; align-items: center; gap: 7px; font-size: 12px; color: #45494F;"><svg viewBox="0 0 16 16" style="width: 16px; height: 16px;"><circle cx="8" cy="8" r="4" fill="#666158"></circle></svg>مهم</span>
          <span style="display: inline-flex; align-items: center; gap: 7px; font-size: 12px; color: #45494F;"><svg viewBox="0 0 16 16" style="width: 16px; height: 16px;"><circle cx="8" cy="8" r="5.5" fill="#666158"></circle></svg>بسیار مؤثر</span>
          <span style="display: inline-flex; align-items: center; gap: 7px; font-size: 12px; color: #45494F;"><svg viewBox="0 0 16 16" style="width: 16px; height: 16px;"><circle cx="8" cy="8" r="7" fill="#666158"></circle></svg>نقطهٔ عطف</span>
        </div>
      </div>

      <div style="background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px; padding: 24px 26px; margin-bottom: 14px;">
        <h3 style="font-size: 16px; font-weight: 800; margin: 0 0 4px;">{{evCountFa}} رویدادی که روی خط بالا نشسته‌اند</h3>
        <p style="font-size: 12.8px; line-height: 1.85; color: #666158; margin: 0 0 18px;">به ترتیب تاریخ. اینها حمله یا افشاگری‌اند، نه اثر علمی — ولی بدون آن‌ها نصف این فهرست نوشته نمی‌شد.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px;">
          <sc-for list="{{events}}" as="e" hint-placeholder-count="19">
            <div style="background: #FAFAF7; border-radius: 11px; padding: 14px 16px; border-inline-start: 3px solid #A32222;">
              <div style="display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; margin-bottom: 5px;">
                <span style="font-size: 14.5px; font-weight: 800; color: #A32222; font-variant-numeric: tabular-nums;">{{e.yFa}}</span>
                <span style="font-size: 10.5px; color: #666158;">{{e.m}}</span>
                <h4 style="font-size: 13.5px; font-weight: 700; margin: 0; line-height: 1.6;">{{e.fa}}</h4>
              </div>
              <p style="font-size: 11.5px; color: #666158; direction: ltr; text-align: right; margin: 0 0 6px; unicode-bidi: isolate;">{{e.en}}</p>
              <p style="font-size: 12.5px; line-height: 1.9; color: #45494F; margin: 0;">{{e.note}}</p>
            </div>
          </sc-for>
        </div>
      </div>

      <div style="background: #FFFFFF; border: 1px solid #E4E1D6; border-radius: 16px; padding: 26px 28px; margin-bottom: 14px;">
        <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 6px;">حمله، و بعد پاسخ</h3>
        <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0 0 6px;">الگویی که در نمودار بالا دیده می‌شود، این‌جا با پنج نمونهٔ مستند بیان شده است: ادبیات این رشته اغلب <b>واکنشی</b> است، نه پیش‌دستانه. فاصله هم ثابت نیست — از چند ماه تا پنج سال.</p>
        <p style="font-size: 12.5px; line-height: 1.9; color: #666158; margin: 0 0 6px;">این‌ها رابطهٔ علت و معلولی مستند یا به‌رسمیت‌شناخته‌شده‌اند، نه هم‌زمانی تصادفی.</p>
          <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 14px; align-items: center; padding: 16px 0; border-top: 1px solid #F0EEE7;">
            <div>
              <div style="font-size: 11.5px; font-weight: 700; color: #A32222; font-variant-numeric: tabular-nums;">۱۹۸۸</div>
              <div style="font-size: 14.5px; font-weight: 700; margin-top: 3px; line-height: 1.6;">کرم موریس</div>
            </div>
            <div style="text-align: center; min-width: 86px;">
              <div style="font-size: 16px; color: #B9B3A6; line-height: 1;">←</div>
              <div style="font-size: 10.5px; color: #666158; margin-top: 4px;">هفته‌ها</div>
            </div>
            <div>
              <div style="font-size: 11.5px; font-weight: 700; color: #2F5233; font-variant-numeric: tabular-nums;">۱۹۸۸</div>
              <div style="font-size: 14.5px; font-weight: 700; margin-top: 3px; line-height: 1.6;">تأسیس CERT</div>
            </div>
            <p style="grid-column: 1 / -1; font-size: 12.8px; line-height: 1.95; color: #45494F; margin: 8px 0 0;">مدل تشخیص نفوذ دنینگ یک سال زودتر منتشر شده بود و کسی جدی‌اش نگرفت. موریس آن مقاله را به بودجه و نهاد تبدیل کرد.</p>
          </div>
          <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 14px; align-items: center; padding: 16px 0; border-top: 1px solid #F0EEE7;">
            <div>
              <div style="font-size: 11.5px; font-weight: 700; color: #A32222; font-variant-numeric: tabular-nums;">۲۰۰۱–۲۰۰۳</div>
              <div style="font-size: 14.5px; font-weight: 700; margin-top: 3px; line-height: 1.6;">کد رد و اس‌کیو‌ال اسلمر</div>
            </div>
            <div style="text-align: center; min-width: 86px;">
              <div style="font-size: 16px; color: #B9B3A6; line-height: 1;">←</div>
              <div style="font-size: 10.5px; color: #666158; margin-top: 4px;">≈ یک سال</div>
            </div>
            <div>
              <div style="font-size: 11.5px; font-weight: 700; color: #2F5233; font-variant-numeric: tabular-nums;">۲۰۰۲</div>
              <div style="font-size: 14.5px; font-weight: 700; margin-top: 3px; line-height: 1.6;">نوشتن کد امن</div>
            </div>
            <p style="grid-column: 1 / -1; font-size: 12.8px; line-height: 1.95; color: #45494F; margin: 8px 0 0;">مایکروسافت توسعهٔ ویندوز را موقتاً متوقف کرد و همهٔ برنامه‌نویس‌هایش را به دورهٔ امنیت فرستاد. آن کتاب، خروجی همان دوره است.</p>
          </div>
          <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 14px; align-items: center; padding: 16px 0; border-top: 1px solid #F0EEE7;">
            <div>
              <div style="font-size: 11.5px; font-weight: 700; color: #A32222; font-variant-numeric: tabular-nums;">۲۰۱۰</div>
              <div style="font-size: 14.5px; font-weight: 700; margin-top: 3px; line-height: 1.6;">استاکس‌نت</div>
            </div>
            <div style="text-align: center; min-width: 86px;">
              <div style="font-size: 16px; color: #B9B3A6; line-height: 1;">←</div>
              <div style="font-size: 10.5px; color: #666158; margin-top: 4px;">یک تا سه سال</div>
            </div>
            <div>
              <div style="font-size: 11.5px; font-weight: 700; color: #2F5233; font-variant-numeric: tabular-nums;">۲۰۱۱ و ۲۰۱۳</div>
              <div style="font-size: 14.5px; font-weight: 700; margin-top: 3px; line-height: 1.6;">زنجیرهٔ کشتار و ATT&amp;CK</div>
            </div>
            <p style="grid-column: 1 / -1; font-size: 12.8px; line-height: 1.95; color: #45494F; margin: 8px 0 0;">وقتی مهاجم یک دولت باشد، «جلوی بدافزار را بگیر» بی‌معنا می‌شود. باید رفتار یک کمپین چندماهه را مدل کرد — و همین شد.</p>
          </div>
          <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 14px; align-items: center; padding: 16px 0; border-top: 1px solid #F0EEE7;">
            <div>
              <div style="font-size: 11.5px; font-weight: 700; color: #A32222; font-variant-numeric: tabular-nums;">۲۰۱۳</div>
              <div style="font-size: 14.5px; font-weight: 700; margin-top: 3px; line-height: 1.6;">افشاگری‌های اسنودن</div>
            </div>
            <div style="text-align: center; min-width: 86px;">
              <div style="font-size: 16px; color: #B9B3A6; line-height: 1;">←</div>
              <div style="font-size: 10.5px; color: #666158; margin-top: 4px;">پنج سال</div>
            </div>
            <div>
              <div style="font-size: 11.5px; font-weight: 700; color: #2F5233; font-variant-numeric: tabular-nums;">۲۰۱۸</div>
              <div style="font-size: 14.5px; font-weight: 700; margin-top: 3px; line-height: 1.6;">TLS 1.3</div>
            </div>
            <p style="grid-column: 1 / -1; font-size: 12.8px; line-height: 1.95; color: #45494F; margin: 8px 0 0;">بازطراحی یک پروتکل جهانی کند است. ولی جهتش — حذف هر چیز شکسته و محرمانگی پیشرو به‌صورت پیش‌فرض — همان ۲۰۱۳ تعیین شد.</p>
          </div>
          <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 14px; align-items: center; padding: 16px 0; border-top: 1px solid #F0EEE7;">
            <div>
              <div style="font-size: 11.5px; font-weight: 700; color: #A32222; font-variant-numeric: tabular-nums;">۲۰۲۰</div>
              <div style="font-size: 14.5px; font-weight: 700; margin-top: 3px; line-height: 1.6;">سولارویندز</div>
            </div>
            <div style="text-align: center; min-width: 86px;">
              <div style="font-size: 16px; color: #B9B3A6; line-height: 1;">←</div>
              <div style="font-size: 10.5px; color: #666158; margin-top: 4px;">پنج ماه</div>
            </div>
            <div>
              <div style="font-size: 11.5px; font-weight: 700; color: #2F5233; font-variant-numeric: tabular-nums;">۲۰۲۱</div>
              <div style="font-size: 14.5px; font-weight: 700; margin-top: 3px; line-height: 1.6;">دستور اجرایی ۱۴۰۲۸</div>
            </div>
            <p style="grid-column: 1 / -1; font-size: 12.8px; line-height: 1.95; color: #45494F; margin: 8px 0 0;">سریع‌ترین پاسخ کل این فهرست. دلیلش هم ساده است: این بار قربانی، خودِ دولت فدرال بود.</p>
          </div>
        <div style="background: #F5E1DF; border-radius: 12px; padding: 16px 18px; margin-top: 18px;">
          <span style="font-size: 11.5px; font-weight: 700; color: #A32222;">و جایی که پاسخ، کتاب نبود — </span>
          <span style="font-size: 13.3px; color: #45494F; line-height: 1.95;">پاسخ هارت‌بلید (۲۰۱۴) نه مقاله بود نه استاندارد؛ بودجه‌ای بود برای نگه‌داری کتابخانه‌های حیاتی متن‌باز، چون معلوم شد نیمی از وب روی کدی ایستاده که تقریباً هیچ‌کس پولش را نمی‌دهد. و برای Log4Shell (۲۰۲۱) و درِ پشتی XZ (۲۰۲۴) هنوز هیچ پاسخ ساختاری کاملی نوشته نشده — این دو هنوز سؤال بازند، نه درس گرفته‌شده.</span>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 12px;">
        <sc-for list="{{catCards}}" as="c" hint-placeholder-count="6">
          <div style="''' + CARD + ''' padding: 18px 20px; border-top: 3px solid {{c.color}};">
            <div style="display: flex; align-items: baseline; gap: 9px; margin-bottom: 8px;">
              <h3 style="font-size: 14.5px; font-weight: 700; margin: 0; line-height: 1.5;">{{c.name}}</h3>
              <span style="margin-inline-start: auto; font-size: 12px; font-weight: 700; color: {{c.color}}; background: {{c.soft}}; border-radius: 999px; padding: 2px 9px;">{{c.countFa}}</span>
            </div>
            <p style="font-size: 12.5px; line-height: 1.9; color: #45494F; margin: 0;">{{c.blurb}}</p>
          </div>
        </sc-for>
      </div>
    </section>

    <!-- ============ ۰۲ شتاب ============ -->
    <section id="s2" style="max-width: 1120px; margin: 0 auto; padding: 44px 24px 10px;">
      <p style="font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: #2F5233; margin: 0 0 12px;">۰۲ — شتابِ رشته</p>
      <h2 style="font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 14px;">هر پنج سال، چند اثر ماندگار</h2>
      <p style="font-size: 15.5px; line-height: 1.95; color: #45494F; max-width: 70ch; margin: 0 0 20px;">این نمودار سوگیری دارد و باید با همین سوگیری خوانده شود: آثار نزدیک‌تر هنوز فرصت نکرده‌اند غربال شوند، پس دههٔ اخیر پرتراکم‌تر دیده می‌شود. با این حال جهش پس از ۲۰۱۳ — سالِ کشف نمونهٔ خصمانه — واقعی است.</p>
      <div style="''' + CARD + ''' padding: 24px 26px 18px;">
        <div style="display: flex; align-items: flex-end; gap: 6px; height: 130px; direction: rtl;">
          <sc-for list="{{bars}}" as="b" hint-placeholder-count="12">
            <div style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; gap: 5px;">
              <span style="font-size: 11px; font-weight: 700; color: #45494F; font-variant-numeric: tabular-nums;">{{b.nFa}}</span>
              <div style="width: 100%; height: {{b.h}}px; background: #2F5233; border-radius: 4px 4px 0 0; min-height: 2px;" title="{{b.label}}"></div>
            </div>
          </sc-for>
        </div>
        <div style="display: flex; gap: 6px; margin-top: 8px; padding-top: 8px; border-top: 1px solid #F0EEE7; direction: rtl;">
          <sc-for list="{{bars}}" as="b" hint-placeholder-count="12">
            <span style="flex: 1; text-align: center; font-size: 10px; color: #666158; font-variant-numeric: tabular-nums; overflow: hidden;">{{b.axis}}</span>
          </sc-for>
        </div>
      </div>
    </section>

    <!-- ============ ۰۳ کتابخانه ============ -->
    <section id="s3" style="max-width: 1120px; margin: 0 auto; padding: 44px 24px 10px;">
      <p style="font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: #2F5233; margin: 0 0 12px;">۰۳ — کتابخانه</p>
      <h2 style="font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 14px;">{{totalFa}} اثر، به ترتیب تاریخ</h2>
      <p style="font-size: 15.5px; line-height: 1.95; color: #45494F; max-width: 70ch; margin: 0 0 8px;">از قدیمی‌ترین به تازه‌ترین. هر کارت پیوند به منبع اصلی دارد؛ جایی که نسخهٔ آزادِ رسمی وجود داشته، همان را گذاشته‌ام.</p>
      <p style="font-size: 13.5px; line-height: 1.9; color: #666158; max-width: 70ch; margin: 0 0 20px;"><b>گام بعدی:</b> برای {{bookFa}} کتاب این فهرست، صفحهٔ جداگانه با معرفی کامل در دست نوشتن است و پیوند «توضیحات بیشتر» همین‌جا اضافه می‌شود.</p>

      <div style="position: sticky; top: 49px; z-index: 20; background: #F5F3EE; padding: 12px 0 10px; margin-bottom: 14px; border-bottom: 1px solid #E4E1D6;">
        <input id="q" type="text" value="{{q}}" onInput="{{onQuery}}" placeholder="جست‌وجو در عنوان، پدیدآور و توضیح — فارسی یا انگلیسی">
        <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 10px;">
          <sc-for list="{{kindChips}}" as="f" hint-placeholder-count="4">
            <button onClick="{{f.pick}}" style="font-size: 12.5px; font-weight: 700; border-radius: 999px; padding: 9px 14px; background: {{f.bg}}; color: {{f.fg}}; border: 1px solid {{f.border}};">{{f.label}} <span style="opacity: 0.65;">{{f.count}}</span></button>
          </sc-for>
        </div>
        <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 7px; align-items: center;">
          <sc-for list="{{catChips}}" as="f" hint-placeholder-count="7">
            <button onClick="{{f.pick}}" style="font-size: 12.5px; font-weight: 600; border-radius: 999px; padding: 9px 14px; background: {{f.bg}}; color: {{f.fg}}; border: 1px solid {{f.border}};">{{f.label}} <span style="opacity: 0.65;">{{f.count}}</span></button>
          </sc-for>
          <span style="margin-inline-start: auto; font-size: 12.5px; color: #666158;">{{shownFa}} اثر</span>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(330px, 1fr)); gap: 12px;">
        <sc-for list="{{list}}" as="it" hint-placeholder-count="12">
          <div style="''' + CARD + ''' padding: 20px 22px; border-inline-start: 4px solid {{it.color}}; display: flex; flex-direction: column;">
            <div style="display: flex; align-items: baseline; gap: 9px; flex-wrap: wrap; margin-bottom: 8px;">
              <span style="font-size: 17px; font-weight: 800; color: {{it.color}}; font-variant-numeric: tabular-nums;">{{it.yFa}}</span>
              <span style="font-size: 10.5px; font-weight: 700; color: #666158; background: #F5F3EE; border-radius: 999px; padding: 3px 9px;">{{it.kind}}</span>
              <span style="margin-inline-start: auto; font-size: 10.5px; color: {{it.color}}; background: {{it.soft}}; border-radius: 999px; padding: 3px 9px;">{{it.catName}}</span>
            </div>
            <h3 style="font-size: 15.5px; font-weight: 700; margin: 0 0 6px; line-height: 1.65;">{{it.fa}}</h3>
            <p style="font-size: 12px; color: #666158; direction: ltr; text-align: right; margin: 0 0 6px; line-height: 1.6; unicode-bidi: isolate;">{{it.en}}</p>
            <p style="font-size: 12.5px; color: #45494F; margin: 0 0 12px; line-height: 1.75;">{{it.who}}</p>
            <p style="font-size: 13.3px; line-height: 1.95; color: #45494F; margin: 0 0 14px; flex: 1;">{{it.adv}}</p>
            <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; padding-top: 12px; border-top: 1px solid #F0EEE7;">
              <span style="font-size: 12px; color: #B4530E; letter-spacing: 1px;" title="برآورد اثرگذاری از پنج">{{it.impFa}}</span>
              <a href="{{it.href}}" target="_blank" rel="noopener" style="margin-inline-start: auto; font-size: 12.5px; font-weight: 700; color: {{it.color}};">منبع اصلی ↗</a>
            </div>
            <sc-if value="{{it.b01}}" hint-placeholder-val="{{true}}">
              <a href="SecBook01.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b02}}">
              <a href="SecBook02.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b03}}">
              <a href="SecBook03.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b04}}">
              <a href="SecBook04.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b05}}">
              <a href="SecBook05.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b06}}">
              <a href="SecBook06.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b07}}">
              <a href="SecBook07.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b08}}">
              <a href="SecBook08.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b09}}">
              <a href="SecBook09.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b10}}">
              <a href="SecBook10.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b11}}">
              <a href="SecBook11.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b12}}">
              <a href="SecBook12.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b13}}">
              <a href="SecBook13.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b14}}">
              <a href="SecBook14.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
            <sc-if value="{{it.b15}}">
              <a href="SecBook15.dc.html" style="font-size: 12px; font-weight: 700; color: {{it.color}}; margin-top: 10px; display: inline-block;">صفحهٔ معرفی کامل ←</a>
            </sc-if>
          </div>
        </sc-for>
      </div>

      <sc-if value="{{empty}}" hint-placeholder-val="{{true}}">
        <div style="''' + CARD + ''' border-style: dashed; padding: 40px; text-align: center;">
          <p style="font-size: 14.5px; color: #45494F; margin: 0 0 6px;">با این فیلترها اثری پیدا نشد.</p>
          <p style="font-size: 13px; color: #666158; margin: 0;">شاید با عنوان انگلیسی یا نام پدیدآور جست‌وجو کنی.</p>
        </div>
      </sc-if>
    </section>

    <!-- ============ ۰۴ آینده ============ -->
    <section id="s4" style="background: #EDF1EB; border-top: 1px solid #D5DDD2; border-bottom: 1px solid #D5DDD2; margin-top: 44px;">
      <div style="max-width: 1120px; margin: 0 auto; padding: 56px 24px;">
        <p style="font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: #2F5233; margin: 0 0 12px;">۰۴ — نتیجه‌گیری</p>
        <h2 style="font-size: clamp(24px, 3.4vw, 34px); font-weight: 800; margin: 0 0 18px; line-height: 1.45;">آینده: هوش مصنوعی، یادگیری ماشین و معماری امنیت</h2>
        <p style="font-size: 17px; line-height: 2.05; color: #45494F; max-width: 68ch; margin: 0 0 26px;">اگر این {{totalFa}} اثر را پشت سر هم بخوانی، یک الگو تکرار می‌شود: هر بار که یک مرز قابل‌دفاع ساخته شد، لایهٔ بعدیِ فناوری آن مرز را بی‌معنا کرد. آنچه امروز اتفاق می‌افتد، تکرار همان الگو در بنیادی‌ترین سطح ممکن است.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">

          <div style="''' + CARD + ''' padding: 24px 26px; border-top: 3px solid #BE185D;">
            <div style="font-size: 11.5px; font-weight: 700; color: #BE185D; margin-bottom: 10px;">۰۱ — مرزی که فرو ریخت</div>
            <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px; line-height: 1.55;">داده و دستور، دیگر از هم جدا نیستند</h3>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 12px;">کل معماری امنیت پنجاه سال روی یک تفکیک بنا شده بود: این بخش <b>داده</b> است و این بخش <b>دستور</b>. سرریز بافر، تزریق SQL و XSS هر سه نقض همین مرزند و راه‌حلشان هم یکی بود: مرز را سفت‌تر کن.</p>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0;">مدل زبانی این تفکیک را ندارد. هر متنی که می‌خواند، هم‌زمان داده و دستور است. مقالهٔ گرشیک (۲۰۲۳) نشان داد این یک باگ پیاده‌سازی نیست؛ ویژگی معماری است. تا امروز هیچ راه‌حل کاملی برایش منتشر نشده و احتمال اینکه با یک وصلهٔ هوشمندانه حل شود، کم است.</p>
          </div>

          <div style="''' + CARD + ''' padding: 24px 26px; border-top: 3px solid #0D9488;">
            <div style="font-size: 11.5px; font-weight: 700; color: #0D9488; margin-bottom: 10px;">۰۲ — دارایی تازه</div>
            <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px; line-height: 1.55;">مدل، هم‌زمان دارایی و نشت است</h3>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 12px;">شوکری (۲۰۱۷) نشان داد می‌شود فهمید یک رکورد در دادهٔ آموزش بوده یا نه. کارلینی (۲۰۲۱) نشان داد می‌شود خودِ متن را کلمه‌به‌کلمه بیرون کشید. یعنی وزن‌های مدل، یک کپیِ فشرده و نشت‌دار از دادهٔ آموزش‌اند.</p>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0;">نتیجهٔ معماری‌اش روشن است: مدل باید مثل پایگاه داده طبقه‌بندی شود، نه مثل یک فایل اجرایی. کنترل دسترسی، رمزنگاری در حالت سکون، و ثبت دسترسی — همان چیزهایی که برای داده بدیهی است.</p>
          </div>

          <div style="''' + CARD + ''' padding: 24px 26px; border-top: 3px solid #C2410C;">
            <div style="font-size: 11.5px; font-weight: 700; color: #C2410C; margin-bottom: 10px;">۰۳ — ادامهٔ اعتماد صفر</div>
            <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px; line-height: 1.55;">از محیط، به هویت، و حالا به <i>نیت</i></h3>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 12px;">مسیر روشن است: فروم جریکو (۲۰۰۴) گفت محیط مرده است؛ کیندروگ (۲۰۱۰) اسمش را گذاشت؛ NIST (۲۰۲۰) معماری‌اش را نوشت. در هر سه، واحدِ اعتماد از «جای شبکه» به «هویت» منتقل شد.</p>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0;">عامل‌های خودمختار گام بعدی را تحمیل می‌کنند: یک عامل هویت معتبر دارد و مجاز است — ولی ممکن است کاری بکند که کاربر نخواسته. سؤال امنیتی از «این کیست؟» به «این دارد از طرف چه کسی و با چه مجوزی عمل می‌کند؟» منتقل می‌شود. این یعنی مجوزِ محدود به وظیفه، سقف مشخص برای هر اقدام، و ثبت قابل‌ردیابی هر تصمیم — چیزی شبیه اصل «کمترین امتیاز» سالتزر و شرودر، منتها برای چیزی که خودش تصمیم می‌گیرد.</p>
          </div>

          <div style="''' + CARD + ''' padding: 24px 26px; border-top: 3px solid #7E22CE;">
            <div style="font-size: 11.5px; font-weight: 700; color: #7E22CE; margin-bottom: 10px;">۰۴ — طرف دفاع</div>
            <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px; line-height: 1.55;">چرا یادگیری ماشین هنوز تشخیص را حل نکرده</h3>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 12px;">رؤیای دنینگ در ۱۹۸۷ همین بود: رفتار عادی را یاد بگیر و از انحراف هشدار بده. چهار دهه بعد، هنوز کامل نشده — و دلیلش فنی نیست، آماری است.</p>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0;">وقتی نرخ پایهٔ حمله بسیار پایین است، حتی یک تشخیص‌دهندهٔ ۹۹ درصد دقیق، سیل هشدار کاذب تولید می‌کند. این همان درسی است که در سؤال «دقت ۹۹ درصد روی بیماری نادر» تکرار می‌شود. یادگیری ماشین در تشخیص، <b>غربال‌گر</b> خوبی است و <b>تصمیم‌گیرندهٔ</b> بدی — و هر معماری‌ای که این دو را یکی بگیرد، شکست می‌خورد.</p>
          </div>

          <div style="''' + CARD + ''' padding: 24px 26px; border-top: 3px solid #0E6FB4;">
            <div style="font-size: 11.5px; font-weight: 700; color: #0E6FB4; margin-bottom: 10px;">۰۵ — اقتصاد</div>
            <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px; line-height: 1.55;">هزینهٔ حمله پایین آمد، هزینهٔ دفاع نه</h3>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 12px;">راس اندرسون سال‌ها پیش گفت امنیت بیشتر یک مسئلهٔ اقتصادی است تا فنی: جایی خراب می‌شود که هزینه را یکی بدهد و فایده را دیگری ببرد.</p>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0;">ابزارهای مولد، هزینهٔ نوشتن ایمیل فیشینگ باورپذیر، جست‌وجوی الگوی آسیب‌پذیر در کد و تولید بدافزار متنوع را به‌شدت پایین آورده‌اند. طرف دفاع هم همین ابزار را دارد، ولی دفاع باید همه‌جا درست کار کند و حمله فقط یک‌جا. این عدم‌تقارن با ارزان‌شدن ابزار، <b>به نفع مهاجم</b> بزرگ‌تر می‌شود — و تنها پاسخ ساختاری‌اش کم‌کردن سطح حمله است، نه بالا بردن سرعت واکنش.</p>
          </div>

          <div style="''' + CARD + ''' padding: 24px 26px; border-top: 3px solid #166534;">
            <div style="font-size: 11.5px; font-weight: 700; color: #166534; margin-bottom: 10px;">۰۶ — آنچه عوض نمی‌شود</div>
            <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 12px; line-height: 1.55;">هشت اصل ۱۹۷۵ هنوز سر جایشان‌اند</h3>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0 0 12px;">نکتهٔ عجیب این فهرست این است: هرچه فناوری عوض شد، اصول سالتزر و شرودر عوض نشدند. کمترین امتیاز، پیش‌فرضِ امنِ شکست، میانجی‌گری کامل و طراحی باز، دقیقاً همان‌قدر که برای یک سامانهٔ اشتراک زمانی در ۱۹۷۵ معنا داشتند، برای یک عامل هوش مصنوعی در ۲۰۲۶ معنا دارند.</p>
            <p style="font-size: 14px; line-height: 2; color: #45494F; margin: 0;">اگر قرار باشد از این پنجاه سال یک چیز برداشت، همین است: <b>فناوری‌ها مسئله را جابه‌جا می‌کنند، اصول را باطل نمی‌کنند.</b></p>
          </div>
        </div>

        <div style="''' + CARD + ''' padding: 26px 28px;">
          <h3 style="font-size: 17px; font-weight: 800; margin: 0 0 8px;">سه پیش‌بینی قابل‌سنجش</h3>
          <p style="font-size: 13.5px; line-height: 1.9; color: #666158; margin: 0 0 18px;">این‌ها پیش‌بینی‌اند، نه نتیجه‌گیری از داده. عمداً طوری نوشته شده‌اند که بشود بعداً غلط‌بودنشان را ثابت کرد.</p>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
            <div style="background: #FAFAF7; border-radius: 12px; padding: 18px 20px;">
              <div style="font-size: 12px; font-weight: 700; color: #2F5233; margin-bottom: 8px;">۰۱</div>
              <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">تزریق غیرمستقیم دستور تا پایان ۲۰۲۸ «حل» نمی‌شود. مدیریت می‌شود — با جداسازی مجوز و تأیید انسانی در اقدام‌های پرخطر — ولی راه‌حل عمومی و اثبات‌پذیری منتشر نمی‌شود.</p>
            </div>
            <div style="background: #FAFAF7; border-radius: 12px; padding: 18px 20px;">
              <div style="font-size: 12px; font-weight: 700; color: #2F5233; margin-bottom: 8px;">۰۲</div>
              <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">«هویت عامل» به یک مقولهٔ جداگانه در استانداردها تبدیل می‌شود — جدا از هویت کاربر و هویت سرویس — و یک سند مرجع از NIST یا IETF برایش منتشر خواهد شد.</p>
            </div>
            <div style="background: #FAFAF7; border-radius: 12px; padding: 18px 20px;">
              <div style="font-size: 12px; font-weight: 700; color: #2F5233; margin-bottom: 8px;">۰۳</div>
              <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">مهاجرت پساکوانتومی، نه شکستن رمزنگاری، بزرگ‌ترین پروژهٔ امنیتی دههٔ پیش رو خواهد بود — و بیشتر سازمان‌ها دیرتر از موعد شروعش می‌کنند.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ ۰۵ روش ============ -->
    <section id="s5" style="max-width: 1120px; margin: 0 auto; padding: 50px 24px 64px;">
      <p style="font-size: 12px; letter-spacing: 0.12em; font-weight: 700; color: #2F5233; margin: 0 0 12px;">۰۵ — روش و محدودیت‌ها</p>
      <h2 style="font-size: clamp(22px, 3vw, 30px); font-weight: 800; margin: 0 0 22px;">این فهرست چطور ساخته شد</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 14px;">
        <div style="''' + CARD + ''' padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">معیار انتخاب</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">اثری وارد فهرست شده که <b>چیزی را برای اولین بار ممکن کرده باشد</b> یا <b>زبان مشترکی ساخته باشد</b> که بعدش همه با آن حرف زدند. کتاب‌های آموزشی خوب ولی بدون سهم مفهومی، و مقاله‌های پرارجاع ولی کم‌اثر، عمداً نیامده‌اند.</p>
        </div>
        <div style="''' + CARD + ''' padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">تاریخ‌ها</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">سالِ <b>اولین انتشار عمومی</b> ملاک است؛ برای مقاله‌هایی که ابتدا روی arXiv آمده‌اند، همان سال ثبت شده و نه سال کنفرانس. برای کتاب‌ها سال ویرایش اول، مگر جایی که ویرایش بعدی خودش اثر مستقلی بوده باشد.</p>
        </div>
        <div style="''' + CARD + ''' padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">عدد اثرگذاری</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">ستاره‌ها <b>قضاوت من‌اند، نه سنجه</b>. شمار ارجاع را ملاک نگذاشته‌ام چون استاندارد و کتاب با مقاله قابل‌مقایسه نیستند. ملاکم این بوده که اگر این اثر نبود، چقدر از آنچه امروز بدیهی است وجود نداشت.</p>
        </div>
        <div style="''' + CARD + ''' padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">سوگیری‌هایی که می‌دانم</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">فهرست به‌شدت <b>انگلیسی‌زبان و آمریکایی</b> است؛ کارهای مهم روسی، چینی و اروپایی که به انگلیسی منتشر نشده‌اند در آن نیستند. آثار نزدیک به امروز هم هنوز غربال تاریخی نشده‌اند و احتمالاً چند تایشان ده سال دیگر بی‌اهمیت به‌نظر می‌رسند.</p>
        </div>
        <div style="''' + CARD + ''' padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">چه چیزی عمداً نیامده</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">کتاب‌های روزنامه‌نگارانه دربارهٔ حمله‌های مشهور، گزارش‌های سالانهٔ شرکت‌های امنیتی، و ابزارها بدون مقالهٔ پشتیبان. همه‌شان ارزشمندند ولی معیار «جلو بردن علم» را برآورده نمی‌کنند.</p>
        </div>
        <div style="''' + CARD + ''' padding: 22px 24px;">
          <h3 style="font-size: 15px; font-weight: 800; margin: 0 0 10px;">گام بعدی</h3>
          <p style="font-size: 13.5px; line-height: 1.95; color: #45494F; margin: 0;">برای {{bookFa}} کتاب این فهرست، صفحهٔ معرفی جداگانه نوشته می‌شود: چه می‌گوید، برای چه کسی است، کدام فصل‌ها هنوز به‌کار می‌آیند و کدام‌ها تاریخ گذشته‌اند. پیوندشان از همین کارت‌ها اضافه خواهد شد.</p>
        </div>
      </div>
    </section>

  </main>

  <footer style="border-top: 1px solid #E4E1D6; background: #FFFFFF;">
    <div style="max-width: 1120px; margin: 0 auto; padding: 24px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <a href="Main.dc.html#writing" style="font-size: 13px; font-weight: 600; color: #45494F;">← بازگشت به نوشته‌ها</a>
      <span style="font-size: 12.5px; color: #666158;">رضا هاشمی · نقشهٔ ادبیات امنیت</span>
    </div>
  </footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1120,"height":1400}}'>
''' + logic + '''
</script>
</body>
</html>
'''

io.open(os.path.join(SRC, 'Security.dc.html'), 'w', encoding='utf-8').write(PAGE)
print('written', len(PAGE), 'chars')
