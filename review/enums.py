from django.db import models
from django.utils.translation import gettext_lazy as _

class QuestionCategory(models.TextChoices):
    school = "학교", _("학교")
    life = "생활", _("생활")
    free = "자유", _("자유")
