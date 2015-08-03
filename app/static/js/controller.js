ERROR_USER_EXISTS='ERROR_USER_EXISTS'
ERROR_INVALID_VALUES='ERROR_INVALID_VALUES'

KEY_EMAIL='KEY_EMAIL'


function submitNewApplication()
{
	$('#form').parsley().validate();
	if($('#form').parsley().isValid()) {

		window.sessionStorage.setItem(KEY_EMAIL,document.getElementById('email').value);

		$.ajax({
	    url: '/new_applicant',
	    type: 'POST',
	    data:  $('form').serialize(),
	    success: function(result) { 
	    	if(result==ERROR_USER_EXISTS) {alert('An entry with this email-id / phone-number already exists.\n Please recheck these fields.')} 
	    	else if(result==ERROR_INVALID_VALUES) {alert('Some of these values are ivalid. Please recheck them.')}
	    	else { document.documentElement.innerHTML=result; }
	    }
		});
	}
}


function submitAnswers()
{
	$('#qform').parsley().validate();
	if($('#qform').parsley().isValid()) {
		email = window.sessionStorage.getItem(KEY_EMAIL);
		$.ajax({
	    url: '/update_answers/'+encodeURIComponent(email),
	    type: 'POST',
	    data:  $('form').serialize(),
	    success: function(result) { document.documentElement.innerHTML=result;}
		});
	}
}


function submitBgcheck() {

	var res = confirm("By clicking 'Okay', you'll be providing Instacart the permission to do a background check.");
	if (res == true) {
		email = window.sessionStorage.getItem(KEY_EMAIL);	    
	    $.ajax({
	    url: '/submit_bgcheck/'+encodeURIComponent(email),
	    type: 'POST',
	    data:  $('form').serialize(),
	    success: function(result) { document.documentElement.innerHTML=result;}
		});
	} else {
	    alert('A Background Check is mandatory. Visit this link to learn more https://en.wikipedia.org/wiki/Background_check')
	}
}