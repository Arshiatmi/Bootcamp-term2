var editIcon = document.querySelectorAll(".edit-icon");
var taskItemLeft = document.querySelectorAll(".task-item-left");
var closeIcon = document.querySelectorAll(".close-icon");
var taskText = document.querySelectorAll(".task-text");
var checkIcon = document.querySelectorAll(".check-icon");
var deleteIcon = document.querySelectorAll(".delete-icon");
var checkBoxButton = document.querySelectorAll(".checkbox-btn");
var checkTaskForm = document.querySelectorAll(".check-task-form");
var editTaskForm = document.querySelectorAll(".edit-task-form");
var deleteTaskForm = document.querySelectorAll(".delete-task-form");

var prevText = "";
var currentText = "";

for (let i = 0; i < checkTaskForm.length; i++) {
  checkBoxButton[i].addEventListener("click", function () {
    checkTaskForm[i].submit();
  });
}

for (let i = 0; i < editIcon.length; i++) {
  editIcon[i].addEventListener("click", function () {
    prevText = taskText[i].textContent;
    taskItemLeft[i].classList.add("activeSubmitEdit");
    taskText[i].setAttribute("contenteditable", true);

    taskText[i].addEventListener("keyup", function () {
      currentText = taskText[i].textContent;
    });

    closeIcon[i].addEventListener("click", function () {
      taskItemLeft[i].classList.remove("activeSubmitEdit");
      taskText[i].setAttribute("contenteditable", false);
      taskText[i].textContent = prevText;
    });

    checkIcon[i].addEventListener("click", function () {
      taskItemLeft[i].classList.remove("activeSubmitEdit");
      taskText[i].setAttribute("contenteditable", false);
      taskText[i].textContent = currentText;
      var textInput = editTaskForm[i].querySelector("input[name=text]");
      textInput.value = currentText;

      editTaskForm[i].submit();
    });
  });
}

for (let i = 0; i < deleteTaskForm.length; i++) {
  deleteIcon[i].addEventListener("click", function () {
    deleteTaskForm[i].submit();
  });
}