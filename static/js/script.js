const toTop = document.querySelector(".scroll-to-top");

window.addEventListener("scroll", () => {
    if (window.pageYOffset > 100) {
        toTop.classList.add("active");
    } else {
        toTop.classList.remove("active");
    }
})


const slogan = document.querySelector("#slogan-text");
const strSlogan = slogan.textContent;
const splitSlogan = strSlogan.split("");
slogan.textContent = "";
for (let i=0; i < splitSlogan.length; i++){
    slogan.innerHTML += "<span>" + splitSlogan[i] +"</span>";
}

let character =0;
let timer = setInterval(onTick, 50);

function onTick(){
    const span = slogan.querySelectorAll("span")[character]
    span.classList.add("reveal");
    character++;
    if (character === splitSlogan.length) {
        complete();
        return;
    }
}

function complete(){
    clearInterval(timer);
    timer = null;
}
