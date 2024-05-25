
// start date & time
function updateClock() {
  var sundte = new Date();
  var hours = sundte.getHours();
  var minutes = sundte.getMinutes();
  var seconds = sundte.getSeconds();

  document.getElementById("time").innerHTML = "ساعت " + hours + ":" + minutes + ":" + seconds;
}

// Call updateClock every second (1000 milliseconds)
setInterval(updateClock, 1000);


var sundte = new Date();
var yeardte = sundte.getFullYear();
var monthdte = sundte.getMonth();
var dtedte = sundte.getDate();
var daydte = sundte.getDay();
var sunyear;

switch (daydte) {
  case 0:
    var today = "يکشنبه";
    break;
  case 1:
    var today = "دوشنبه";
    break;
  case 2:
    var today = "سه شنبه";
    break;
  case 3:
    var today = "چهارشنبه";
    break;
  case 4:
    var today = "پنجشنبه";
    break;
  case 5:
    var today = "جمعه";
    break;
  case 6:
    var today = "شنبه";
    break;
}
switch (monthdte) {
  case 0:
    sunyear = yeardte - 622;
    if (dtedte <= 20) {
      var sunmonth = "دي";
      var daysun = dtedte + 10;
    } else {
      var sunmonth = "بهمن";
      var daysun = dtedte - 20;
    }
    break;
  case 1:
    sunyear = yeardte - 622;
    if (dtedte <= 19) {
      var sunmonth = "بهمن";
      var daysun = dtedte + 11;
    } else {
      var sunmonth = "اسفند";
      var daysun = dtedte - 19;
    }
    break;
  case 2:
    {
      if ((yeardte - 621) % 4 == 0) var i = 10;
      else var i = 9;
      if (dtedte <= 20) {
        sunyear = yeardte - 622;
        var sunmonth = "اسفند";
        var daysun = dtedte + i;
      } else {
        sunyear = yeardte - 621;
        var sunmonth = "فروردين";
        var daysun = dtedte - 20;
      }
    }
    break;
  case 3:
    sunyear = yeardte - 621;
    if (dtedte <= 20) {
      var sunmonth = "فروردين";
      var daysun = dtedte + 11;
    } else {
      var sunmonth = "ارديبهشت";
      var daysun = dtedte - 20;
    }
    break;
  case 4:
    sunyear = yeardte - 621;
    if (dtedte <= 21) {
      var sunmonth = "ارديبهشت";
      var daysun = dtedte + 10;
    } else {
      var sunmonth = "خرداد";
      var daysun = dtedte - 21;
    }

    break;
  case 5:
    sunyear = yeardte - 621;
    if (dtedte <= 21) {
      var sunmonth = "خرداد";
      var daysun = dtedte + 10;
    } else {
      var sunmonth = "تير";
      var daysun = dtedte - 21;
    }
    break;
  case 6:
    sunyear = yeardte - 621;
    if (dtedte <= 22) {
      var sunmonth = "تير";
      var daysun = dtedte + 9;
    } else {
      var sunmonth = "مرداد";
      var daysun = dtedte - 22;
    }
    break;
  case 7:
    sunyear = yeardte - 621;
    if (dtedte <= 22) {
      var sunmonth = "مرداد";
      var daysun = dtedte + 9;
    } else {
      var sunmonth = "شهريور";
      var daysun = dtedte - 22;
    }
    break;
  case 8:
    sunyear = yeardte - 621;
    if (dtedte <= 22) {
      var sunmonth = "شهريور";
      var daysun = dtedte + 9;
    } else {
      var sunmonth = "مهر";
      var daysun = dtedte + 22;
    }
    break;
  case 9:
    sunyear = yeardte - 621;
    if (dtedte <= 22) {
      var sunmonth = "مهر";
      var daysun = dtedte + 8;
    } else {
      var sunmonth = "آبان";
      var daysun = dtedte - 22;
    }
    break;
  case 10:
    sunyear = yeardte - 621;
    if (dtedte <= 21) {
      var sunmonth = "آبان";
      var daysun = dtedte + 9;
    } else {
      var sunmonth = "آذر";
      var daysun = dtedte - 21;
    }

    break;
  case 11:
    sunyear = yeardte - 621;
    if (dtedte <= 19) {
      var sunmonth = "آذر";
      var daysun = dtedte + 9;
    } else {
      var sunmonth = "دي";
      var daysun = dtedte + 21;
    }
    break;
}
document.getElementById("demo").innerHTML =
  "امروز: " +
  today +
  "&nbsp;" +
  [daysun + 1] +
  "&nbsp;" +
  sunmonth +
  "&nbsp;" +
  sunyear +
  " ";

// end date & time

// show alert for comment form
document.getElementById('commentForm').addEventListener('submit', function(e) {
    // Prevent the default form submission behavior
    e.preventDefault();

    // Get all form fields
    var formFields = this.elements;

    // Flag to track if any field is empty
    var isAnyFieldEmpty = false;

    // Loop through each form field
    for (var i = 0; i < formFields.length; i++) {
        // Check if the field is an input element and if it's empty
        if (formFields[i].nodeName === 'INPUT' && !formFields[i].value.trim()) {
            // Set flag to true if any field is empty
            isAnyFieldEmpty = true;
            break; // No need to continue checking once an empty field is found
        }
    }

    // If any field is empty, show an alert
    if (isAnyFieldEmpty) {
        alert('لطفا هر دو فیلد را تکمیل نمایید.');
    } else {
        // If all fields are filled, show a success message
        alert('ممنونم که به ارسال نظر اهمیت دادین !');

        // Optionally, submit the form after showing the alert
        this.submit();
    }
});
// show alert for comment form




