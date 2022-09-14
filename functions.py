def addColorToClass(class1, txtColor, backgroundColor):
    css1 = "<style>."+class1+" {background-color: "+backgroundColor+";color: "+txtColor+";border: 2px solid black;margin: 20px;padding: 20px;}</style>"
    return css1
def changeNav2(txtColor, backgroundColor):
    css1 = "<style>.home {background-color: "+backgroundColor+";color: "+txtColor+";border: 2px solid black;margin: 20px;padding: 20px;} .intro{background-color: "+backgroundColor+";color: "+txtColor+";border: 2px solid black;margin: 20px;padding: 20px;} .ob {background-color: "+backgroundColor+";color: "+txtColor+";border: 2px solid black;margin: 20px;padding: 20px;}</style>"
    return css1
def addToCss(css2):
    css1 = "<style>"+css2+"</style>"
    return css1
def p1(words):
    p2 = "<p>"+words+"</p>"
    return p2
def b1(words):
    p2 = "<b>"+words+"</b>"
    return p2
def i1(words):
    p2 = "<i>"+words+"</i>"
    return p2
def img1(url):
    p2 = "<img src="+url+">"
    return p2
def li1(list1):
    p2 = "<ul> <li> "+list1+" </li> </ul>"
    return p2
def br1():
    p2 = "<br>"
    return p2
def bodyStart():
    p2 = "<body>"
    return p2
def bodyStop():
    p2 = "</body>"
    return p2
def title1(words):
    p2 = "<title>"+words+"</title>"
    return p2
def h1(words, number1):
    p2 = "<h"+number1+">"+words+"</h"+number1+">"
    return p2
def em1(words):
    p2 = "<em>"+words+"</em>"
    return p2
def u1(words):
    p2 = "<u>"+words+"</u>"
    return p2
def a1(link):
    p2 = "<a href="+link+">"+words+"</a>"
    return p2
def small1(words):
    p2 = "<small>"+words+"</small>"
    return p2
def strike1(words):
    p2 = "<strike>"+words+"</strike>"
    return p2
def ol1(words):
    p2 = "<ol>"+words+"</ol>"
    return p2
def comment1(words):
    p2 = "<!-- "+words+" -->"
    return p2
def center1(words):
    p2 = "<center>"+words+"</center>"
    return p2
def div1():
    p2 = "<div>"
    return p2
def div2():
    p2 = "</div>"
    return p2
def divColor():
    p2 = "<div class=`city`;background-color=grey>"
    # print(divId)
    # divId = divId + 1
    return p2
def inputElem(id1, yourClass, type1, name, value):
    idHolder = ''
    classHolder = ''
    type1Holder = ''
    nameHolder = ''
    valueHolder = ''
    addHtml = False
    p2 = ''
    if(id1 != ''):
        idHolder = 'id='+id1+''
        addHtml = True
    if(yourClass != ''):
        classHolder = 'class='+yourClass+''
        addHtml = True
    if(type1 != ''):
        type1Holder = 'type='+type1+''
        addHtml = True
    if(name != ''):
        nameHolder = 'name='+name+''
        addHtml = True
    if(value != ''):
        valueHolder = 'value='+value+''
        addHtml = True
    if(addHtml):
        p2 = "<input "+type1Holder+" "+classHolder+" "+idHolder+" "+nameHolder+" "+valueHolder+">"
    return p2
