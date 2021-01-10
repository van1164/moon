from django.contrib import admin
from .models import dataxx
from .models import admin_account
from .models import 질문지
from .models import 제8기동사단
from .models import 정보통신대대
from .models import 직할공병대대
from .models import 직할군수지원대대
from .models import 기갑수색대대
from .models import 보충중대
from .models import 의무대
from .models import 군사경찰대
from .models import 본부대
from .models import 화생방지원대대
from .models import 정보대대
from .models import 사단직할대
from .models import 제101기보대대
from .models import 제122기보대대
from .models import 제137기보대대
from .models import 기갑군수지원대대
from .models import 기갑참모부
from .models import 기갑직할대
from .models import 기갑여단
from .models import 인사처
from .models import 정보처
from .models import 작전처
from .models import 군수처
from .models import 화력실
from .models import 교훈처
from .models import 지통처
from .models import 군종부
from .models import 공보정훈부
from .models import 재정부
from .models import 지휘부
from .models import 작계처
from .models import 감찰부
from .models import 법무부
from .models import 참모처
from .models import 제107기보대대
from .models import 제26전차대대
from .models import 제32전차대대
from .models import 제60군수지원대대
from .models import 제60직할대
from .models import 제60참모부
from .models import 제60여단
from .models import 제123기보대대
from .models import 제125기보대대
from .models import 제57전차대대
from .models import 제73군수지원대대
from .models import 제73직할대
from .models import 제73참모부
from .models import 제73여단
from .models import 제50포병대대
from .models import 제95포병대대
from .models import 제228포병대대
from .models import 제231포병대대
from .models import 포병직할대
from .models import 포병참모부
from .models import 포병여단



# Register your models here.

admin.site.register(dataxx)
admin.site.register(admin_account)
admin.site.register(질문지)
admin.site.register(제8기동사단)
# ================================사단직할대=====================================
admin.site.register(정보통신대대)
admin.site.register(직할공병대대)
admin.site.register(직할군수지원대대)
admin.site.register(기갑수색대대)
admin.site.register(보충중대)
admin.site.register(의무대)
admin.site.register(군사경찰대)
admin.site.register(본부대)
admin.site.register(화생방지원대대)
admin.site.register(정보대대)
admin.site.register(사단직할대)
# ================================제 1기갑여단=====================================
admin.site.register(제101기보대대)
admin.site.register(제122기보대대)
admin.site.register(제137기보대대)
admin.site.register(기갑군수지원대대)
admin.site.register(기갑참모부)
admin.site.register(기갑직할대)
admin.site.register(기갑여단)
# ================================ 참모처 =====================================
admin.site.register(인사처)
admin.site.register(정보처)
admin.site.register(작전처)
admin.site.register(군수처)
admin.site.register(화력실)
admin.site.register(교훈처)
admin.site.register(지통처)
admin.site.register(군종부)
admin.site.register(공보정훈부)
admin.site.register(재정부)
admin.site.register(지휘부)
admin.site.register(작계처)
admin.site.register(감찰부)
admin.site.register(법무부)
admin.site.register(참모처)
# =================================제 60여단=====================================
admin.site.register(제107기보대대)
admin.site.register(제26전차대대)
admin.site.register(제32전차대대)
admin.site.register(제60군수지원대대)
admin.site.register(제60직할대)
admin.site.register(제60참모부)
admin.site.register(제60여단)
# =================================제 73여단=====================================
admin.site.register(제123기보대대)
admin.site.register(제125기보대대)
admin.site.register(제57전차대대)
admin.site.register(제73군수지원대대)
admin.site.register(제73직할대)
admin.site.register(제73참모부)
admin.site.register(제73여단)
# ================================포병여단=====================================
admin.site.register(제50포병대대)
admin.site.register(제95포병대대)
admin.site.register(제228포병대대)
admin.site.register(제231포병대대)
admin.site.register(포병직할대)
admin.site.register(포병참모부)
admin.site.register(포병여단)
