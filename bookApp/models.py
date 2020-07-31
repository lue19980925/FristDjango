from django.db import models

# Create your models here.
class Book(models.Model):
    #title is a string leixing max_length is 20
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(True)
    def __repr__(self):
        return '<Book: %s>' %(self.title)

    # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        db_table = "books"
        verbose_name_plural = '图书管理'
class Hero(models.Model):
    name = models.CharField(max_length=20)     #name
    gender = models.BooleanField()  #sex
    content = models.CharField(max_length=200)  #jianjie
    Book = models.ForeignKey('Book',on_delete=models.CASCADE)
    def __repr__(self):
        return "<Hero %s>" %(self.name)
    def __str__(self):
        return self.name
    def sex(self):
        if self.gender:
            return "男"
        else:
            return "女"
    # 自定义对应的表名，默认表名：bookApp_hero
    class Meta:
        db_table = "heros"
        verbose_name_plural = '人物管理'

