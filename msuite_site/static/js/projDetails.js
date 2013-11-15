$(document).ready(function(){
	
    $('.leaveComment').click(function (e) {
    	e.preventDefault();
        $("#commentBox").toggle(1000);
    });

});