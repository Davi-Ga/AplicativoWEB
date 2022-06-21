$(document).ready(function(){

    var deleteBtn = $('.btn-danger');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-btn')
  
    $(deleteBtn).on('click',function(e){
      e.preventDefault();
  
      var deleteLink = $(this).attr('href');
      var result = confirm('Deseja deletar esse Banco?');

      if(result){
        window.location.href = deleteLink;
      }
    });

    $(searchBtn).on('click',function(){
        searchForm.submit();
    });
  });