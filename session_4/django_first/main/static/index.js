var formDelete = document.querySelectorAll(".form-delete");
var taskCheck = document.querySelectorAll(".task-check");
var formChange = document.querySelectorAll(".form-change");
var checkIcon = document.querySelectorAll(".check-icon");
var editIcon = document.querySelectorAll(".bxs-pencil");
var icon = document.querySelectorAll(".icon");
var content = document.querySelectorAll(".content");
var closeIcon = document.querySelectorAll(".bx-x");
var checkTick = document.querySelectorAll(".bx-check");
var changeText = document.querySelectorAll(".text-change");

var prevText = "";
var currentText = "";

formDelete.forEach((item) => {
  item.addEventListener("click", function () {
    item.submit();
  });
});

taskCheck.forEach((item) => {
  item.querySelector("input").addEventListener("click", function () {
    item.submit();
  });
});

editIcon.forEach((item, index) => {
  item.addEventListener("click", function () {
    icon[index].classList.add("showCheckIcon");
    content[index].setAttribute("contenteditable", true);
    prevText = content[index].innerHTML;

    closeIcon[index].addEventListener("click", function () {
      icon[index].classList.remove("showCheckIcon");
      content[index].setAttribute("contenteditable", false);
      content[index].innerHTML = prevText;
    });

    content[index].addEventListener("keyup", function () {
      currentText = content[index].textContent;
    });

    checkTick[index].addEventListener("click", function () {
      icon[index].classList.remove("showCheckIcon");
      content[index].setAttribute("contenteditable", false);
      changeText[index].value = currentText;
      content[index].innerHTML = currentText;

      formChange[index].submit();
    });
  });
});
