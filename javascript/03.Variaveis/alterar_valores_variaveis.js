a = 10
b = 20
c = null

document.write("<h2>A = " + a + "</h2>")
document.write("<h2>B = " + b + "</h2>")
document.write("<h2>C = " + c + "</h2>")
document.write("<hr>")

c = a
a = b
b = c
c = null

document.write("<h2>A = " + a + "</h2>")
document.write("<h2>B = " + b + "</h2>")
document.write("<h2>C = " + c + "</h2>")
