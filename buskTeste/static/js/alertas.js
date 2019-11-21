function sendRegisterBook() {
  document.formResgisterBook.submit();
}

function sendUpdateBook() {
  document.formUpdateBook.submit();
}

function sendDeleteBook() {
  document.formDeleteBook.submit();
}

function showSuccessRegister() {
  Swal.fire({
    'title': 'Livro Cadastrado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}

function showSuccessDelete() {
  Swal.fire({
    'title': 'Livro Excluído com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}

function showSuccessUpdate() {
  Swal.fire({
    'title': 'Livro Atualizado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}
