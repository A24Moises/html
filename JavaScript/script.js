
function addTime(){
    let add= document.getElementById("add");
    if(count.innerText==0){
        count.innerText=1;
    }else{
        count.innerText++;
    }
}
function lessTime(){
    let less= document.getElementById("less");
    if(count.innerText==0){
        count.innerText=-1;
    }else{
        count.innerText--;
    }
}
function resetTime(){
    let reset= document.getElementById("reset");

    reset.style.color="black";
    count.innerText=0;
}
