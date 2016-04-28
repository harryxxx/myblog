var num=0

function changePic (whichpic) 
{
    if (!document.getElementsByTagName || !document.getElementById) return false;
    var source = whichpic.getAttribute("href");
    var des = document.getElementById("description");
    if (source == "pre")
    {
        if (num != 0)
        {
            num --;
            source = "./static/pic2/pic" + num + ".jpg";
        }
        else
            source = "./static/pic2/pic" + num + ".jpg";
    }
    if (source == "next")
    {
        num ++;
        source = "./static/pic2/pic" + num + ".jpg";
    }
    text = "picture-"+num
    var pic = document.getElementById("picture");
    des.firstChild.nodeValue = text;
    pic.setAttribute("src",source);
    return true
}

function preparePreview ()
{
    if (!document.getElementsByTagName || !document.getElementById) return false;
    if (!document.getElementById("preview")) return false;
    var previews = document.getElementById("preview");
    var links = previews.getElementsByTagName("a");
    for (var i=0; i<links.length; i++)
    {
        links[i].onclick = function()
        {
            return changePic(this) ? false : true;
        }
    }
}

function showPic (whichpic)
{
    if (!document.getElementsByTagName || !document.getElementById) return false;
    var source = whichpic.getAttribute("href");
    var text = whichpic.getAttribute("title");
    var pic = document.getElementById("picture");
    var des = document.getElementById("description");
    des.firstChild.nodeValue = text;
    pic.setAttribute("src", source);
}

function popUp (winURL)
{
    if (!document.getElementsByTagName || !document.getElementById) return false;
    if (!document.getElementById("picture")) return false;    
    var previewpic = document.getElementById("picture");
    var picURL = previewpic.getAttribute("src")
    window.open(picURL, "popup", "width=320,height=480");
    return true
}

function prepareLinks ()
{
    if (!document.getElementsByTagName) return false;
    var links = document.getElementsByTagName("a");
    for (var i=0; i<links.length; i++)
    {
        if (links[i].getAttribute("class") == "popup")
        {
            links[i].onclick = function()
            {
                return popUp(this.href) ? false : true;
            }
        }
    }
}

function addLoadEvent (func)
{
    var oldonload = window.onload;
    if (typeof window.onload != 'function')
    {
        window.onload = func;
    }
    else
    {
        window.onload = function()
        {
            oldonload();
            func();
        }
    }
}

addLoadEvent(prepareLinks);
addLoadEvent(preparePreview);