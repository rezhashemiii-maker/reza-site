# مسیر یادگیری مهندس هوش مصنوعی (AI Engineer Roadmap)
**رضا هاشمی** — شش مرحله، شصت پروژهٔ کاربردی با دیتاست‌های عمومی

---

## مرحله ۱ — پایتون و مهندسی نرم‌افزار
پایه‌ای که همه‌چیز رویش ساخته می‌شود: کد تمیز، کار با داده و ابزارهای روزمرهٔ یک مهندس.

### سرفصل‌ها
- Functions، Classes و Data Structures
- Git و APIها
- NumPy، Pandas و SQL

### نکات مهم یادگیری
- کد تمیز مهم‌تر از کد زیاد است: توابع کوچک، نام‌گذاری روشن، type hint.
- از روز اول Git و venv / requirements.txt داشته باشید.
- SQL را جدی بگیرید؛ بیشتر دادهٔ واقعی در پایگاه داده است، نه CSV.

### پروژه‌ها
1. **داشبورد قیمت مواد غذایی و تورم** — دیتاست: [FAO Food Price Index](https://www.fao.org/worldfoodsituation/foodpricesindex/en/). پاک‌سازی با Pandas، ذخیره در SQLite، کوئری روند ماهانه و داشبورد Streamlit. _قیمت غذا دغدغهٔ همه است؛ این داشبورد نشان می‌دهد کدام اقلام سریع‌تر گران شده‌اند._
2. **تحلیل کیفیت هوای شهرها** — دیتاست: [OpenAQ](https://openaq.org). دریافت داده از API، ذخیره در SQL، گزارش روزهای آلوده و مقایسهٔ شهرها. _کمک می‌کند ببینیم کدام ساعت‌ها و فصل‌ها برای فعالیت بیرون از خانه امن‌ترند._
3. **تحلیل تأخیر پروازها** — دیتاست: [US DOT Flight Delays (Kaggle)](https://www.kaggle.com/datasets/usdot/flight-delays). پاک‌سازی دادهٔ حجیم و کوئری‌های SQL برای یافتن بدترین فرودگاه، ساعت و ایرلاین. _جواب یک سؤال ساده و پرکاربرد: کِی و با کدام ایرلاین پرواز کنیم که کمتر معطل شویم._
4. **ردیاب مخارج شخصی (CLI + SQLite)** — دیتاست: [Personal Finance datasets (Kaggle)](https://www.kaggle.com/search?q=personal+finance+transactions). اپ خط فرمان مبتنی بر Classes، دسته‌بندی خودکار هزینه‌ها و گزارش ماهانه. _ابزاری که هر کسی برای مدیریت بودجهٔ خانه می‌تواند استفاده کند._
5. **کاوش داده‌های زلزله** — دیتاست: [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/). دریافت زندهٔ داده، نقشهٔ تعاملی و آمار فراوانی و شدت به تفکیک منطقه. _تصویری روشن از ریسک لرزه‌ای مناطق، با دادهٔ رسمی و زنده._
6. **تحلیل بازار خودروی کارکرده** — دیتاست: [Craigslist Cars & Trucks (Kaggle)](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data). پاک‌سازی آگهی‌ها، حذف داده‌های پرت و تحلیل افت قیمت بر اساس سن، کارکرد و برند. _به خریدار کمک می‌کند بفهمد قیمت یک خودروی دست‌دوم منصفانه است یا نه._
7. **داشبورد بازار اجارهٔ کوتاه‌مدت** — دیتاست: [Inside Airbnb](https://insideairbnb.com/get-the-data/). ادغام چند فایل CSV، جدول‌های SQL و نقشهٔ قیمت هر محله. _هم مسافر و هم صاحب‌خانه می‌بینند قیمت منطقی هر محله چقدر است._
8. **تحلیل تصادفات رانندگی** — دیتاست: [US Accidents (Kaggle)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents). کار با چند میلیون ردیف، تحلیل اثر آب‌وهوا، ساعت و نوع جاده بر تصادف. _پیدا کردن نقطه‌ها و ساعت‌های پرخطر، یعنی رانندگی امن‌تر._
9. **تحلیل تغییرات دما و بارش** — دیتاست: [NOAA GHCN-Daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily). کار با سری زمانی چنددهه‌ای، میانگین متحرک و مقایسهٔ شهرها. _نشان دادن تغییر اقلیم با دادهٔ واقعی ایستگاه‌ها، نه با حدس._
10. **تحلیل کتاب‌های پرطرفدار** — دیتاست: [Goodreads Books (Kaggle)](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks). پاک‌سازی دادهٔ متنی، کوئری روی نویسنده‌ها و ناشران و ساخت فهرست پیشنهادی. _یک راهنمای کتاب‌خوانی داده‌محور برای هر سلیقه._

---

## مرحله ۲ — مبانی یادگیری ماشین
انتخاب مدل درست و ارزیابی صادقانه — مهارتی که از حفظ کردن الگوریتم‌ها مهم‌تر است.

### سرفصل‌ها
- یادگیری با نظارت و بدون نظارت
- Classification، Regression و Clustering
- Feature Engineering
- Cross-Validation و Bias-Variance

### نکات مهم یادگیری
- حفظ الگوریتم مهم نیست؛ مهم انتخاب مدل و ارزیابی درست است.
- همیشه با یک baseline ساده شروع کنید.
- مراقب Data Leakage باشید؛ Pipeline در scikit-learn بهترین همراه شماست.

### پروژه‌ها
1. **پیش‌بینی قیمت مسکن** — دیتاست: [California Housing (Kaggle)](https://www.kaggle.com/datasets/camnugent/california-housing-prices). Regression و Feature Engineering، مقایسهٔ Linear با Gradient Boosting و توضیح‌پذیری با SHAP. _تخمین منصفانهٔ قیمت خانه و فهم اینکه چه عواملی قیمت را بالا می‌برند._
2. **تشخیص پیامک و ایمیل اسپم** — دیتاست: [SMS Spam Collection (UCI)](https://archive.ics.uci.edu/dataset/228/sms+spam+collection). TF-IDF + Logistic Regression و تحلیل Precision / Recall. _فیلتری که هر روز وقت و اعصاب آدم‌ها را نجات می‌دهد._
3. **پیش‌بینی ریزش مشتری (Churn)** — دیتاست: [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn). Classification روی دادهٔ نامتوازن و انتخاب آستانه بر اساس هزینهٔ کسب‌وکار. _به هر کسب‌وکار کوچکی کمک می‌کند مشتری‌اش را قبل از رفتن نگه دارد._
4. **پیش‌بینی بیماری قلبی** — دیتاست: [Heart Disease (UCI)](https://archive.ics.uci.edu/dataset/45/heart+disease). Cross-Validation، مقایسهٔ مدل‌ها و شرح محدودیت‌های مدل‌های پزشکی. _تمرین مسئولانه روی یک مسئلهٔ حساس سلامت، با تأکید بر محدودیت‌ها._
5. **بخش‌بندی مشتریان فروشگاه** — دیتاست: [Online Retail II (UCI)](https://archive.ics.uci.edu/dataset/502/online+retail+ii). تحلیل RFM + K-Means و تفسیر خوشه‌ها برای بازاریابی. _فروشگاه‌ها پیشنهاد درست را به مشتری درست می‌دهند، نه به همه._
6. **پیش‌بینی تقاضای دوچرخهٔ اشتراکی** — دیتاست: [Bike Sharing (UCI)](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset). Regression با ویژگی‌های زمانی و آب‌وهوایی و ارزیابی روی بازهٔ زمانی جدا. _کمک به برنامه‌ریزی حمل‌ونقل شهری پاک‌تر._
7. **تشخیص تراکنش جعلی** — دیتاست: [Credit Card Fraud (Kaggle)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). کار با دادهٔ به‌شدت نامتوازن، معیار PR-AUC و مقایسهٔ Undersampling و class weight. _محافظت از پول مردم در برابر کلاهبرداری._
8. **پیش‌بینی عملکرد محصول کشاورزی** — دیتاست: [Crop Yield Prediction (Kaggle)](https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset). Regression با دادهٔ بارش، دما و سم و تحلیل اهمیت ویژگی‌ها. _به کشاورز و برنامه‌ریز امنیت غذایی تصویر بهتری از برداشت آینده می‌دهد._
9. **سیستم پیشنهاد فیلم** — دیتاست: [MovieLens](https://grouplens.org/datasets/movielens/). Collaborative Filtering با Matrix Factorization و ارزیابی با RMSE و Precision@K. _همان چیزی که هر روز در اپ‌ها می‌بینیم، این بار ساخت خودت._
10. **پیش‌بینی لغو رزرو هتل** — دیتاست: [Hotel Booking Demand (Kaggle)](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand). Classification، جلوگیری از Data Leakage و تفسیر مدل برای مدیر هتل. _هتل‌های کوچک ظرفیتشان را بهتر مدیریت می‌کنند و ضرر نمی‌کنند._

---

## مرحله ۳ — یادگیری عمیق
شبکه‌های عصبی از درون: از Backpropagation تا Transformer، با PyTorch.

### سرفصل‌ها
- شبکه‌های عصبی و Backpropagation
- CNN و Embedding
- مدل‌های ترتیبی
- Transformerها و کار با PyTorch

### نکات مهم یادگیری
- یک بار training loop را دستی در PyTorch بنویسید.
- پیش از آموزش از صفر، Transfer Learning را امتحان کنید.
- منحنی loss را بخوانید و overfitting را با چشم تشخیص دهید.

### پروژه‌ها
1. **تشخیص بیماری برگ گیاهان** — دیتاست: [PlantVillage (Kaggle)](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset). Transfer Learning با ResNet / EfficientNet، دموی Gradio و سرویس FastAPI. _کشاورز با یک عکس موبایل بیماری محصولش را زودتر می‌فهمد._
2. **دسته‌بندی پسماند برای بازیافت** — دیتاست: [TrashNet](https://github.com/garythung/trashnet). CNN با Data Augmentation و آزمون روی عکس موبایل. _تفکیک درست زباله از مبدأ، ساده‌تر از همیشه._
3. **تحلیل احساسات نظرات کاربران** — دیتاست: [IMDB Reviews](https://ai.stanford.edu/~amaas/data/sentiment/). مقایسهٔ LSTM با یک Transformer کوچک (DistilBERT). _کسب‌وکارها می‌فهمند مشتری‌ها واقعاً دربارهٔ آن‌ها چه حسی دارند._
4. **پیش‌بینی مصرف برق خانگی** — دیتاست: [Household Electric Power Consumption (UCI)](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption). مدل‌های ترتیبی LSTM / GRU برای سری زمانی. _مدیریت مصرف و کاهش قبض برق خانواده‌ها._
5. **تشخیص احساس از چهره** — دیتاست: [FER-2013 (Kaggle)](https://www.kaggle.com/datasets/msambare/fer2013). CNN، ماتریس درهم‌ریختگی و بحث دربارهٔ سوگیری داده. _تمرین بینایی ماشین همراه با نگاه انتقادی به عدالت مدل._
6. **شمارش جای خالی پارکینگ** — دیتاست: [PKLot](https://web.inf.ufpr.br/vri/databases/parking-lot-database/). Classification تصویر هر جایگاه و اجرای آن روی عکس کامل پارکینگ. _پیدا کردن جای پارک بدون دور زدن بی‌پایان._
7. **تشخیص ارقام دست‌نویس فارسی** — دیتاست: [HODA Dataset](https://github.com/amir-saniyan/HodaDatasetReader). CNN از صفر در PyTorch و ساخت دموی نوشتن روی صفحه. _پایهٔ خواندن خودکار فرم‌ها و چک‌های فارسی._
8. **تشخیص فرمان صوتی** — دیتاست: [Speech Commands](https://www.tensorflow.org/datasets/catalog/speech_commands). تبدیل صدا به Spectrogram و طبقه‌بندی با CNN. _کنترل صوتی ساده برای وسایل خانه، مناسب افراد کم‌توان._
9. **تشخیص میوهٔ سالم از خراب** — دیتاست: [Fruits Fresh and Rotten (Kaggle)](https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification). Transfer Learning و تحلیل اشتباه‌های مدل با Grad-CAM. _کاهش ضایعات غذا در انبار و فروشگاه._
10. **تشخیص ذات‌الریه از عکس قفسهٔ سینه** — دیتاست: [Chest X-Ray Pneumonia (Kaggle)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia). CNN با دادهٔ نامتوازن، معیار Recall و نمایش ناحیهٔ تصمیم مدل. _تمرین روی یک مسئلهٔ واقعی پزشکی، با تأکید بر اینکه مدل جای پزشک نیست._

---

## مرحله ۴ — LLM و هوش مصنوعی مولد
به‌جای آموزش مدل زبانی از صفر، با مدل‌های آماده محصول بسازید.

### سرفصل‌ها
- Transformerها، Embedding، Token و Context Window
- Prompting و Structured Output
- Function Calling
- Fine-tuning

### نکات مهم یادگیری
- به‌جای آموزش LLM از صفر، با مدل‌های آماده محصول بسازید.
- خروجی ساختاریافته (JSON Schema / Pydantic) را همیشه اعتبارسنجی کنید.
- پیش از Fine-tuning مطمئن شوید Prompting و RAG کافی نیست.

### پروژه‌ها
1. **دستیار هوشمند اسناد** — دیتاست: [CUAD (قراردادها)](https://www.atticusprojectai.org/cuad). استخراج اطلاعات، پرسش و پاسخ و خروجی JSON. _خواندن قرارداد طولانی دیگر یک روز کامل وقت نمی‌گیرد._
2. **استخراج اطلاعات از فاکتور و رسید** — دیتاست: [CORD](https://github.com/clovaai/cord). LLM چندوجهی + Structured Output و خروجی CSV. _ثبت خودکار هزینه‌ها از عکس رسید، برای خانواده و کسب‌وکار کوچک._
3. **خلاصه‌ساز اخبار و مقالات** — دیتاست: [CNN/DailyMail (Hugging Face)](https://huggingface.co/datasets/abisee/cnn_dailymail). خلاصه‌سازی چندسطحی و ارزیابی با ROUGE. _خبر یک روز در دو دقیقه، بدون از دست دادن نکتهٔ مهم._
4. **دستیار سفر با Function Calling** — دیتاست: [Open-Meteo + OpenStreetMap](https://open-meteo.com). مدل ابزار آب‌وهوا و مکان را فراخوانی می‌کند و برنامهٔ سفر می‌سازد. _برنامهٔ سفری که آب‌وهوای واقعی را هم در نظر می‌گیرد._
5. **Fine-tune مدل کوچک برای نظرات فارسی** — دیتاست: [Persian sentiment datasets (Hugging Face)](https://huggingface.co/datasets?search=persian+sentiment). LoRA روی یک مدل کوچک و مقایسه با Prompting. _ابزار تحلیل نظر برای کسب‌وکارهای فارسی‌زبان._
6. **ساخت خودکار آزمون از متن درسی** — دیتاست: [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/). تولید سؤال چهارگزینه‌ای با Structured Output و سنجش کیفیت سؤال‌ها. _معلم‌ها و دانش‌آموزها از هر متنی آزمون تمرینی می‌سازند._
7. **ساده‌سازی متون پزشکی** — دیتاست: [MedQuAD](https://github.com/abachaa/MedQuAD). بازنویسی پاسخ‌های تخصصی به زبان ساده و سنجش خوانایی. _اطلاعات سلامت برای همه قابل فهم می‌شود._
8. **دستیار رزومه و تطبیق با آگهی شغلی** — دیتاست: [Resume Dataset (Kaggle)](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset). استخراج مهارت‌ها با Embedding و امتیاز تطبیق رزومه با آگهی. _کارجوها می‌فهمند رزومه‌شان برای کدام شغل مناسب‌تر است._
9. **دسته‌بندی و پیش‌نویس پاسخ ایمیل** — دیتاست: [Enron Email Dataset](https://www.cs.cmu.edu/~enron/). Classification با LLM و تولید پیش‌نویس پاسخ با لحن قابل تنظیم. _صندوق ایمیل شلوغ مرتب می‌شود و پاسخ‌ها سریع‌تر می‌روند._
10. **توصیف تصویر برای نابینایان** — دیتاست: [VizWiz Captioning](https://vizwiz.org/tasks-and-datasets/image-captioning/). مدل چندوجهی برای توصیف عکس و ارزیابی روی عکس‌های واقعی کاربران نابینا. _یک ابزار دسترس‌پذیری که مستقیماً زندگی آدم‌ها را ساده‌تر می‌کند._

---

## مرحله ۵ — RAG و AI Agentها
مدل را به دانش و ابزار وصل کنید: بازیابی، برنامه‌ریزی و حافظه.

### سرفصل‌ها
- RAG و Vector Database
- استراتژی‌های Retrieval
- Tool Use و چرخهٔ Agent
- Memory، Planning و Orchestration

### نکات مهم یادگیری
- کیفیت RAG بیشتر به chunking و retrieval بستگی دارد تا خود مدل.
- Hybrid Search (BM25 + Vector) و Reranking را امتحان کنید.
- Agent را ساده شروع کنید؛ هر ابزار اضافه یعنی احتمال خطای بیشتر.

### پروژه‌ها
1. **دستیار پرسش و پاسخ قوانین** — دیتاست: [GDPR Text](https://gdpr-info.eu). RAG همراه با ذکر منبع (citation). _هر کسی می‌تواند بپرسد قانون دقیقاً چه می‌گوید، با ارجاع به ماده._
2. **Agent پشتیبانی مشتری** — دیتاست: [Bitext Customer Support (Hugging Face)](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset). Agentic RAG + ابزار پیگیری سفارش آزمایشی. _پشتیبانی شبانه‌روزی برای کسب‌وکارهای کوچک._
3. **دستیار پژوهش مقالات علمی** — دیتاست: [arXiv API](https://info.arxiv.org/help/api/index.html). جست‌وجو، خلاصه و مقایسهٔ مقالات. _دانشجوها در چند دقیقه می‌فهمند کدام مقاله ارزش خواندن دارد._
4. **دستیار تغذیه و دستور پخت** — دیتاست: [USDA FoodData Central](https://fdc.nal.usda.gov). Agent با ابزار محاسبهٔ کالری و پیشنهاد غذا. _برنامهٔ غذایی ساده و دقیق برای هر خانواده._
5. **Agent تحلیل داده (Text-to-SQL)** — دیتاست: [Chinook Database](https://github.com/lerocha/chinook-database). پرسش فارسی یا انگلیسی ← SQL ← نمودار، همراه با حافظهٔ گفت‌وگو. _مدیرها بدون بلد بودن SQL از داده‌شان جواب می‌گیرند._
6. **دستیار مستندات برنامه‌نویسی** — دیتاست: [Python Documentation](https://docs.python.org/3/download.html). RAG روی مستندات با Hybrid Search و Reranking. _برنامه‌نویس تازه‌کار جواب دقیق را از منبع رسمی می‌گیرد، نه از حدس._
7. **Agent برنامه‌ریز سفر چندابزاره** — دیتاست: [OpenTripMap + Open-Meteo](https://opentripmap.io/product). Planning چندمرحله‌ای با چند ابزار و حافظهٔ ترجیحات کاربر. _یک برنامهٔ سفر کامل که خودش با شرایط تطبیق پیدا می‌کند._
8. **دستیار کشاورز** — دیتاست: [FAO Publications](https://www.fao.org/publications). RAG روی راهنماهای آفات و کوددهی با پاسخ به زبان ساده. _دانش تخصصی کشاورزی به دست کشاورز کوچک می‌رسد._
9. **دستیار بررسی تداخل دارو** — دیتاست: [openFDA API](https://open.fda.gov/apis/). Agent با ابزار جست‌وجوی دارو و هشدار ایمنی، با Guardrail پزشکی. _آگاهی بیشتر بیمار، همراه با ارجاع همیشگی به پزشک و داروساز._
10. **Agent مقایسهٔ قیمت و خرید** — دیتاست: [Amazon Products (Kaggle)](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset). Retrieval روی محصولات، مقایسهٔ ویژگی‌ها و توصیه با دلیل. _خرید آگاهانه‌تر بدون ساعت‌ها گشتن._

---

## مرحله ۶ — MCP، ارزیابی و استقرار
از نمونهٔ اولیه تا سرویس قابل اعتماد: امنیت، سنجش و پایش.

### سرفصل‌ها
- MCP و Tool Serverها
- Permission و احراز هویت
- Observability و Guardrails
- مدیریت خطا و Evaluation Dataset
- FastAPI، Docker و CI/CD
- Monitoring و بررسی تغییر عملکرد مدل

### نکات مهم یادگیری
- بدون Evaluation Dataset، بهبود فقط حدس است.
- Logging و Tracing را از ابتدا طراحی کنید، نه بعد از خرابی.
- اصل کمترین دسترسی (Least Privilege) را برای ابزارهای Agent رعایت کنید.

### پروژه‌ها
1. **MCP Server آب‌وهوا و کیفیت هوا** — دیتاست: [Open-Meteo + OpenAQ](https://open-meteo.com). سرور MCP با احراز هویت و rate limit. _دادهٔ محیطی معتبر در دسترس هر دستیار هوشمند._
2. **Production RAG با ارزیابی خودکار** — دیتاست: [HotpotQA](https://hotpotqa.github.io). سنجش faithfulness و relevance و گزارش خودکار در CI. _سیستمی که می‌شود به جواب‌هایش اعتماد کرد، با عدد._
3. **API تحلیل احساسات با Docker و Monitoring** — دیتاست: [Evidently](https://github.com/evidentlyai/evidently). FastAPI + Docker + GitHub Actions و تشخیص Data Drift. _مدلی که در دنیای واقعی کار می‌کند و وقتی خراب شد خبر می‌دهد._
4. **Agent ایمن با Guardrails** — دیتاست: [garak (LLM scanner)](https://github.com/NVIDIA/garak). آزمون Prompt Injection، فیلتر PII و لاگ کامل تصمیم‌ها. _حفاظت از دادهٔ کاربران در برابر سوءاستفاده._
5. **سامانهٔ پایش هوشمند مزرعه و گلخانه** — دیتاست: [Greenhouse sensor datasets (Kaggle)](https://www.kaggle.com/search?q=greenhouse+sensor). مدل پیش‌بینی + Agent هشدار + MCP + داشبورد پایش در Production. _کشاورزی دقیق‌تر با مصرف کمتر آب و انرژی._
6. **داشبورد Observability برای LLM** — دیتاست: [Langfuse](https://langfuse.com). Tracing هر درخواست، هزینه، تأخیر و کیفیت پاسخ در یک داشبورد. _می‌فهمی سیستم هوشمندت کجا کند، گران یا اشتباه است._
7. **مجموعهٔ آزمون رگرسیون برای Prompt** — دیتاست: [MT-Bench (Hugging Face)](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments). Evaluation Dataset، LLM-as-judge و A/B تست Prompt در CI. _هر تغییر کوچک، کیفیت پاسخ کاربران را خراب نمی‌کند._
8. **استقرار مدل روی Kubernetes** — دیتاست: [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/). Deployment، Autoscaling و Health Check برای مدل مرحلهٔ ۲. _سرویسی که با زیاد شدن کاربر از کار نمی‌افتد._
9. **MCP Server تقویم شخصی با OAuth** — دیتاست: [Google Calendar API](https://developers.google.com/calendar/api). OAuth، Permission سطح‌بندی‌شده و ابزارهای خواندن و نوشتن رویداد. _دستیار هوشمند به تقویمت دسترسی دارد، ولی فقط همان‌قدر که اجازه داده‌ای._
10. **Pipeline بازآموزی خودکار مدل** — دیتاست: [Apache Airflow](https://airflow.apache.org). زمان‌بندی بازآموزی، مقایسه با مدل فعلی و استقرار فقط در صورت بهبود. _مدلی که با تغییر دنیا کهنه نمی‌شود._
