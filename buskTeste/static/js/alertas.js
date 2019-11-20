function sendRegisterBook() {
  document.formResgisterBook.submit();
}

function sendUpdateBook() {
  document.formUpdateBook.submit();
}

function showSuccess() {
  Swal.fire({
    'title': 'Cadastrado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
  })
}

function validBookForm() {
  let valid = true;
  if (document.getElementById('isbn').value == "") {
    console.log('1');
    valid = false;
  } else if (document.getElementById('titulo').value == "") {
    console.log('2');
    valid = false;
  } else if (document.getElementById('subtitulo').value == "") {
    console.log('3');
    valid = false;
  } else if (document.getElementById('autor').value == "") {
    console.log('4');
    valid = false;
  } else if (document.getElementById('editora').value == "") {
    console.log('5');
    valid = false;
  } else if (document.getElementById('edicao').value == "") {
    console.log('6');
    valid = false;
  } else if (document.getElementById('ano').value == "") {
    console.log('7');
    valid = false;
  } else if (document.getElementById('paginas').value == "") {
    console.log('8');
    valid = false;
  } else if (document.getElementById('genero').value == "") {
    console.log('9');
    valid = false;
  } else if (document.getElementById('preco_compra').value == "") {
    console.log('10');
    valid = false;
  } else if (document.getElementById('preco_venda').value == "") {
    console.log('11');
    valid = false;
  } else if (document.getElementById('quantidade').value == "") {
    console.log('12');
    valid = false;
  } else if (document.getElementById('sinopse').value == "") {
    console.log('13');
    valid = false;
  }
  return valid;
}