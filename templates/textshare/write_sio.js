<script src="/textshare/media/js/lib/socket.io.js" type="text/javascript"></script>
<script>
function send_text(){
	var socket = io.connect('http://localhost:8080');
	socket.emit('textchange', document.getElementById("note_text").innerHTML);
}
</script>