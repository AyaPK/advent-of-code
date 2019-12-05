
var fs = require("fs");
var text = fs.readFileSync("./input.txt", "utf-8");
var textByLine = text.split("\n")

output = []
textByLine.forEach(a=>output.push(Math.floor(a/3)-2))
console.log(output.reduce((a,b)=>a+b))

