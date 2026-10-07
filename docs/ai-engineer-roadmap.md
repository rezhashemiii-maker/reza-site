# مسیر یادگیری مهندس هوش مصنوعی (AI Engineer Roadmap)
**رضا هاشمی** — شش مرحله، سی پروژهٔ کاربردی با دیتاست‌های عمومی

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
1. **داشبورد قیمت مواد غذایی و تورم** — دیتاست: FAO Food Price Index / World Bank Commodity Prices. پاک‌سازی با Pandas، ذخیره در SQLite، کوئری روند ماهانه و داشبورد Streamlit.
2. **تحلیل کیفیت هوای شهرها** — دیتاست: OpenAQ API. دریافت داده از API، ذخیره در SQL، گزارش روزهای آلوده و مقایسهٔ شهرها.
3. **تحلیل تأخیر پروازها** — دیتاست: US DOT Flight Delays (Kaggle). پاک‌سازی دادهٔ حجیم و کوئری‌های SQL برای یافتن بدترین فرودگاه، ساعت و ایرلاین.
4. **ردیاب مخارج شخصی (CLI + SQLite)** — دیتاست: Personal Finance dataset (Kaggle). اپ خط فرمان مبتنی بر Classes، دسته‌بندی خودکار هزینه‌ها و گزارش ماهانه.
5. **کاوش داده‌های زلزله** — دیتاست: USGS Earthquake API. دریافت زندهٔ داده، نقشهٔ تعاملی و آمار فراوانی و شدت به تفکیک منطقه.

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
1. **پیش‌بینی قیمت مسکن** — دیتاست: California Housing / Ames Housing. Regression و Feature Engineering، مقایسهٔ Linear با Gradient Boosting و توضیح‌پذیری با SHAP.
2. **تشخیص پیامک و ایمیل اسپم** — دیتاست: SMS Spam Collection (UCI). TF-IDF + Logistic Regression و تحلیل Precision / Recall.
3. **پیش‌بینی ریزش مشتری (Churn)** — دیتاست: Telco Customer Churn (Kaggle). Classification روی دادهٔ نامتوازن و انتخاب آستانه بر اساس هزینهٔ کسب‌وکار.
4. **پیش‌بینی بیماری قلبی** — دیتاست: Heart Disease (UCI). Cross-Validation، مقایسهٔ مدل‌ها و شرح محدودیت‌های مدل‌های پزشکی.
5. **بخش‌بندی مشتریان فروشگاه** — دیتاست: Online Retail II (UCI). تحلیل RFM + K-Means و تفسیر خوشه‌ها برای بازاریابی.

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
1. **تشخیص بیماری برگ گیاهان** — دیتاست: PlantVillage. Transfer Learning با ResNet / EfficientNet، دموی Gradio و سرویس FastAPI.
2. **دسته‌بندی پسماند برای بازیافت** — دیتاست: TrashNet / Garbage Classification (Kaggle). CNN با Data Augmentation و آزمون روی عکس موبایل.
3. **تحلیل احساسات نظرات کاربران** — دیتاست: IMDB / Amazon Reviews. مقایسهٔ LSTM با یک Transformer کوچک (DistilBERT).
4. **پیش‌بینی مصرف برق خانگی** — دیتاست: Household Electric Power Consumption (UCI). مدل‌های ترتیبی LSTM / GRU برای سری زمانی.
5. **تشخیص احساس از چهره** — دیتاست: FER-2013. CNN، ماتریس درهم‌ریختگی و بحث دربارهٔ سوگیری داده.

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
1. **دستیار هوشمند اسناد** — دیتاست: CUAD (قراردادها) یا اسناد عمومی دولتی. استخراج اطلاعات، پرسش و پاسخ و خروجی JSON.
2. **استخراج اطلاعات از فاکتور و رسید** — دیتاست: SROIE / CORD. LLM چندوجهی + Structured Output و خروجی CSV.
3. **خلاصه‌ساز اخبار و مقالات** — دیتاست: CNN/DailyMail یا arXiv Abstracts. خلاصه‌سازی چندسطحی و ارزیابی با ROUGE.
4. **دستیار سفر با Function Calling** — دیتاست: Open-Meteo API + OpenStreetMap. مدل ابزار آب‌وهوا و مکان را فراخوانی می‌کند و برنامهٔ سفر می‌سازد.
5. **Fine-tune مدل کوچک برای نظرات فارسی** — دیتاست: Digikala / SnappFood Comments (Hugging Face). LoRA روی یک مدل کوچک و مقایسه با Prompting.

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
1. **دستیار پرسش و پاسخ قوانین و آیین‌نامه‌ها** — دیتاست: متون عمومی قانون کار / GDPR. RAG همراه با ذکر منبع (citation).
2. **Agent پشتیبانی مشتری** — دیتاست: Bitext Customer Support (Hugging Face). Agentic RAG + ابزار پیگیری سفارش آزمایشی.
3. **دستیار پژوهش مقالات علمی** — دیتاست: arXiv API / Semantic Scholar. جست‌وجو، خلاصه و مقایسهٔ مقالات.
4. **دستیار تغذیه و دستور پخت** — دیتاست: USDA FoodData Central + RecipeNLG. Agent با ابزار محاسبهٔ کالری و پیشنهاد غذا.
5. **Agent تحلیل داده (Text-to-SQL)** — دیتاست: Chinook / Northwind DB. پرسش فارسی یا انگلیسی ← SQL ← نمودار، همراه با حافظهٔ گفت‌وگو.

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
1. **MCP Server داده‌های آب‌وهوا و کیفیت هوا** — دیتاست: Open-Meteo + OpenAQ. سرور MCP با احراز هویت و rate limit.
2. **Production RAG با ارزیابی خودکار** — دیتاست: SQuAD / HotpotQA به‌عنوان eval set. سنجش faithfulness و relevance و گزارش خودکار در CI.
3. **API تحلیل احساسات با Docker و Monitoring** — دیتاست: مدل مرحلهٔ ۳. FastAPI + Docker + GitHub Actions و تشخیص Data Drift با Evidently.
4. **Agent ایمن با Guardrails** — دیتاست: ابزارهای SQL و ایمیل آزمایشی. آزمون Prompt Injection، فیلتر PII و لاگ کامل تصمیم‌ها.
5. **سامانهٔ پایش هوشمند مزرعه و گلخانه** — دیتاست: Smart Agriculture / Greenhouse sensor datasets (Kaggle). مدل پیش‌بینی + Agent هشدار + MCP + داشبورد پایش در Production.

---

## چک‌لیست هر پروژه برای رزومه
- [ ] README با مسئله، داده، روش، نتیجه و تصویر/GIF دمو
- [ ] دموی آنلاین (Hugging Face Spaces / Streamlit Cloud)
- [ ] معیار ارزیابی مشخص و مقایسه با baseline
- [ ] کد ماژولار + تست ساده
- [ ] بخش «محدودیت‌ها و قدم‌های بعدی»
