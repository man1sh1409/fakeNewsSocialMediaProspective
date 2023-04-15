let modalBtn=document.getElementById('btn-submit')
    modalBtn.addEventListener("submit",(e)=>{
    console.log('listinign event')
    e.preventDefault()
    res=0
    src=""
    let displayDiv=document.getElementById('show-res')
    let displaybtn=document.getElementById('dis-btn')
    displaybtn.style.display='block'
    var x = document.createElement("IMG");
    if(res){
        x.setAttribute("src", 'static/fail.gif');
    }
    else{
        x.setAttribute("src",src="static/success.gif")
    }
    x.setAttribute("width", "100%");
    x.setAttribute("height", "30%");
    x.setAttribute("alt", "The Pulpit Rock");
    displayDiv.appendChild(x);
    }






