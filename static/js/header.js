$(document).ready(function () {
    // Attach a click event handler to the "SIGNUP" button
    $("#header-signup").click(function () {
        redirectToSignup(); // Call the redirectToSignup function
    });

});
function redirectToSignup() {
    window.location.href = '/signup'; // Redirect to the signup route
}