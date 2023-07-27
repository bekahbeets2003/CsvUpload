// add date event listeners
function add_date_event_listeners(date_input){
    date_input.addEventListener("blur", function() {
      validateDateRange(this);
    });

    date_input.addEventListener("change", function() {
      validateDateRange(this);
    });
}

//add file event listeners
function add_file_event_listeners(file_input){
    /*file_input.addEventListener("blur", function() {
        validateFileExt(file_input, 'csv');
    });*/

    file_input.addEventListener("change", function() {
       validateFileExt(file_input, 'csv');
    });
}


function set_welcome_message(json_user){
    let fname = json_user[1];
    let lname = json_user[3];

    document.querySelector(".welcome-message").textContent = 'Welcome, ' + fname + ' ' + lname + '!';
}

function set_user_id(user){
    const user_input = document.getElementById("user_id");
    user_input.value = user[0].toString();
}

function load_vendors_dd(json_vendors){
  const options = [];
  options.push('<option value="">Select...</option>');

  for (const i in json_vendors) {
    options.push('<option value="' + json_vendors[i][0] + '">' + json_vendors[i][1] + '</option>');
  }
  document.querySelector("#dropDownVendors").innerHTML = options.join("");
}

// Validate the date to the last 10 years
function validateDateRange(date_input) {
  let retVal = true;

  const date = new Date(date_input.value);
  let minDate = new Date(date_input.min);
  let maxDate = new Date(date_input.max);

  const invalid_div = document.getElementById("date_custom_validation");
  if (date < minDate || date > maxDate) {
    invalid_div.textContent = 'Date must be between today and 10 years ago';
    invalid_div.classList.remove('d-none');
    date_input.setCustomValidity("Please enter a date between 2013 and today");
    return false;
  }
  else{
    invalid_div.textContent = '';
    invalid_div.classList.add('d-none');
  }

  return retVal;
}

// validate user selected the correct file type
function validateFileExt(file_input, file_ext){
  let retVal = true;
  const file = file_input.files[0];
  const ext = file.name.split(".")[1];

  const invalid_div = document.getElementById("file_custom_validation");


  if (ext !== file_ext) {
    file_input.focus();
    invalid_div.textContent = 'File type must be csv';
    invalid_div.classList.remove('d-none');
    return false;
  }
  else {
    invalid_div.textContent = '';
    invalid_div.classList.add('d-none');  }

  return retVal;
}

function set_submit_button_listeners(date_input, file_input, submit_btn){
    let x = 0;
    submit_btn.addEventListener("click", function() {

        if (!validateDateRange(date_input)) {return false;};

        if (!validateFileExt(file_input, 'csv')) {return false;};

        // if all validation checks return true
        return confirm('Do you want to submit this file?');
    });
}