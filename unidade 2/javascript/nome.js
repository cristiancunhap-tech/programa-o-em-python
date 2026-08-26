const nome = prompt("Digite o seu nome: ");
const saudacao = "Bem vindo " + nome;

alert(saudacao);

const titulo = document.getElementById("nomeUsuario");
titulo.innerText = saudacao;
