<script src="/textshare/media/js/lib/socket.io.js" type="text/javascript"></script>
<script>
var socket = io.connect('http://localhost:8080');
socket.on('textchange', function (data) {
		document.getElementById("note_text").innerHTML = data;
	});
</script>