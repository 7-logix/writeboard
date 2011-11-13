<script src="/textshare/media/js/socket.io.js" type="text/javascript"></script>
<script type="text/javascript">
var socket = new io.Socket('localhost',{
	port: 8080
});
socket.connect();

socket.on('textchange', function (data) {
		document.getElementById("note_text").innerHTML = data;
	});
</script>