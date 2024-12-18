const form = document.querySelector("form");
const fullname = document.getElementById("name");
const email = document.getElementById("email");
const phone = document.getElementById("phone");
const subject = document.getElementById("subject");
const message = document.getElementById("message");



function sendEmail() {
    const bodyMessage = `Full Name: ${fullname.value}<br> Email: ${email.value}<br> Phone: ${phone.value}<br> Subject: ${"Новое сообщение с сайта"}<br> Message: ${message.value}<br>`;

    Email.send({
        SecureToken: "0b65f793-ff3d-4435-b296-573d823a2c86",
        To : 'art.pointqa@gmail.com',
        From : "art.pointqa@gmail.com",
        Subject : "Новое сообщение с сайта",
        Body : bodyMessage
    }).then(
      message => {
        if (message == "OK") {
            Swal.fire({           
                title: "Thank you for your time!",
                text: "Message sent successfully",
                icon: "success",
                width: '500px',
                customClass: {
                    popup: 'swal-popup-large'
                  }
              });
        }
      }
    );
}

function checkInputs() {
  const items = document.querySelectorAll(".item");

  for(const item of items) {
    if(item.value == "") {
      item.classList.add("error");
      item.parentElement.classList.add("error");
    }

    if(items[1].value != "") {
      checkEmail();
    }

    items[1].addEventListener("keyup", () => {
      checkEmail();
    });

    item.addEventListener("keyup",() => {
      if(item.value !="") {
        item.classList.remove("error");
        item.parentElement.classList.remove("error");
      }
      else {
        item.classList.add("error");
        item.parentElement.classList.add("error");
      }
    });
  }
}

function checkEmail() {
  const emailRemex = /^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,3})(\.[a-z]{2,3})?$/;
  const errorTxtEmail = document.querySelector(".error-txt.email");

  if (!email.value.match(emailRemex)) {
    email.classList.add("error");
    email.parentElement.classList.add("error");

    if(email.value != "") {
      errorTxtEmail.innerText = "Enter a valid email adress";
    }
    else {
      errorTxtEmail.innerText = "Email can't be blank";
    }
  }
  else {
    email.classList.remove("error");
    email.parentElement.classList.remove("error");
  }
}


form.addEventListener("submit", (e) => {
    e.preventDefault();
    checkInputs();

    if(!fullname.classList.contains("error") && 
    !email.classList.contains("error") && !phone.classList.contains("error") && !subject.classList.contains
    ("error") && !message.classList.contains("error")) {
      sendEmail();

      form.reset();
      return false;
   } 

});
