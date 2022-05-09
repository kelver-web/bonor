function removeMensagem(){
    setTimeout(function(){ 
        var msg = document.getElementById("fechar");
        msg.parentNode.removeChild(msg);   
    }, 3000);
}
document.onreadystatechange = () => {
    if (document.readyState === 'complete') {
      // toda vez que a página carregar, vai limpar a mensagem (se houver) 
      // após 5 segundos
        removeMensagem(); 
    }
};

