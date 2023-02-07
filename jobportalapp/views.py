from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.core.mail import send_mail
from job_portal_project.settings import EMAIL_HOST_USER

# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['cname']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['cpassword']
            ph = a.cleaned_data['phone']
            ad = a.cleaned_data['address']
            if ps == cp:
                b = regmodel(cname=nm, email=em, password=ps, cpassword=cp, phone=ph, address=ad)
                b.save()
                return redirect(login)
            else:
                return HttpResponse("incorrect password")
        else:
            return HttpResponse("registration failed")
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=regmodel.objects.all()
            for i in b:
                cmp=i.cname
                request.session['cname']=cmp
                id=i.id
                if i.email==em and i.password==ps:
                    return render(request,'profile.html',{'cmp':cmp,'id':id})
            else:
                    return HttpResponse("login failed")
    else:
        return render(request,'login.html')



def formpage(request,id):
    b=regmodel.objects.get(id=id)
    cm=b.cname
    em=b.email
    if request.method=='POST':
        a=pageform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['cname']
            em=a.cleaned_data['email']
            jn=a.cleaned_data['jname']
            jt=a.cleaned_data['jtype']
            wt = a.cleaned_data['wtype']
            ex = a.cleaned_data['exp']

            b=pagemodel(cname=nm, email=em, jname=jn, jtype=jt, wtype=wt, exp=ex)
            b.save()
            return redirect(jobdisplay)
        else:
            return HttpResponse("Registration Failed")
    else:
        return render(request,'upload job.html',{'cm':cm,'em':em})


def profile(request):
    return render(request, 'profile.html')


def jobdisplay(request):
    a=pagemodel.objects.all()
    b=request.session['cname']
    return render(request,'job display.html',{'a':a,'b':b})


def editcard(request,id):
    a=pagemodel.objects.get(id=id)
    if request.method=='POST':
        a.jname = request.POST.get('jname')
        a.cname=request.POST.get('cname')
        a.jtype=request.POST.get('jtype')
        a.wtype = request.POST.get('wtype')
        a.exp=request.POST.get('exp')
        a.save()
        return redirect(jobdisplay)
    return render(request,'Edit Card.html',{'a': a})

def deletecard(request,id):
    a=pagemodel.objects.get(id=id)
    a.delete()
    return redirect(jobdisplay)


def regclass(request):
    if request.method=='POST':
        un=request.POST.get('username')
        fn=request.POST.get('first_name')
        ln=request.POST.get('last_name')
        em=request.POST.get('email')
        ps=request.POST.get('password')
        b=User(username=un, first_name=fn, last_name=ln, email=em, password=ps)
        b.save()
        return redirect(logclass)
    else:
        return render(request,'userreg.html')