def tagElem(tag, yourClass, type1, name, value, id1, onblur, onchange, onclick, oncontextmenu, oncopy, oncut, ondblclick, ondrag, ondragend, ondragenter, ondragleave, ondragover, ondragstart, ondrop, onfocus, oninput, oninvalid, onkeydown, onkeypress, onkeyup, onmousedown, onmousemove, onmouseout, onmouseover, onmouseup, onmousewheel, onpaste, onscroll, onselect, onwheel, onmoreAttributes, internalText):
    p2 = ''
    addHtml = False
    tagHolder = ''
    if(tag != ''):
        tagHolder = 'tag='+tag+''
        addHtml = True
    yourClassHolder = ''
    if(yourClass != ''):
        yourClassHolder = 'class='+yourClass+''
        addHtml = True
    type1Holder = ''
    if(type1 != ''):
        type1Holder = 'type='+type1+''
        addHtml = True
    nameHolder = ''
    if(name != ''):
        nameHolder = 'name='+name+''
        addHtml = True
    valueHolder = ''
    if(value != ''):
        valueHolder = 'value='+value+''
        addHtml = True
    id1Holder = ''
    if(id1 != ''):
        id1Holder = 'id1='+id1+''
        addHtml = True
    onblurHolder = ''
    if(onblur != ''):
        onblurHolder = 'onblur='+onblur+''
        addHtml = True
    onchangeHolder = ''
    if(onchange != ''):
        onchangeHolder = 'onchange='+onchange+''
        addHtml = True
    onclickHolder = ''
    if(onclick != ''):
        onclickHolder = 'onclick='+onclick+''
        addHtml = True
    oncontextmenuHolder = ''
    if(oncontextmenu != ''):
        oncontextmenuHolder = 'oncontextmenu='+oncontextmenu+''
        addHtml = True
    oncopyHolder = ''
    if(oncopy != ''):
        oncopyHolder = 'oncopy='+oncopy+''
        addHtml = True
    oncutHolder = ''
    if(oncut != ''):
        oncutHolder = 'oncut='+oncut+''
        addHtml = True
    ondblclickHolder = ''
    if(ondblclick != ''):
        ondblclickHolder = 'ondblclick='+ondblclick+''
        addHtml = True
    ondragHolder = ''
    if(ondrag != ''):
        ondragHolder = 'ondrag='+ondrag+''
        addHtml = True
    ondragendHolder = ''
    if(ondragend != ''):
        ondragendHolder = 'ondragend='+ondragend+''
        addHtml = True
    ondragenterHolder = ''
    if(ondragenter != ''):
        ondragenterHolder = 'ondragenter='+ondragenter+''
        addHtml = True
    ondragenterHolder = ''
    if(ondragenter != ''):
        ondragenterHolder = 'ondragenter='+ondragenter+''
        addHtml = True
    ondragleaveHolder = ''
    if(ondragleave != ''):
        ondragleaveHolder = 'ondragleave='+ondragleave+''
        addHtml = True
    ondragoverHolder = ''
    if(ondragover != ''):
        ondragoverHolder = 'ondragover='+ondragover+''
        addHtml = True
    ondragstartHolder = ''
    if(ondragstart != ''):
        ondragstartHolder = 'ondragstart='+ondragstart+''
        addHtml = True
    ondropHolder = ''
    if(ondrop != ''):
        ondropHolder = 'ondrop='+ondrop+''
        addHtml = True
    onfocusHolder = ''
    if(onfocus != ''):
        onfocusHolder = 'onfocus='+onfocus+''
        addHtml = True
    oninputHolder = ''
    if(oninput != ''):
        oninputHolder = 'oninput='+oninput+''
        addHtml = True
    oninvalidHolder = ''
    if(oninvalid != ''):
        oninvalidHolder = 'oninvalid='+oninvalid+''
        addHtml = True
    onkeydownHolder = ''
    if(onkeydown != ''):
        onkeydownHolder = 'onkeydown='+onkeydown+''
        addHtml = True
    onkeypressHolder = ''
    if(onkeypress != ''):
        onkeypressHolder = 'onkeypress='+onkeypress+''
        addHtml = True
    onkeyupHolder = ''
    if(onkeyup != ''):
        onkeyupHolder = 'onkeyup='+onkeyup+''
        addHtml = True
    onmousedownHolder = ''
    if(onmousedown != ''):
        onmousedownHolder = 'onmousedown='+onmousedown+''
        addHtml = True
    onmousemoveHolder = ''
    if(onmousemove != ''):
        onmousemoveHolder = 'onmousemove='+onmousemove+''
        addHtml = True
    onmouseoutHolder = ''
    if(onmouseout != ''):
        onmouseoutHolder = 'onmouseout='+onmouseout+''
        addHtml = True
    onmouseoverHolder = ''
    if(onmouseover != ''):
        onmouseoverHolder = 'onmouseover='+onmouseover+''
        addHtml = True
    onmouseupHolder = ''
    if(onmouseup != ''):
        onmouseupHolder = 'onmouseup='+onmouseup+''
        addHtml = True
    onmousewheelHolder = ''
    if(onmousewheel != ''):
        onmousewheelHolder = 'onmousewheel='+onmousewheel+''
        addHtml = True
    onpasteHolder = ''
    if(onpaste != ''):
        onpasteHolder = 'onpaste='+onpaste+''
        addHtml = True
    onscrollHolder = ''
    if(onscroll != ''):
        onscrollHolder = 'onscroll='+onscroll+''
        addHtml = True
    onselectHolder = ''
    if(onselect != ''):
        onselectHolder = 'onselect='+onselect+''
        addHtml = True
    onwheelHolder = ''
    if(onwheel != ''):
        onwheelHolder = 'onwheel='+onwheel+''
        addHtml = True
    onmoreAttributesHolder = ''
    if( onmoreAttributes != ''):
        onmoreAttributesHolder = ''+onmoreAttributes+''
        addHtml = True
    internalTextHolder = ''
    if( internalText != ''):
        internalTextHolder = ''+internalText+''
        addHtml = True
    if(addHtml):
        p2 = "<"+tag+""+type1Holder+""+yourClassHolder+""+id1Holder+""+nameHolder+""+valueHolder+""+onblurHolder+""+onchangeHolder+""+onclickHolder+""+oncontextmenuHolder+""+oncopyHolder+""+oncutHolder+""+ondblclickHolder+""+ondragHolder+""+ondragendHolder+""+ondragenterHolder+""+ondragleaveHolder+""+ondragoverHolder+""+ondragstartHolder+""+ondropHolder+""+onfocusHolder+""+oninputHolder+""+oninvalidHolder+""+onkeydownHolder+""+onkeypressHolder+""+onkeyupHolder+""+onmousedownHolder+""+onmousemoveHolder+""+onmouseoutHolder+""+onmouseoverHolder+""+onmouseupHolder+""+onmousewheelHolder+""+onpasteHolder+""+onscrollHolder+""+onselectHolder+""+onwheelHolder+""+onmoreAttributes+">"+internalTextHolder+"</"+tag+">"
        def Appendtext(p3):
            with open('htmlMemory.txt','a+') as f:
                f.write(''+p3+'')
            f.close()
        Appendtext(p2)
    addHtml = False
    return p2
