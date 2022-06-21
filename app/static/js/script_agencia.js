$(document).ready(function(){

    var deleteBtn = $('.btn-danger');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form')
  
    $(deleteBtn).on('click',function(e){
      e.preventDefault();
  
      var deleteLink = $(this).attr('href');
      var result = confirm('Deseja deletar essa Agencia?');

      if(result){
        window.location.href = deleteLink;
      }
    });

    $(searchBtn).on('click',function(){
        searchForm.submit();
    });
  });