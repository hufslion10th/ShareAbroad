from django.db import models
from django.utils.translation import gettext_lazy as _

class ReviewCategory(models.TextChoices): # 카테고리 안에 카테고리 넣는 법도 알아보면 좋을듯 (교환학생-유럽/7+1-아메리카 이렇게)
    exchange = "교환학생", _("교환학생")
    sevenone = "7+1", _("7+1")
    etc = "기타", _("기타") 
