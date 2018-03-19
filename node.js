"use strict";

const Express = require("express");
const Jsonfile = require("jsonfile");
const fs = require("fs");

var app = new Express();
    app.use(Express.static(__dirname+"/assets"));
    app.listen(8080);

    app.route("/")
        .get((req, res, next) => res.sendFile(__dirname+"/assets/index.html"));

    app.get("/sms", function (req, res, next) {
        var tab = [];
        var list = fs.readdirSync(__dirname+"/sms_valides");
        for (var i = 0 ; i < list.length ; i++)
            if (!/^.+\.json$/.test(list[i])) list.splice(i--, 1);
            else {
                var result = Jsonfile.readFileSync(__dirname+"/sms_valides/"+list[i]);
                tab.push(result);
            }
        res.json(tab);
    });

    app.get("/photo", function (req, res, next) {
        var tab = [];
        var list = fs.readdirSync(__dirname+"/assets/images_valides");
        for (var i = 0 ; i < list.length ; i++)
            if (!/^.+\.png$/.test(list[i])) list.splice(i--, 1);
            else tab.push("../images_valides/"+list[i]);
        res.json(tab);
    });