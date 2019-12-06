
var fs = require("fs");
var text = fs.readFileSync("./input.txt", "utf-8");
var textByLine = text.split("\n")

var output = []

function calc(x){
    var temparray = []
    while(x > 0){
        x = Math.floor(x/3)-2
        temparray.push(x)
    }
    return temparray.reduce((a,b)=>a+b)
}

textByLine.forEach(a=>output.push(calc(a)))
console.log(output.reduce((a,b)=>a+b))