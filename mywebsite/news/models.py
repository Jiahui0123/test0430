from django.db import models

# Create your models here.

# 定義分類名稱欄位 
class Category(models.Model): 
    title = models.CharField(max_length=255, default="") 
 
    def __str__(self): 
        return self.title 
    
class NewsUnit(models.Model):
    # 設定新聞訊息類別
    # category = models.CharField(max_length=10,null=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT) 
    # 發佈新聞的作者
    author = models.CharField(max_length=20,null=False)
    # 新聞訊息的標題
    title = models.CharField(max_length=100,null=False)
    # 新聞訊息的內容
    content = models.TextField(null=False)
    # 新聞發佈的時間
    pub_date = models.DateTimeField(auto_now_add=True)
    # 是允許許顯示
    is_show = models.BooleanField(default=False)
    # 點擊此數
    click_count = models.IntegerField(default=0)
    # 新聞訊息的圖片
    image = models.ImageField(upload_to='news_images/',null=True,blank=True)
    # 新聞訊息的連結
    link = models.URLField(null=True,blank=True)

    def __str__(self):
        # return self.title
        return self.title
    

