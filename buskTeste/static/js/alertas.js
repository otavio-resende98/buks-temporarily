function sendRegisterBook() {
  document.formResgisterBook.submit();
}

function sendUpdateBook() {
  document.formUpdateBook.submit();
}

function showSuccessRegister() {
  Swal.fire({
    'title': 'Cadastrado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}

function showSuccessUpdate() {
  Swal.fire({
    'title': 'Atualizado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}