def createButton(id1, yourClass, buttonLabel, action):
    p2 = ''
    addHtml = False
    actionHolder = ''
    id1Holder = ''
    classHolder = ''
    labelHolder = ''
    if(action != ''):
        actionHolder = " onclick=window.location.href="+action+""
        addHtml = True
    if(id1 != ''):
        id1Holder = " id="+id1+""
        addHtml = True
    if(yourClass != ''):
        classHolder = " class="+yourClass+""
        addHtml = True
    if(buttonLabel != ''):
        labelHolder = "" +buttonLabel+""
        addHtml = True
    print('create button was ran')
    if(addHtml):
        p2 = "<button"+actionHolder+""+id1Holder+""+classHolder+""+actionHolder+">"+buttonLabel+"</button>"
    return p2
def font1(words, font):
    p2 = "<font face="+font+">"+words+"</font>"
    return p2
def link1(link2):
    p2 = "<link type=`text/css` href="+link2+">"
    return p2
def hr1(width, size):
    p2 = "<hr width="+width+" size="+size+" />"
    return p2
def meta1(name, content):
    p2 = "<meta name="+name+" content="+content+">"
    return p2
def tableStart(border, cellpadding, cellspacing, width):
    p2 = "<table border="+border+" cellpadding="+cellpadding+" cellspacing="+cellspacing+" width="+width+">"
    return p2
def tableStop():
    p2 = "</table>"
    return p2
def trStart():
    p2 = "<tr>"
    return p2
def trStop():
    p2 = "</tr>"
    return p2
def th1(words):
    p2 = "<th>"+words+"</th>"
    return p2
def td1(words):
    p2 = "<td>"+words+"</td>"
    return p2
def formAction(action):
    p2 = "<form action=`"+action+"`>"
    return p2
def formActionMethod(action, method):
    p2 = "<form method="+method+"action=`"+action+"`>"
    return p2
def formStop():
    p2 = "</form>"
    return p2
def input1(addedHtmlInput):
    p2 = "<input "+addedHtmlInput+">"
    return p2
def option1(theOption):
    p2 = "<option>"+theOption+"</option>"
    return p2
def optionSelected1(theOption):
    p2 = "<option selected>"+theOption+""
    return p2
def sendToHtml(html1):
    p2 = ""+html1+""
    return p2
def deleteHtmlTxt():
    f = open("htmlMemory.txt", "r+")
    f.truncate(0)
    f.close()
def deleteCssTxt():
    f = open("cssMemory.txt", "r+")
    f.truncate(0)
    f.close()
def profile(bio1, pfp1, background1, name1):
    from formats import homePageFormat1
    import getpass
    user = getpass.getuser()
    addCss = 0
    addHtml = 0
    css = ''
    html = ''
    import sys
    args: list[str] = sys.argv
    filename = 'websites.txt'
    file = open(filename, "r")
    line_count = 0

    for line in file:

        if line != "\n":

            line_count += 1
    with open ('websites.txt', 'rt') as myfile:
        p2 = ''
        linesRead = 0
        timesLooped = 0
        for myline in myfile:
            while(linesRead < 2 and timesLooped < line_count):
                timesLooped += 1
                if(addHtml == 1):
                    html = myline
                    addHtml = 0
                    linesRead = linesRead + 1
                if(addCss == 1):
                    addHtml = 1
                    css = myline
                    addCss = 0
                if(myline == 'this file belongs to '+user+'\n'):
                    addCss = 1 
                    # print(user)
                # print(myline)
    with open ("htmlMemory.txt", "r") as myfile:
        htmlMemory = myfile.read()
    with open ("cssMemory.txt", "r") as myfile:
        cssMemory = myfile.read()
    css = ''.join([str(elem) for elem in css]).replace('\n', '') 
    html = ''.join([str(elem) for elem in html]).replace('\n', '') 
    def Appendtext():
        with open('websites.txt','a+') as f:
            f.write('\nthis file belongs to '+user+'\n'+css+''+cssMemory+'\n'+html+''+htmlMemory+'')
        f.close()
    Appendtext()
    html = html + htmlMemory
    css = css + cssMemory
    print(css)
    print(html)
    print(user)
    p2 = homePageFormat1(html, css,bio1, pfp1, background1, name1)
    return (p2)

