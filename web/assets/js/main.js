$(function() {
  var $btn = $('#btn-replace');
	// select text on focus for easier copying
	$('#link-html, #text, #input-link').focus(function(e) {
		$(this).select();
	});

  $btn.click(function() {
    //console.log('button clicked');
    var data = $('#link-html').val();
    $.post("/replace-links", { text: data })
      .done(function(resp) {
        $('#link-html').val(resp);
      })
      .fail(function() {
        // do error stuff
        console.error('stuff failed!');
      });
  });
  // button for fetching pageID
  $('#btn-fetchlink, #btn-fetchid').click(function(e) {
		e.preventDefault();
		var data = $('#input-link').val();
	  $.post("/get-page-id", { 'input-link': data })
	    .done(function(resp) {
				console.log(e.target.id);
				var baseUrl = "https://de.trotec.com/";
				var val = e.target.id == "btn-fetchlink" ? baseUrl + "?id=" + resp : resp;
	      $('#input-link').val(val);
				// TODO: fix - broken
				var clipboard = new Clipboard('#btn-fetchlink, #btn-fetchid', {
				    text: function(trigger) {
							console.log(trigger);
				      return $('#input-link').val();
				    }
				});
				clipboard.destroy();
	    })
	    .fail(function() {
	      // do error stuff
	      console.error('fetching link failed!');
	    });
  })
	
	var linkfetchCallback = function() {
		
	};

	// Clipboard.js init
	var clipboard = new Clipboard('#btn-replace, #btn-js-replace');
    clipboard.on('success', function(e) {
		$('.alert').fadeIn('slow', function() {
			window.setTimeout(function() { $('.alert').fadeOut('slow'); }, 3000 );	
		});	
					
    });
    clipboard.on('error', function(e) {
      console.log(e);
    });

});
