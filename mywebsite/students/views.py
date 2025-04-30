from django.shortcuts import render, redirect
from students.models import Student
from students.forms import PostForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # 抓資料表所有資料的方法
    # 資料表.objects.all()[.order_by(欄位名稱)]
    # Student.objects.all().order_by('id')
    stdData = Student.objects.all().order_by('id')
    paginator = Paginator(stdData,10)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    return render(request, "students/index.html", locals())

def stdSearch(request):
    # 抓資料表一筆資料的方法
    # 資料表.objects.get(查詢條件)
    # Student.objects.get(stdName="陳曉雯")
    # 避免查不到資料出現錯誤，用try...except包起來
    try:     # 要完成的任務
        result = Student.objects.get(stdName="陳曉X")
    except:  # 錯誤或例外發生時要執行的程式
        errormessage = "(讀取錯誤!)"
    return render(request, "students/stdSearch.html", locals())

def stdFormModel(request):
    # 建立表單驗證物件進階用法
    if request.method == 'POST':
        postform = PostForm(request.POST)
        if postform.is_valid():
            # 處理表單數據
            # 變數接資料    前端網頁傳過來的資料
            stdNamePost = request.POST["stdName"]
            stdSexPost = request.POST["stdSex"]
            stdBirthdayPost = request.POST["stdBirthday"]
            stdEmailPost = request.POST["stdEmail"]
            stdPhonePost = request.POST["stdPhone"]
            stdAddrPost = request.POST["stdAddr"]
            # 將資料新增至資料表
            # 資料表欄位名稱=變數名稱(從 request.POST 取得資料)
            unit = Student.objects.create(
                stdName=stdNamePost,
                stdSex=stdSexPost,
                stdBirth=stdBirthdayPost,
                stdEmail=stdEmailPost,
                stdPhone=stdPhonePost,
                stdAddr=stdAddrPost
            )
            # 將內容寫入資料庫
            unit.save()
            return redirect('/students/index/')
    else:
        postform = PostForm()
    
    return render(request, 'students/stdFormModel.html', locals())

def stdForm(request):
    if request.method == "POST":
        #             request.GET()
        # 變數接資料    前端網頁傳過來的資料
        stdNamePost = request.POST["stdName"]
        stdSexPost = request.POST["stdSex"]
        stdBirthdayPost = request.POST["stdBirthday"]
        stdEmailPost = request.POST["stdEmail"]
        stdPhonePost = request.POST["stdPhone"]
        stdAddrPost = request.POST["stdAddr"]
        # 將資料新增至資料表
        # 資料表欄位名稱=變數名稱(從 request.POST 取得資料)
        unit = Student.objects.create(
            stdName=stdNamePost,
            stdSex=stdSexPost,
            stdBirth=stdBirthdayPost,
            stdEmail=stdEmailPost,
            stdPhone=stdPhonePost,
            stdAddr=stdAddrPost
        )
        # 將內容寫入資料庫
        unit.save()

        return redirect("/students/index/")
    else:
        message = "請輸入資料(資料未作驗證)"
    return render(request, "students/stdForm.html", locals())

def delete(request,id=None):
    if id is not None:
        if request.method == "POST": #如果是以 POST 方式才處理
            id = request.POST['stdId']
        try:
            unit = Student.objects.get(id=id)
            unit.delete()
            return redirect('/students/index/')
        except:
            message = "讀取錯誤!"
    return render(request,"students/delete.html",locals())

def edit(request, id=None,mode=None):
    if mode=="edit": # edit.html 的 form 表單的 action 是 /edit/{{unit.id}}/edit
        unit = Student.objects.get(id=id) #取得要修改的資料記錄
        unit.stdName=request.GET['stdName']
        unit.stdSex=request.GET['stdSex']
        unit.stdBirth=request.GET['stdBirthday']
        unit.stdEmail=request.GET['stdEmail']
        unit.stdPhone=request.GET['stdPhone']
        unit.stdAddr=request.GET['stdAddr']
  
        unit.save() #寫入資料庫
        message = '已修改...'
        return redirect('/students/index/')
    else:
        try:
            unit = Student.objects.get(id=id) #取得要修改的資料記錄
            strdate = str(unit.stdBirth)
            strdate2 = strdate.replace("年","-")
            strdate2 = strdate.replace("月","-")
            strdate2 = strdate.replace("日","-")
            unit.stdBirth = strdate2
        except:
            message = "此 id 不存在！"
    return render(request, "students/edit.html", locals())

def edit2(request,id=None,mode=None):
    if mode=="save": # edit2.html 的 form 表單的 action 是 /edit/{{unit.id}}/save
        unit = Student.objects.get(id=id) #取得要修改的資料記錄
        unit.stdName=request.POST['stdName']
        unit.stdSex=request.POST['stdSex']
        unit.stdBirth=request.POST['stdBirthday']
        unit.stdEmail=request.POST['stdEmail']
        unit.stdPhone=request.POST['stdPhone']
        unit.stdAddr=request.POST['stdAddr']
        unit.save() #寫入資料庫
        message = '已修改...'
        return redirect('/students/index/')
    elif mode=="load":
        unit = Student.objects.get(id=id) #取得要修改的資料記錄
        strdate = str(unit.stdBirth)
        strdate2 = strdate.replace("年","-")
        strdate2 = strdate.replace("月","-")
        strdate2 = strdate.replace("日","-")
        unit.stdBirth = strdate2
        return render(request, "students/edit2.html", locals())