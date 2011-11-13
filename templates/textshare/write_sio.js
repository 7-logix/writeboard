<script src="/textshare/media/js/socket.io.js" type="text/javascript"></script>
<script type="text/javascript">
function send_text(){
	var socket = new io.Socket('localhost',{
		port: 8080
	});
	socket.connect();
	
	socket.emit('textchange', document.getElementById("note_text").innerHTML);
}
</script>