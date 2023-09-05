$(document).ready(function () {
    // Attach a click event handler to the "SIGNUP" button
    $("#header-signup").click(function () {
        redirectToSignup(); // Call the redirectToSignup function
    });
    // Attach a click event handler to the "LOGIN" button
    $("#header-login").click(function () {
        redirectToLogin(); // Call the redirectToLogin function
    });

});
function redirectToSignup() {
    window.location.href = '/signup'; // Redirect to the signup route
}
function redirectToLogin(){
    window.location.href = '/login'; // Redirect to the login route
}