"use strict";

var nbrSms = 0;
var lu = 0;
var green = true;
var listSms = [];
var limitSms = 3;

function loadSms() {
    $.ajax({
        method: "GET",
        url: "/sms"
    }).done(function( msg ) {
        listSms = msg;
    });
}

function writeSms() {
    if (listSms.length == 0 || lu >= listSms.length) return;
    var m = (green) ? '<div class="greenMessage"><p>'+listSms[lu]+'</p></div>' : '<div class="grayMessage"><p>'+listSms[lu]+'</p></div>';

    var text = $("#messages").html();
    var ltext = text.split("</div>");
    ltext.splice(ltext.length-1, 1);
    if (ltext.length >= limitSms) {
        text = "";
        for (var i = ltext.length-limitSms+1 ; i < ltext.length ; i++)
            text += ltext[i]+"</div>";
    }
    $("#messages").html(text+m);

    lu++;
    green = !green;
}

loadSms();
setInterval(loadSms, 1000);
writeSms();
setInterval(writeSms, 2000);

var photo = 0;
var listPhoto = [];

function loadImg() {
    $.ajax({
        method: "GET",
        url: "/photo"
    }).done(function( msg ) {
        listPhoto = msg;
    });
}

function writePhoto() {
    if (listPhoto.length == 0 || photo >= listPhoto.length) return;
    $("section").css("background-image", 'url("'+listPhoto[photo]+'")');
}

loadImg();
setInterval(loadImg, 1000);
writePhoto();
setInterval(writePhoto, 2000);