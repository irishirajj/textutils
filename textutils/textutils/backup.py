#Took the text input entered in the form
    djtext=request.GET.get("text","default")
    #Take the input of the check boxex.
    removepunc=request.GET.get('removepunc',"off")
    fullcaps=request.GET.get('fullcaps',"off")
    removeNewLine=request.GET.get('removenewline',"off")
    removeExtraSpace=request.GEt.get('removespace',"off")
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