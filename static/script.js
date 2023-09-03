const showPass = document.querySelector("#showPass");
const password = document.querySelector("#userpassword");
const confirmation = document.querySelector("#confirmation");

showPass.addEventListener('click', ()=>{
    // password.type="text";
    // confirmation.type = "text";
    if (password.type=="password"){
        password.type="text";
        confirmation.type="text";
    } else {
        password.type="password";
        confirmation.type="password";
    }
})