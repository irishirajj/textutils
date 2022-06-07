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
    djtext=request.POST.get("text","default")

    #Take the input of all the check boxes.
    removepunc=request.POST.get('removepunc',"off")
    fullcaps=request.POST.get('fullcaps',"off")
    removeNewLine=request.POST.get('removenewline',"off")
    removeExtraSpace=request.POST.get('removespace',"off")

    #Now, if any of the checkboxes were selected we will do someting.Else, return http response:

    if removepunc=="on" or fullcaps=="on" or removeNewLine=="on" or removeExtraSpace=="on":
        message="We have "
        analyzed=djtext
        if removepunc=="on":
            temp=""
            for char in analyzed:
                if char not in punctuation:
                    temp=temp+char
            analyzed=temp
        if fullcaps=="on":
            temp=""
            for char in analyzed:
                temp+=char.upper()
            analyzed=temp
        if removeNewLine =="on":
            #analyzed=  analyzed.replace('\n', ' ').replace('\r', '')
            temp=""
            for char in analyzed:
                if char!='\n' and char!='\r':
                    temp+=char
            analyzed=temp

        if removeExtraSpace=="on":
            temp=""
            for index,char in enumerate(analyzed):
                if analyzed[index]==" " and analyzed[index+1]==" ":
                    pass
                else:
                    temp+=char
            analyzed=temp
        params={'purpose':"Capitalize Text",'analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("None of the text modifiers options were selected.")
    

    
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