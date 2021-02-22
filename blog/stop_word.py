import string

import hazm
from bs4 import BeautifulSoup
from hazm import Stemmer, Normalizer

PersianStopWord = ['هایی', '', 'بازی کنان', 'بیش', 'شدی', 'گيري', 'شش  نداشته', 'کس', 'بکن', 'لطفاً', 'باشیم', 'اش',
                   'کاملاً', 'پاعینِ',
                   'به کرات', 'اين', 'اما', 'بالاخره', 'افسوس', 'چه بسا', 'اغلب', 'صرفا', 'یافتن', 'میکنند', 'کم',
                   'نکنی', 'تان',
                   'نهایتا', 'گویم', 'زود', 'آنجا', ',', 'خواستم', 'در کنار', 'زیاده', 'ملیون', 'وقتی', 'درسته', 'ديده',
                   'دوباره',
                   'ثانیاً', 'بعید', 'مجانی', 'نکنیم', 'گفتن', 'گردند', 'بطور', 'جمعی', 'چو', 'به ناچار', 'بیشتری',
                   'پیشتر', 'نخواهی',
                   'بگوید', 'بیایید', 'دیروز', 'گذاری', 'گرفتن', 'زیرچشمی', 'حدودِ', 'سر', 'واما', 'به خوبی', 'برایم',
                   'كسي', 'بیا',
                   'احتمالا', 'تر  براساس', 'ناامید', 'این قدر', 'بهت', 'ممیزیهاست', 'خويش', 'اگر چه', 'براساس', 'سوی',
                   'بی تفاوتند',
                   'شدیدا', 'اگرچه', 'زير', '[', 'چند', 'اگر', 'یابیم', 'دم', 'علیه', 'صد', 'خویش', 'جلو', 'كنند',
                   'این', 'میکنم',
                   'امروزه', 'هر چند', 'آخرها', 'شان', 'بارها', 'برابرِ', 'ف', 'میان', 'مگر این که', 'چکار', 'حتماً',
                   'آنانی', 'زمان',
                   'خود به خود', 'یافتیم', 'علیرغم', 'می\u200cکنیم', 'توانسته', 'نداشتی', 'تماما', 'یا', 'طبیعتا',
                   'تویِ', 'کردی',
                   'شناسی', 'بجز', 'نام', 'مشت', 'دراین میان', 'داشت', 'ل', 'می\u200cداند', 'انجام', 'بهترين',
                   'بااین حال', 'برای', 'ز',
                   'مذهبی اند', 'ثانیا', 'پیش', 'بیایند', 'بخواهیم', 'دریغا', 'كل', 'مجدداً', 'يكديگر', 'تمام قد',
                   'اینجا', 'ناخواسته',
                   'به شان', 'هست', 'عمدتا', '۷', 'همانا', 'حتي', 'آخه', 'می\u200cرسد', 'مخصوصاً', 'و لا غیر',
                   'نمی\u200cکند', 'کنار',
                   'ضدِّ', 'داد', 'گویید', 'مجموعاً', 'حتی', 'عجولانه', 'جديد', 'بخواهند', 'بتواند', 'وجود', 'باشی',
                   'یاب', 'آيد', 'اوست',
                   'وسطِ', 'تاکنون', 'تند تند', 'رفتارهاست', 'واقعاً', 'مکرر', 'درصورتی که', 'یکریز', 'پاره\u200cای',
                   'درحالیکه', 'ایند',
                   'بهترین', 'اینگونه', 'ج', 'نزدیکِ', 'اینها', 'آسیب پذیرند', 'تواند', 'متاسفانه', 'حاضر', 'جريان',
                   'وای', 'ناگاه',
                   'بگیرد', 'حال', 'هوی', 'بهش', 'روز به روز', 'داری', 'قانوناً', 'صرفاً', 'چاپلوسانه', 'مورد', 'خدمات',
                   'هر چه', 'چ',
                   'پروردگارا', 'مطمینا', '«', 'باز هم', 'روزه ایم', 'چرا', 'جلوگيري', 'نه', 'گیریم', 'روي', 'ط',
                   'سالانه', '۴', 'برعکس',
                   'گیرند', 'پهن شده', 'وی', 'بيست', 'يكي', 'حاضرم', 'لطفا', 'انتها', 'نیازمندند', 'عملا', 'روزانه',
                   'می\u200cکنند', 'گو',
                   'به قدری', 'دیوانه\u200cای', 'ا', 'بسیاری', 'ايم', 'ان شاأالله', 'بسی', 'حکماً', 'دامم', 'کَی',
                   'طبعاً', 'توان', 'دهد',
                   'بعداً', 'ناگزیر', 'یافتی', 'هاي', 'نگو', 'چیزی', 'خودشان', 'زشتکارانند', 'هق هق کنان', 'بطوری که',
                   'بالطبع', 'شد',
                   'نوعی', 'ح', 'عمدا', 'اینطور', '$', 'و', 'کند', 'بکنید', 'جايي', 'منتهی', 'به هرحال', 'بگیرید', '٪',
                   'گوی', 'این جوری',
                   'بکنیم', 'تریلیون', 'غالبا', 'خوب', 'قاالند', 'سه باره', 'بودید', 'شوند', 'طرف', 'احیاناً', 'دنبالِ',
                   'زنند', 'گروهي',
                   'لزوماً', 'گویند', 'برابر', 'ساخته', ':', 'بالایِ', 'هیچکدام', 'توؤماً', 'آباد', 'سراسر', 'مشترکاً',
                   'شوم', 'ولی',
                   'خودمان', 'قدری', 'گفتید', 'آری', 'هستيم', 'طی', 'رفت', 'کی', 'رشته', 'ش', 'تمام', 'مسلما', 'شاهدند',
                   'وضع', 'را',
                   'جناح', 'به علاوه', 'ی', 'وقتي', 'توانستند', 'گذاري', 'دا', 'ناشی', 'جدا', 'هستیم', 'بیشتر', 'درین',
                   'می\u200cکنم',
                   'ظاهراً', '.', 'باد', 'ک', 'وگو', 'همه ساله', 'فعلا', 'دیگر', 'ایا', 'بخصوص', 'داشتم', '؛', 'ن',
                   'تک تک', 'گوید',
                   'لاجرم', 'هرچه', 'تولِ', 'سازی', 'دهند', 'مدّتی', 'خواهیم', 'علی رغم', 'بروز', 'بسوی', 'ای', 'امسال',
                   'آنها', 'گرفتیم',
                   'کنند', 'عمده', 'بگو', 'باید', 'کاش', 'دایما', 'دادید', 'در کل', 'گذاشته', '/', 'آنكه', 'سریعا',
                   'دیگه', 'حول',
                   'برداری', 'ندارید', 'نداشتم', 'اساساً', '»', 'بخواه', 'مدتهاست', 'اكنون', 'هنگامی', 'کننده', 'سازي',
                   'مع ذلک', 'طبعا',
                   'دادم', 'چطور', 'شخصا', 'دایم', 'آیا', 'چنين', 'تمامشان', 'قصدِ', 'صندوق هاست', 'توانستم', 'بگوییم',
                   'نوعي', 'گوییم',
                   'حالا', 'رنجند', 'نبود', 'می\u200cرود', 'دیر', 'پشت', 'ت', 'خواه', 'خیره', 'همچنان که', 'شدید',
                   'كردم', 'بخواهم',
                   'مطمانا', 'نماید', 'به مراتب', 'میکنی', 'دقیقا', 'بخش', 'گویا', 'به ویژه', 'بیابد', 'مستحضرید',
                   'آورده', 'پس فردا',
                   'تو', 'علاوه بر آن', 'ندارند', 'حقیرانه', 'ازاین رو', 'مع الاسف', 'بروشنی', 'امیدوارند', 'وي', 'بی',
                   'کرد', 'گفتند',
                   'باشيم', 'خوش', 'مدت', 'چندین', 'گرفتی', 'توسط', 'شویم', 'بیرونِ', 'یک کمی', 'حق', 'آره', 'بخشی',
                   'بودند', 'آسان',
                   'کل', 'نخواهند', '۱', 'باوجودی که', 'دیگری', 'فوق', 'فردا', 'روزهاي', 'درباره', 'توانی', 'نباید',
                   'این گونه', 'خواهند',
                   'سوم', 'خود', 'خب', 'آخر', 'مرسی', 'کنونی', 'معدود', 'نداریم', 'گفت', 'درعین حال', 'همیشه', 'بس',
                   'قبلند', 'گفته',
                   'ایشان', 'جز', 'شوقم', 'هنگامی که', 'خداست', 'گویی', 'روب', 'دیوی', 'بعضی\u200cها', 'به وضوح',
                   'سرانجام', 'یارب',
                   'چنان', 'هبچ', 'ماست', 'وحشت زده', 'زیرِ', 'دادن', 'همين', 'اصلاً', 'بيش', 'توانیم', 'هم', 'سپس',
                   'ص', 'داراست',
                   'نموده', 'نبايد', 'مستقیما', 'كند', 'بودم', 'واقعی', 'ق', 'بیاورم', 'ضمناً', 'غیرقانونی', 'بگیرند',
                   'بعدا', 'بلافاصله',
                   'عنوان', 'فقط', 'حداکثر', 'تعمدا', 'بالای', 'ویا', 'کنم', 'شدم', 'نوع', 'چیز', 'دانند', 'ندارم',
                   'كردند', 'دادند',
                   'صورت', 'سعی', 'اشکارا', 'زیر', 'یقیناً', 'من', 'چگونه', 'رسید', 'نیز', 'بدین ترتیب', 'پرسان',
                   'خواستند', 'ّه', 'بسا',
                   'همان طور که', 'مثلِ', 'معتقدم', 'ميليون', 'بگویید', 'نيست', 'ديگران', 'جا', 'مجموعا', 'پی درپی',
                   'روش', 'بزودی',
                   'بگیریم', 'شش', 'یه', 'كمتر', 'راه', 'ريزي', 'اند', 'نداشته', 'توانست', '-', 'یابد', 'گرفت',
                   'بخواهد', 'ظ', 'چه طور',
                   'ث', 'خواستی', 'مختلف', 'تاكنون', 'ملیارد', 'روبروست', 'بکنی', 'مفیدند', 'نیستند', 'سری', 'خودتو',
                   'هنگامِ', 'گرفتید',
                   'دادیم', 'عموم', 'بدهید', 'معذوریم', 'نظیر', 'گردد', 'کنید', 'اولین', 'اون', 'عمدتاً', 'چرا که',
                   'اکثر', 'ديروز', 'م',
                   'کردم', 'نشده', 'حسابگرانه', 'اتفاقا', 'عمداً', 'میکنیم', 'مي', 'ایم', 'ذاتاً', 'محکم', 'همگی',
                   'هیچ گاه', 'پيش',
                   'بعضی شان', 'قطعا', 'نزديك', 'گونه', 'پیشِ', 'دیگران', 'موقتا', 'شیک', 'قدر', 'بله', 'نزدیک', 'ب',
                   'شماری', 'فكر',
                   'نکرده', 'بايد', 'متفاوتند', 'در باره', 'بسياري', 'همچنين', 'لذا', 'رواست', 'مبادا', 'بگویی',
                   'مطمانم', 'نوعاً',
                   'به طوری که', 'باز', 'خوشبختانه', 'آنطور', 'نخستين', 'آهان', 'سراپا', 'اجراست', 'بیاییم',
                   'درست و حسابی', 'مغرضانه',
                   'زهی', 'س', 'دارند', 'بیرون', 'برایمان', 'دهم', 'خودتان', 'تمامي', 'صددرصد', 'گويد', 'آخ', 'کو',
                   'نخودی', 'بعد',
                   'يابد', 'اری', 'آمدن', 'عمل', 'الی', 'به راستی', 'به سرعت', 'آزادانه', 'معتقدیم', 'همچنان', 'كردن',
                   'جلوگیری', 'کسانی',
                   'بدون', 'به تمامی', 'ها', 'همه\u200cاش', 'آقایان', 'دارید', 'پشیمونی', 'يا', 'مردانه', 'بوده',
                   'یواش یواش',
                   'تر براساس', 'نهایتاً', 'شبهاست', 'برایشان', 'چی', 'نمی\u200cشود', '\ufeffو', 'باشد', 'ساکنند',
                   'استفاد', 'بی آنکه',
                   'الان', 'بعضي', 'داشتی', 'عملاً', 'خواهم', 'گیرم', 'شونده', 'تقریباً', 'هیچ', 'چه', 'سالته', 'چته',
                   '۳', 'یابی',
                   'راستی', 'هفت', 'عموما', 'جمعا', 'اینکه', '؟', 'نمی', 'اکثراً', '۶', 'ناگهانی', 'بتوانی', 'یعنی',
                   'در ثانی', 'لب',
                   'دار', 'براحتی', 'بتوانیم', 'بماند', 'گیرید', 'به جز', 'درواقع', 'هیچی', 'شاید', 'اخیر', 'ناگهان',
                   'می\u200cشود',
                   'دهید', 'طور', 'د', 'خصوصاً', 'واقفند', 'كنيد', 'بیایی', 'اینقدر', 'ديگري', 'هرکس', 'لیکن', 'دیشب',
                   'انطور', 'در واقع',
                   'مکرراً', 'خارجِ', 'رسما', 'قاعدتاً', 'دهی', 'روزهای', 'تحریم هاست', 'رویِ', 'تمامی', 'یافته',
                   'همدیگر', 'قبل', 'حتما',
                   'ام', 'زمینه', 'برآنند', 'ناشي', 'آنقدر', 'اولاً', 'راست', 'علّتِ', 'كرده', 'ضمن', 'درحالی که',
                   'معمولا', 'جدید', 'ع',
                   'داریم', 'نیمی', 'نخواهم', 'چت', 'دیرم', 'سهواً', '#', 'آرام', 'به هیچ وجه', 'بسيار',
                   'حاشیه\u200cای', 'خویشتنم',
                   'برخوردارند', 'اخیراً', 'یک کم', 'شناسي', 'کماکان', 'نخستین', 'ذ', 'خصوصا', 'گفتی', 'دوم', 'آشکارا',
                   'بتدریج', 'گيرد',
                   'زودتر', 'بسختی', 'بيشتري', 'تحت', 'عقبِ', 'بگذاریم', 'برا', 'خودمو', 'نداشتیم', 'آمرانه', 'حاکیست',
                   'مقصرند', 'ان',
                   'رویش', 'ساده اند', 'بعضا', 'بتوان', 'پی', 'سریع', 'محتاجند', 'معمولاً', 'نداشتند', 'داريم',
                   'باورند', 'اشتباها',
                   'قضایاست', 'داشتن', 'جدیدا', 'بودیم', 'رو', 'بین', 'بدانها', 'شده', 'کدام', 'گرچه', 'کمتری', 'برایت',
                   'میکند', 'نظير',
                   'پنج', 'فعلاً', 'کنون', 'تریلیارد', 'گاه', 'سخته', 'نیستیم', 'ندارد', 'بالاخص', 'کمتر', 'سایر',
                   'انقدر', 'کنیم',
                   'جرمزاست', 'میزان', 'مردم', 'کردن', 'کامل', 'یکدیگر', 'بدینجا', 'کنارش', 'متؤسفانه', 'انشاالله',
                   'ریزی', '۵',
                   'عملی اند', 'بعری', 'یکسال', 'یافتید', 'امیدواریم', 'سیخ', 'بویژه', 'بين', 'خواستیم', 'هر', 'عجب',
                   'چندان', 'خیاه',
                   'وگرنه', 'قابل', 'گیرد', 'خواسته', '(', 'دانست', 'اي', 'ممکن', 'كنيم', ')', 'به زودی', 'نیست',
                   'کنایه\u200cای', 'الا',
                   '۲', 'کما\x7fاینکه', 'کنی', 'قطعاً', 'آمده', 'چيزي', 'بیاورند', 'داشتند', 'همچین', 'تعدادی',
                   'داشتیم', 'کاملا',
                   'وابسته اند', 'نخواهد', 'كه', 'روز', 'امشب', 'همین که', 'خواهید', 'برایش', 'اثرِ', 'نزدِ', 'ايشان',
                   'گاهی', 'روزه ست',
                   'اينكه', 'راحت', 'شايد', 'توانند', 'برایِ', 'اینو', 'خودش', 'یابم', 'شوید', 'بیاورد', 'چند روزه',
                   'شدیداً', 'به درشتی',
                   'داشته', 'آن گاه', 'هستید', 'به روشنی', 'سریِ', 'به تازگی', 'انگار', 'آید', 'گرفتم', 'سوي', 'آهای',
                   'فکر', 'اکثریت',
                   'تر', 'بعد از این که', 'آرام آرام', 'زياد', 'کمتره', 'انچنان', '…', 'بی اطلاعند', 'میلیارد',
                   'دشمنیم', 'مرتب',
                   'پدرانه', 'آنگاه', 'نکنید', 'جداگانه', 'به', 'چنانکه', 'بهتر', 'منطقی', 'همین', 'تقریبا', 'شو',
                   'گرفتارند', 'خواهد',
                   'بیاوریم', 'اساسا', 'مانند', 'هیچکس', 'قبلاً', 'اقلیت', 'هرگاه', 'آنکه', 'عموماً', 'آنچه', 'كرد',
                   'جلویِ', 'ژ',
                   'اینچنین', 'طريق', 'انصافا', 'رفته', 'با', 'اندکی', 'نكرده', 'آن', 'بگویند', 'اگه', 'آقای', 'هرچند',
                   'بخشه', 'همچون',
                   'کنارِ', 'شاهدیم', 'چیزیست', 'خواهيم', 'جنابعالی', 'مگو', 'معلومه', 'بي', 'بشدت', 'پارسال', '۸',
                   'های', 'همزمان',
                   'وقتی که', 'اینجاست', 'سالهاست', 'طبقِ', 'جهت', 'به تدریج', 'حضرتعالی', 'خواستن', 'یابند', 'سویِ',
                   'شیرینه', 'از جمله',
                   'عنقریب', 'کلی', 'یافت', 'دو', 'اصولا', 'مجبورند', 'بعدها', 'روزه\u200cای', 'عرفانی', 'خلاصه',
                   'بیابیم', 'خواهی',
                   'بلكه', 'مخالفند', 'عاجزانه', 'خواست', 'آورد', 'بالعکس', 'بازهم', 'پریروز', 'همانها', 'جلوی',
                   'عاقبت', 'جاي',
                   'عبارتند', 'كنم', 'است', 'قاطبه', 'شدن', 'راجع به', 'بعضی', 'شخصاً', 'هزار', 'ازجمله', 'اید', 'روی',
                   'تلویحا', 'بيشتر',
                   'داشتید', 'علاوه بر', 'ترين', 'خالصانه', 'دارم', 'معتقدند', 'مثل', 'شدند', ']', 'خیلی', 'خودبه خودی',
                   'شود', 'بار',
                   'بعلاوه', 'به جای', 'مثلا', 'توانستن', 'فلذا', 'رسیده', 'چهار', 'نشان', 'اعلام', 'بکنند', 'برخوردار',
                   'گرفتند',
                   'بالاست', 'کاشکی', 'مگر', 'نکن', 'طلبکارانه', 'تلویحاً', 'اینهاست', 'گروهی', 'طي', 'دااما',
                   'بااین وجود', 'گفتیم',
                   'یقینا', 'ه', 'فاقد', 'نسبتا', 'بیاب', 'حدود', 'امیدوارم', 'داده', '،', 'غ', 'مان', 'البتّه',
                   'پایین ترند', 'همهٌ',
                   'ض', '*', 'ثالثاً', 'آی', '۹', 'بدانجا', 'پیشاپیش', 'اصلا', 'بیابید', 'رهگشاست', 'ناراضی اند',
                   'حدودا', 'شما', 'نمي',
                   'همه', 'فر', 'مقصری', 'نمايد', 'بیاور', 'ویژه', 'خودم', 'ديگر', '۰', 'جنس اند', 'محکم\u200cتر', 'گه',
                   'مقابل', 'دریغ',
                   'مقدار', 'جور', 'توانستیم', 'یک', 'گذشته', 'تازه', 'سریعاً', 'کسی', 'همگان', 'به گرمی',
                   'می\u200cتواند', 'همه شان',
                   'متعاقبا', 'ده', 'برنامه سازهاست', 'اکنون', 'آدمهاست', 'سالم\u200cتر', 'یافتم', 'همه روزه', 'گفتم',
                   'تصریحاً', 'جداً',
                   'بی تردید', 'اینک', 'دادی', 'شوراست', 'جایی', 'توانید', 'مشغولند', 'انکه', 'پیدا', 'چقدر', 'مادامی',
                   'کردند',
                   'از آن پس', 'درون', 'بیاید', 'علی الظاهر', 'شماست', 'مانندِ', 'به سادگی', 'بپا', 'موجودند', 'می',
                   'توانستی', 'نکنند',
                   'آنچنان', 'داام', 'توانم', 'باره', 'گهگاه', 'به رغم', 'اسلامی اند', 'حقیقتا', 'آور', 'برخی', 'نداشت',
                   'به طور کلی',
                   '!', 'گويند', 'حداقل', 'هنوز', 'بگیر', 'همان', 'بودن', 'بازیگوشانه', 'گرفته', 'خداحافظ',
                   'پشتوانه اند', 'آنرا',
                   'پیوسته', 'ما', 'بفهمی نفهمی', 'بخوبی', 'شش نداشته', 'هیچگونه', 'کتبا', 'احتراما', 'معمولی', 'بیابم',
                   'اولا', 'چنده',
                   'توی', 'همان گونه که', 'غير', 'نزد', 'کلا', 'شوی', 'بعدازظهر', 'خویشتن', 'نخواهیم', 'در بارهٌ',
                   'دارد', 'داخل',
                   'بخواهید', 'بیگمان', 'درمجموع', 'یک جوری', 'نه تنها', 'امور', 'از', 'وقتیکه', 'بود', 'در نهایت',
                   'بی هدف', 'بلکه',
                   'کارند', 'راسا', 'فبها', 'زيرا', 'طریق', 'شمایند', 'نبش', 'زیاد', 'هم اینک', 'باشم', 'بارة', 'پس',
                   'یکی', 'منی',
                   'آیند', 'عدم', 'بیاورید', 'عقب', 'استفاده', 'خودت', 'ميليارد', 'امروز', 'سمتِ', 'جمع اند', 'ضدِّ',
                   'نگاه', 'ظاهرا',
                   'بی نیازمندانه', 'یابید', 'نداشتید', 'دسته دسته', 'هستند', 'اینان', 'بکنم', 'صریحاً',
                   'سیاه چاله هاست', 'که', 'آقا',
                   'مرا', 'هیچگاه', 'به دلخواه', 'بیایم', 'کجا', 'بعضیهایشان', 'قبلا', 'هنگام', 'سابق', 'بسادگی', 'سعي',
                   'هی', 'هم اکنون',
                   '"', 'شیرین', 'به آسانی', 'هر چند که', 'بالا', 'هرگز', 'به شدت', 'بودی', 'لااقل', 'واقعا', 'بگیری',
                   'مستند', 'موارد',
                   'در', 'افزود', 'چنین', 'چون', 'تا', 'بندی', 'پیداست', 'بیابند', 'اکثرا', 'ازش', 'مدام', 'عنوانِ',
                   'پارسایانه', 'خ',
                   'بلی', 'آمد', 'کجاست', 'غزالان', 'آنچنان که', 'بدان', 'آوه', 'بکار', 'گیری', 'تنها', 'نکنم',
                   'بنابراین', 'بیاوری',
                   'باش', 'خسته\u200cای', 'زمانی', 'جریان', 'بد', 'گیر', 'براي', 'دهیم', 'براستی', 'آشنایند', 'بخواهی',
                   'البته', 'هيچ',
                   'بدین', 'بگیرم', 'دیده', 'خیر', 'روزه م', 'فلان', 'بر', 'بنابراين', 'مردم اند', 'کمی', 'چیست',
                   'ترین', 'نيز', 'نیستم',
                   'نکند', 'برداري', 'هايي', 'همانند', 'انها', 'کلیه', 'برخي', 'آوردن', 'کرده', 'پ', 'بیست', 'ر',
                   'نخست', 'گ', 'دو روزه',
                   'غیر', 'چنانچه', 'دیرت', 'هستم', 'چیه', 'عیناً', 'هستی', 'پیرامون', 'سخت', 'هر از گاهی', 'باشند',
                   'اول', 'جای',
                   'اصولاً', 'مواجهند', 'نخواهید', 'در مجموع', 'مجددا', 'علناً', 'الهی', 'پس از', 'يك', 'او', 'آنان',
                   'قاطعانه', 'یکهزار',
                   'کن', 'بسیار', 'درست', 'کردیم', 'بزرگ', 'آنهاست', 'نفرند', 'مامان مامان گویان', 'علاوه برآن', 'شدیم',
                   'کم کم', 'بگویم',
                   'زیرا', 'می\u200cخواهیم', 'مگر آن که', 'بکند', 'همواره', 'نداری', 'بندي', 'بیابی', 'همچنین',
                   'آن\u200cها', 'باشید',
                   'میلیون', 'اقل', 'سالیانه', 'خواستید', 'چشم بسته', 'میکنید', 'کردید']

stemmer = Stemmer()
normalizer = Normalizer()
PersianStopWord = {stemmer.stem(word) for word in hazm.stopwords_list() + PersianStopWord}


def tokenize_post_text(post_text):
    stemmer = Stemmer()
    normalizer = Normalizer()
    word_list = {stemmer.stem(word).strip(string.punctuation + '۱۲۳۴۵۶۷۸۹۰' + '؟!.،,?').replace(u'\u200c', ' ').strip()
                 for word in
                 BeautifulSoup(normalizer.affix_spacing(post_text), "html.parser").text.split()}
    final_word = {word for word in word_list if word not in PersianStopWord}
    return final_word


def stemmer(word):
    stemmer = Stemmer()
    return stemmer.stem(word)