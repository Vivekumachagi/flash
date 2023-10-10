
    function addRegistrationNumber() {
        var container = document.getElementById("registration_number_container");
        var inputContainer = document.createElement("div");
        inputContainer.className = "registration-number-input";
        var input = document.createElement("input");
        input.name = "registration_numbers[]";
        input.type = "text";
        input.className="parents-stu-reg"
        input.required = true;
        var deleteButton = document.createElement("button");
        deleteButton.type = "button";
        deleteButton.className = "delete-button";

// Create the icon element
        var deleteIcon = document.createElement("i");
        deleteIcon.className = "fas fa-trash-alt";
        deleteButton.appendChild(deleteIcon);
        deleteButton.onclick = function() {
            deleteRegistrationNumber(deleteButton);
        };
        inputContainer.appendChild(input);
        inputContainer.appendChild(deleteButton);
        container.appendChild(inputContainer);
    }

    function deleteRegistrationNumber(button) {
        var inputContainer = button.parentElement;
        inputContainer.remove();
    }

    function updateFieldsVisibility() {
        var selectedRole = document.getElementById("user_role").value;
        var studentFields = document.getElementById("student_fields");
        var parentFields = document.getElementById("parent_fields");
        var facultyFields = document.getElementById("faculty_fields");

        if (selectedRole === "student") {
            studentFields.style.display = "block";
            parentFields.style.display = "none";
            facultyFields.style.display = "none";
        } else if (selectedRole === "faculty") {
            studentFields.style.display = "none";
            parentFields.style.display = "none";
            facultyFields.style.display = "block";
        } else if (selectedRole === "parent") {
            studentFields.style.display = "block";
            parentFields.style.display = "block";
            facultyFields.style.display = "none";
        } else {
            studentFields.style.display = "none";
            parentFields.style.display = "none";
            facultyFields.style.display = "none";
        }
    }

    // Trigger the updateFieldsVisibility function when the page loads.
    window.addEventListener("load", updateFieldsVisibility);

    // Listen for the change event on the user_role select element.
    document.getElementById("user_role").addEventListener("change", updateFieldsVisibility);
