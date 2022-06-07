#I have created this file -Rishi Raj
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'Rishi','place':'Moon'}
    #return HttpResponse("This is the Home Page")
    return render(request,'index.html',params)
def about(request):
    return HttpResponse("<h1>This is a Text Utility website made by Rishi Raj</h1>")
def analyze(request):
    #Took the text input entered in the form
    djtext=request.GET.get("text","default")
    #Take the input of the check boxex.
    removepunc=request.GET.get('removepunc',"off")
    fullcaps=request.GET.get('fullcaps',"off")
    print(djtext)
    print(removepunc)
    #return HttpResponse("Hello beta! Analyze karoge na?")
    if removepunc=="on":
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed+=char
        if fullcaps=="on":
            analyzed2=""
            for char in analyzed:
                analyzed2=analyzed2+char.upper()
            params={'purpose':"Remove the punctuatios",'analyzed_text':analyzed2}
            return render(request,'analyze.html',params)
        params={'purpose':"Remove the punctuatios",'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':"Capitalize Text",'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Remove punctuation function is not selected.")

    
def displayTextFile(request):
    #Toopen a file in the innermost folder: 
    file=open("textutils/myTestFile.txt","rt")
    #"rt" means read and write.
    #To open a file in the outer folder:
    #file=open("./myTextFile.txt","rt")
    return HttpResponse(file.read())
def rmvpunc(request):
    djangotext= request.GET.get('text','name')
    print(djangotext +"Mera apna text bhi saath me print hoga hi na harry bhai")
    return HttpResponse("Remove the Punctuation")
def capfirst(request):
    return HttpResponse("Capitalize the first letter")
def rmvnewline(request):
    return HttpResponse("Remove the new lines")
def rmvspace(request):
    return HttpResponse("Remove the spaces")
def cntchar(request):
    return HttpResponse("Count the number of characters")
def exercise1(request):
    return HttpResponse('''<h1>This is a personal Navigator Page</h1><br>
    <a href="https://www.google.com">Google</a><br>
    <a href="https://www.youtube.com">Youtube</a><br>
    <a href="https://www.facebook.com">Facebook</a><br>
    <a href="https://www.codewithharry.com">Code With Harry</a><br>
    <a href="https://irishirajj.github.io">Rishi Raj</a>''')