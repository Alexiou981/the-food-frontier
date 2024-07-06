// Code taken from Codestar walkthrough by Code Institute
// Gets detele modal and delete button 
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");

// Modal appears when delete button is clicked 
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        deleteModal.show();
    });
}