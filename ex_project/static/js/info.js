window.onload = function(){
    let btn = document.getElementById("btn");

    btn.addEventListener('click', show_msg);
}

function show_msg(){
    alert('제주도!!');
}