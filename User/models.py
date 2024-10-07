from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=50, unique=True)               # 유저 아이디
    password = models.CharField(max_length=100, unique=True)         # 유저 비밀번호
    user_code = models.CharField(max_length=20, primary_key=True)  # 유저 코드 (고유 및 외래키로 참조 가능)

    class Meta:
        # user_code를 복합 기본키처럼 사용
        unique_together = (('user_code'),)  # 복합 고유 제약 설정

    def __str__(self):
        return self.user_code

#
#class SomeOtherModel(models.Model):
#    user_code = models.ForeignKey(User, to_field='user_code', on_delete=models.CASCADE)  # 외래키로 user_code 참조
#    description = models.TextField()
#
#    def __str__(self):
#        return f"Related to User Code: {self.user_code}"