const toTop = document.querySelector(".scroll-to-top");

/* Scroll to top */
window.addEventListener("scroll", () => {
    if (window.pageYOffset > 100) {
        toTop.classList.add("active");
    } else {
        toTop.classList.remove("active");
    }
});


/* Slogan */
if(window.location.pathname == '/') {
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
    const span = slogan.querySelectorAll("span")[character];
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
}



/* Admin Booking Table Status Converter */
if(window.location.pathname == '/bookings/admin-all') {
    var tableStatus = document.getElementsByClassName('booking-status');

    for (var i = 0; i < tableStatus.length; ++i) {
        console.log(tableStatus[i].innerHTML);
        if (tableStatus[i].innerHTML == "0"){
            newStatus = "Pending";
            updateStatusPending(newStatus);
        } else if (tableStatus[i].innerHTML == "1"){
            newStatus = "Approved";
            updateStatusApproved(newStatus);
        }
    }

    function updateStatusPending(newStatus){
        tableStatus[i].innerHTML = newStatus;
        approveBooking();
    }

    function updateStatusApproved(newStatus){
        tableStatus[i].innerHTML = newStatus;
    }

    /* Add approve booking button to pending bookings*/
    function approveBooking(){
        let approveButton = document.getElementsByClassName("approve-booking");
        approveButton[i].classList.add("reveal");
    }
}