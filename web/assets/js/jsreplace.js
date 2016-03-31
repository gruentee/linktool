document.onreadystatechange = function () {
  if (document.readyState == "complete") {
    document.getElementById('btn-js-replace')
      .addEventListener('click', replaceLinkTitles);
  }
}

var replaceLinkTitles = function() {
  var elTextarea = document.getElementById('text');
  var text = elTextarea.value;
  var html = document.createElement('div');
  html.innerHTML = text;
  var links = html.getElementsByTagName("a");
  // cache array length so it's not calculated for every iteration
    var i = links.length;
  for (i; i--;) {
    links[i].setAttribute('title', links[i].innerHTML);
  }
  elTextarea.value = html.innerHTML;
	destroy html;
}

