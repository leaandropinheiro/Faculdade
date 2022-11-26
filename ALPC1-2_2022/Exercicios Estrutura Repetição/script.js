/*(REPETIÇÃO6) Elaborar um programa que efetue a leitura de 10 valores numéricos e 
apresente no final o total do somatório e a média do total.*/

/*let contador = 0;
const numeros = []

while(contador < 10){
    const numero = Number(prompt("Digite qualquer numero:"))
    numeros.push(numero)
    contador += 1;
    console.log(numeros)
    console.log(contador)
}
const soma = numeros.reduce((a,v)=> a+v)
const media = soma / numeros.length
console.log(soma, media)*/


const frase = document.createElement("p")
const bnt = document.querySelector(".botao")


bnt.appendChild(frase)


bnt.style.width="400px"
bnt.style.height="400px"
frase.style.fontSize="25px"


bnt.onclick = () => {
    bnt.className="botao2"
    frase.innerText="Olá"

} 

console.log(bnt)