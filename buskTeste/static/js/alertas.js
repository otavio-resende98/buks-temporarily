//Função para Enviar o formulário do registro do livro
function sendRegisterBook() {
  document.formResgisterBook.submit();
}

//Função para Enviar o formulário da alteração do livro
function sendUpdateBook() {
  document.formUpdateBook.submit();
}

//Função para Enviar o ISBN de deleção do livro
function sendDeleteBook() {
  document.formDeleteBook.submit();
}

//Tela de Sucesso do cadastro
function showSuccessRegister() {
  Swal.fire({
    'title': 'Livro Cadastrado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}

//Tela de Sucesso da deleção
function showSuccessDelete() {
  Swal.fire({
    'title': 'Livro Excluído com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}

//Tela de Sucesso da alteração
function showSuccessUpdate() {
  Swal.fire({
    'title': 'Livro Atualizado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}