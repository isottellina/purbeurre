function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function saveProduct(orig_product, sub_product) {
    $.post("/product/save", {
	"orig_product": orig_product,
	"sub_product": sub_product
    });
}

// Prevent all defaults
(function() {
    // Set up the protection against CSRF
    var csrftoken = Cookies.get('csrftoken');
    
    $.ajaxSetup({
	beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
	}
    });
    
    window.addEventListener("load", function() {
	$(".save-link").click(function(event) {
	    event.preventDefault();
	});
    });
})();