def logclass(request):
    if request.method=='POST':
        a=userlog(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=User.objects.all()
            for i in b:
                x = i.email
                request.session['email'] = x
                if i.email==em and i.password==ps:
                    return render(request,"userprofile.html",{'x':x})
            else:
                return HttpResponse("login failed")
    else:
        return render(request,'userlog.html')


def userupload(request):
    if (request.method == 'POST'):
        a = profileform(request.POST, request.FILES)
        if a.is_valid():
            im = a.cleaned_data['image']
            fn = a.cleaned_data['fname']
            em=a.cleaned_data['email']
            rs=a.cleaned_data['resume']
            ed=a.cleaned_data['education']
            ex=a.cleaned_data['exp']
            ad=a.cleaned_data['address']
            ph=a.cleaned_data['phone']
            b = profilemodel(image=im, fname=fn, email=em, resume=rs, education=ed, exp=ex, address=ad, phone=ph)
            b.save()
            return HttpResponse("file upload successfully...")
        else:
            return HttpResponse("file upload failed...")
    else:
        return render(request, 'userupload.html')


def apply(request,id):
    b =pagemodel.objects.get(id=id)
    cn=b.cname
    jt=b.jname
    if  request.method == 'POST':
        a = applyform(request.POST, request.FILES)
        if a.is_valid():
            cn=a.cleaned_data['company']
            jt=a.cleaned_data['title']
            fn = a.cleaned_data['fname']
            em=a.cleaned_data['email']
            rs=a.cleaned_data['resume']
            ed=a.cleaned_data['education']
            ex=a.cleaned_data['exp']
            ad=a.cleaned_data['address']
            ph=a.cleaned_data['phone']
            c = applymodel(company=cn,title=jt,fname=fn, email=em, resume=rs, education=ed, exp=ex, address=ad, phone=ph)
            c.save()
            # send mail
            subject= f"You Applied For {jt} at {cn}"
            message= f" hi {fn}\n Yor Application was sent to {cn} Successfully"
            email_from= EMAIL_HOST_USER

            send_mail(subject,message,email_from,[em])
            return redirect(emailalert)
        else:
            return HttpResponse("file upload failed...")
    else:
        return render(request, 'apply.html',{'cn':cn,'jt':jt})


def applieddisplay(request):
    a=pagemodel.objects.all()
    return render(request,'applied_display.html',{'a':a})


def emailalert(request):
    return render(request,'emailalert.html')


def wishlist(request,id):
    a=pagemodel.objects.get(id=id)
    b=wishmodel(cname=a.cname,email=a.email,jname=a.jname,jtype=a.jtype,wtype=a.wtype,exp=a.exp)
    b.save()
    return redirect(wish)


def wish(request):
    a=wishmodel.objects.all()
    return render(request,"wish.html",{'a':a})


def remove(request,id):
    a = wishmodel.objects.get(id=id)
    a.delete()
    return redirect(wish)


def appliedview(request):
    a=applymodel.objects.all()
    company=[]
    title=[]
    fname=[]
    email=[]
    resume = []
    education=[]
    exp=[]
    address=[]
    phone=[]
    id=[]
    b=request.session['cname']
    for i in a:
        co=i.company
        company.append(co)
        ti=i.title
        title.append(ti)
        fn=i.fname
        fname.append(fn)
        em=i.email
        email.append(em)
        re = i.resume
        resume.append(str(re).split('/')[-1])
        ed=i.education
        education.append(ed)
        ex=i.exp
        exp.append(ex)
        ad=i.address
        address.append(ad)
        ph=i.phone
        phone.append(ph)
        id1=i.id
        id.append(id1)
    mylist=zip(company,title,fname,email,resume,education,exp,address,phone,id)
    return render(request,"appliedview.html",{'list':mylist,'b':b})

def remov(request,id):
    a=applymodel.objects.get(id=id)
    a.delete()
    return redirect(appliedview)


def sendmail(request,id):
    a=applymodel.objects.get(id=id)
    jt=a.title
    cn=a.company
    fn=a.fname
    em=a.email

    if request.method=='POST':
        subject = f"You Applied For {jt} at {cn}"
        message = f" hi {fn}\n Yor Application was sent to {cn} Successfully"
        email_from = EMAIL_HOST_USER
        send_mail(subject,message, email_from,[em])
        return redirect(emailalert)
    else:
        return render(request, 'sendmail.html',{'jt':jt,'cn':cn,'fn':fn,'em':em})


def userapplied(request):
    a=applymodel.objects.all()
    company=[]
    title=[]
    fname=[]
    email=[]
    resume = []
    education=[]
    exp=[]
    address=[]
    phone=[]
    id=[]
    b=request.session['email']
    for i in a:
        co=i.company
        company.append(co)
        ti=i.title
        title.append(ti)
        fn=i.fname
        fname.append(fn)
        em=i.email
        email.append(em)
        re = i.resume
        resume.append(str(re).split('/')[-1])
        ed=i.education
        education.append(ed)
        ex=i.exp
        exp.append(ex)
        ad=i.address
        address.append(ad)
        ph=i.phone
        phone.append(ph)
        id1=i.id
        id.append(id1)
    mylist=zip(company,title,fname,email,resume,education,exp,address,phone,id)
    return render(request,"userapplied.html",{'list':mylist,'b':b})

