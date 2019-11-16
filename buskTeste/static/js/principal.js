//Coded by OFS - Group (Since 2019)

function openPage(evt, pageMoment) {
    let tabcontent = document.getElementsByClassName("tabcontent");
    for (let i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    let tablinks = document.getElementsByClassName("tablinks");
    for (let i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(pageMoment).style.display = "block";
    evt.currentTarget.className += " active";
  }
  document.getElementById("defaultopenPage").click();


function openOptionBook(evt, pageBook) {
  let livroContent = document.getElementsByClassName("livroContent");
    for (let i = 0; i < livroContent.length; i++) {
      livroContent[i].style.display = "none";
    }
    let $btnBook = document.getElementsByClassName("btn-book");
    for (let i = 0; i < $btnBook.length; i++) {
      $btnBook[i].className = $btnBook[i].className.replace(" activeButton", "");
    }
    document.getElementById(pageBook).style.display = "block";
    evt.currentTarget.className += " activeButton";
  }
  document.getElementById("defaultBook").click();

function openOptionCliente(evt, pageCliente) {
  let clienteContent = document.getElementsByClassName("clienteContent");
    for (let i = 0; i < clienteContent.length; i++) {
      clienteContent[i].style.display = "none";
    }
    let $btnCliente = document.getElementsByClassName("btn-cliente");
    for (let i = 0; i < $btnCliente.length; i++) {
      $btnCliente[i].className = $btnCliente[i].className.replace(" activeButton", "");
    }
    document.getElementById(pageCliente).style.display = "block";
    evt.currentTarget.className += " activeButton";
  }
  document.getElementById("defaultCliente").click();

function openOptionEmprestimo(evt, pageEmprestimo) {
  let emprestimoContent = document.getElementsByClassName("emprestimoContent");
    for (let i = 0; i < emprestimoContent.length; i++) {
      emprestimoContent[i].style.display = "none";
    }
    let $btnEmprestimo = document.getElementsByClassName("btn-emprestimo");
    for (let i = 0; i < $btnEmprestimo.length; i++) {
      $btnEmprestimo[i].className = $btnEmprestimo[i].className.replace(" activeButton", "");
    }
    document.getElementById(pageEmprestimo).style.display = "block";
    evt.currentTarget.className += " activeButton";
  }
  document.getElementById("defaultEmprestimo").click();

function openOptionCompra(evt, pageCompra) {
  let compraContent = document.getElementsByClassName("compraContent");
    for (let i = 0; i < compraContent.length; i++) {
      compraContent[i].style.display = "none";
    }
    let $btnCompra = document.getElementsByClassName("btn-compra");
    for (let i = 0; i < $btnCompra.length; i++) {
      $btnCompra[i].className = $btnCompra[i].className.replace(" activeButton", "");
    }
    document.getElementById(pageCompra).style.display = "block";
    evt.currentTarget.className += " activeButton";
  }
  document.getElementById("defaultCompra").click();
  