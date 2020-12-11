(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space


$(document).ready(function(){


    $('#pro-sidenav-1').sidenav({edge:'right'});



    $('.tooltipped').tooltip();

    $('.modal').modal();
        //bookmark
    $('.bookmark').on('click',function(){
    if ($(this).text() == 'bookmark'){
        $(this).text('bookmark_border');
    }
    else{
        $(this).text('bookmark');
    }
    });

    //favorite
    $('.favorite').on('click',function(){
    if ($(this).text() == 'favorite'){
        $(this).text('favorite_border');
    }
    else{
        $(this).text('favorite');
    }
    });

    //share
    $('.share').on('click',function(){
        //document.write($(this).css('color'))
        if($(this).css('color') == 'rgba(0, 0, 0, 0.87)'){
            $(this).css('color','blue');
        }
        else{
            $(this).css('color','rgba(0, 0, 0, 0.87)');
        }

    });


});




