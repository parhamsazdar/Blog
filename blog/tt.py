# from googletrans import Translator
# translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.kr',
#     ])
#
# translator.translate('hello')
from django.conf import settings
from khayyam import JalaliDatetime
from datetime import datetime
from django.utils import timezone

print(timezone.now())
print(JalaliDatetime(timezone.now()).strftime('%C').strftime('%C'))