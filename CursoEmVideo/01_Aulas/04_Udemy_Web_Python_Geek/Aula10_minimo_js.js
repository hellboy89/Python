function gritar() {
    data = Date()
    alert(data);
    alert("Ahhhhhhhhhhhhhh");
}

function perguntar(params) {
    var nome;
    // Também é possível verificar pelo "inpetor de elementos" do navegador na aba de "console",
    // mostra o erro que está ocorrendo, caso alguma sintaxe escreva errado.
    nome = prompt("qual seu nome? ");
    alert("Olá " + nome)
}

function mudar_texto(params) {
    var h1 = document.getElementsByTagName("h1");

    if(h1[0].innerText == "Juan") {
        h1[0].innerText == "Evolua seu lado geek!";
    }
    else {
        h1[0].innerText = "Juan";
    }
}

function incrementar(params) {
    var p1 = document.getElementById("pl");
    //Valor abaixo "parseInt", serve para converter um valor para inteiro.
    pl.innerText = parseInt(pl.innerText) + 1;
}