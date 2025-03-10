function changeColor(){
    let h1=document.getElementById(heading1);
    alert(heading1.textContent);
    heading1.style.color="red";
}

function changeBgColor(){
    let h2=document.getElementById(heading2);
    heading2.classList.add('bg-danger');    
}

function resetBgColor(){
    heading2.classList.remove('bg-danger');    
}

function putText(){
    let info=document.getElementById("info");
    info.textContent="This page is loaded";
}

function changeParagraph(){
    let paras=document.getElementsByTagName("p");
    for (let index = 0; index < paras.length; index++) {
        const element = paras[index].innerText="Changed " + index;
    };
}

function changeCase(){
    let name=document.getElementById("name");
    let p3=document.getElementById("p3");
    p3.innerText=name.value.toUpperCase();
}

function changeFontSize(){
    let p4=document.getElementById("p4");
    p4.classList.add("fs-1");
    p4.innerHTML="<span class='text-danger' >Hello</span> Mr.Marshall";
}

function loadUserName(){
    let user1=document.getElementById("user1");
    let num=Math.floor(Math.random()*10);
    fetch('https://jsonplaceholder.typicode.com/users')
        .then(response => response.json())
        .then(data => user1.innerText=data[num].name)
}