document.addEventListener("DOMContentLoaded", function () {
    const uploadForm = document.getElementById("upload-form");
    const resultDiv = document.getElementById("result");

    uploadForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(uploadForm);

        // Send the image data to the server for processing and get the result
        fetch("/upload", {
            method: "POST",
            body: formData,
        })
        .then((response) => response.text())
        .then((data) => {
            resultDiv.innerHTML = data;
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    });
});
