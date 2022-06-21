$(document).ready(function(){

    var deleteBtn = $('.btn-danger');
  
    $(deleteBtn).on('click',function(e){
      e.preventDefault();
  
      var deleteLink = $(this).attr('href');
      var result = confirm('Deseja deletar esse Banco?');

      if(result){
        window.location.href = deleteLink;
      }
    });
  });