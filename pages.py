from flask import Flask, render_template, request
from bs4 import BeautifulSoup as Soup
import urllib
from keyboard import press
from functions import addColorToClass, addToCss, p1, b1, i1, img1, li1, br1, bodyStart, bodyStop, title1, h1, em1, u1, a1, small1, strike1, ol1, comment1, center1, div1, div2, divColor, inputElem, createButton, font1, link1, hr1, meta1, tableStart, tableStop, trStart, trStop, th1, td1, formAction, formActionMethod, formStop, input1, option1, optionSelected1, sendToHtml
import getpass
from formats import homePageFormat

def homePage(addHtml, addCss, addJs):
    user = getpass.getuser()
    orders = request.form
    if (len(orders.getlist('username')) > 0):
        user = orders.getlist('username')[0]
        file1 = open("user.txt", "a")  # append mode
        file1.write(""+user+"\n")
        file1.close()
        print('user was changed')
    with open('user.txt') as f:
        for line in f:
            user = line
    
    cssContainer = []
    htmlContainer = []
    jsContainer = []
    divId1 = "0"
    s = ["<p class='button4'>hello this is a example of creating your own page</p>"]
    c = []
    j = []
    def add(script):
        htmlContainer.append(script)
    def add2(script):
        cssContainer.append(script)
    def add3(script):
        jsContainer.append(script)
    add(createButton("theId", "button4", "click to go home", '/'))
    add(p1("ADD TO HTML"))
    add(p1("create any element you can think of"))
    add(p1("attributes that work on any element"))
    attributeArr = "tag,yourClass,type,name,value,id,onblur,onchange,onclick,oncontextmenu,oncopy,oncut,ondblclick,ondrag,ondragend,ondragenter,ondragenter,ondragleave,ondragover,ondragstart,ondrop,onfocus,oninput,oninvalid,onkeydown,onkeypress,onkeyup,onmousedown,onmousemove,onmouseout,onmouseover,onmouseup,onmousewheel,onpaste,onscroll,onselect,onwheel,add-any-attribute,internal-text".split(',')
    answer = []
    urlName = 'tagElem'
    count = 0
    for i in attributeArr:
        count = count + 1
        # print(i)
        answer.append("<input type='text' name='"+urlName+"' placeholder='"+i+"'>")
    inputHtml = ','.join(answer).replace(',', '')
    add(sendToHtml("<form action='/api/tagElem' method='POST'>"+inputHtml+"<button class='button4' value='submit'>submit</button></form>"))
    add(p1("input"))
    add(sendToHtml("<form action='/api/inputElem' method='POST'><input type='text' name='inputElem' placeholder='id'><input placeholder='your-class' type='text' name='inputElem' ><input placeholder='type' type='text' name='inputElem' ><input placeholder='name' type='text' name='inputElem' ><input placeholder='value' type='text' name='inputElem' ><button class='button4' value='submit'>submit</button></form>"))
    add(p1("create button"))
    add(sendToHtml("<form action='/api/createButton3' method='POST'><input placeholder='id' type='text' name='createButton3' ><input placeholder='class' type='text' name='createButton3' ><input placeholder='label' type='text' name='createButton3' ><input placeholder='function' type='text' name='createButton3' ><button class='button4' value='submit'>submit</button></form>"))
    add(p1("p1"))
    add(sendToHtml("<form action='/api/p1' method='POST'><input placeholder='add-text' type='text' name='p1'><button class='button4' value='submit'>submit</button></form>"))
    add(p1("b1"))
    add(sendToHtml("<form action='/api/b1' method='POST'><input placeholder='add-text' type='text' name='b1'><button class='button4' value='submit'>submit</button></form>"))
    add(p1("i1"))
    add(sendToHtml("<form action='/api/i1' method='POST'><input placeholder='add-text' type='text' name='i1'><button class='button4' value='submit'>submit</button></form>"))
    add(p1("DELETE ADDED HTML"))
    add(sendToHtml("<form action='/api/deleteHtmlTxt' method='POST'><button class='button4' value='submit'>DELETE HTML</button></form>"))
    add(p1("change CSS"))
    add(p1("add to css"))
    add(sendToHtml("<form action='/api/addToCss1' method='POST'><input placeholder='add-css-here' type='text' name='addToCss1'><button class='button4' value='submit'>submit</button></form>"))
    add(p1("add color to class"))
    add(sendToHtml("<form action='/api/addColorToClass3' method='POST'><input placeholder='class' type='text' name='addColorToClass3' ><input placeholder='text-color' type='text' name='addColorToClass3' ><input placeholder='background-color' type='text' name='addColorToClass3' ><button class='button4' value='submit'>submit</button></form>"))
    add(p1("change navigation"))
    add(sendToHtml("<form action='/api/changeNav3' method='POST'><input placeholder='text-color' type='text' name='changeNav3' ><input placeholder='background-color' type='text' name='changeNav3' ><button class='button4' value='submit'>submit</button></form>"))
    add(p1("DELETE ADDED CSS"))
    add(sendToHtml("<form action='/api/deleteCssTxt' method='POST'><button class='button4' value='submit'>DELETE HTML</button></form>"))
    add(p1("add javascript"))
    add("<form action='/api/changeNav3' method='POST'><input placeholder='add-javascript-here' type='text' name='changeNav3' ><button class='button4' value='submit'>submit</button></form>")
    add(p1("send to your profile"))
    print("The user currently logged in is: " + user)
    # add(sendToHtml("<form action='/api/profile' method='POST'><button class='button4' value='submit'>Save website</button></form>"))
    add(sendToHtml("<form action='/api/profile' method='POST'><input placeholder='bio' type='text' name='profile3' ><input placeholder='profile pic' type='text' name='profile3' ><input placeholder='background pic' type='text' name='profile3' ><input placeholder='name' type='text' name='profile3' ><button class='button4' value='submit'>make profile</button></form>"))
    with open ("htmlMemory.txt", "r") as myfile:
        data = myfile.read()
    add(data)
    with open ("cssMemory.txt", "r") as myfile:
        data = myfile.read()
    add2(data)
    with open ("jsMemory.txt", "r") as myfile:
        data = myfile.read()
    add3(data)

    add(sendToHtml(addHtml))
    add2(sendToHtml(addCss))
    add3(sendToHtml(addJs))
    add(div2())
    add2(addColorToClass("button4","white", "#8b0000"))
    s.append(htmlContainer)
    c.append(cssContainer)
    j.append(jsContainer)
    def listToString(x):
        x = ' '.join([str(elem) for elem in x])
        x = x.replace("'", '')
        x = x.replace('[', '')
        x = x.replace(']', '')
        x = x.replace(',', '')
        return x
    s = listToString(s)
    c = listToString(c)
    j = listToString(j)
    htmlInput = s
    css = c
    javascript = j
    # css = ["<style>.button4 {background-color: tomato;color: white;border: 2px solid black;margin: 20px;padding: 20px;}</style>"]
    # css = ' '.join([str(elem) for elem in css])
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width", initial-scale="1.0"><meta http-equiv="X-UA-Compatible" content="ie=edge">'+css+'<title>My Website</title></head><body><main class="btns-container"><h1 href="parts.html" class="finder">Axis<h1>  <button id="home" class="ob" type="button" onclick=window.location.href="/">HOME</button> <button id="VR" class="ob" type="button">log in to different account</button><button id="pc" class="ob" type="button" onclick=window.location.href="pc.html">PC</button><button id="phones" class="ob" type="button" onclick=window.location.href="phones.html">Phones</button><button id="processors" class="ob" type="button" onclick=window.location.href="processors.html">Processors</button><button id="parts" class="ob" type="button" onclick=window.location.href="parts.html">Parts</button><button id="sell" class="ob" type="button" onclick=window.location.href="sell.html">Sell</button><button id="checkout" class="ob" type="button" onclick=window.location.href="checkout.html">Checkout</button><div class="banner-section" id="img-container"><h2 class="home">'+user+'</h2><p class="intro">this is an open sourced social network site</p><img src="https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2012/05/internet-globe.jpg">'+javascript+''+htmlInput+'</main><section id="electroics-container"></section><section id="cart"></section></body></html>'

    html = html.replace('"', '')
    def Appendtext(html1):
        with open('websites.txt','a+') as f:
            f.write('\nthis file belongs to '+user+'\n'+css+'\n'+html1+'')
        f.close()
    Appendtext(htmlInput)


    return html