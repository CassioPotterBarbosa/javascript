var c=0
var n=100

while(n<20000){
    c=c+1
    n=n+(n/100*15)
    console.log("-----")
    console.log(c)
    console.log(n)
}