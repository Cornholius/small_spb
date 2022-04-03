$(function () {

    $(".services__inner").on("click","a", function (event) {
        
  

        //забираем идентификатор бока с атрибута href
        var id  = $(this).attr('href'),

        //узнаем высоту от начала страницы до блока на который ссылается якорь
            top = $(id).offset().top;
        
        //анимируем переход на расстояние - top за 1000 мс
        $('body,html').animate({scrollTop: top}, 1000);
    });


    $(".news__item").each(function() {
      let hide = $(this).find(".news__wrapper")
      $('.news-button', this).click(function(){

        hide.toggleClass('news__wrapper--height');  
        if (hide.hasClass('news__wrapper--height')) {
          $(this).html('Скрыть');
        } else {
         $(this).html('Полный текст')
       }   
       return false;

     }); 


    }); 
    $('.menu__btn').on('click', function () {
        $('.menu__list').toggleClass('menu__list--active')
    });

    $('.services__slider').slick({
 

  slidesToShow: 5,
  swipe:false,
  dots:false,
    prevArrow:'<button type="button" class=" slick-arrow slick-prev"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M16 7H3.8L9.4 1.4L8 0L0 8L8 16L9.4 14.6L3.8 9H16V7Z" fill="#FAFAFA"/></svg></button>',
    nextArrow:'<button type="button" class="slick-arrow slick-next"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M0 7H12.2L6.6 1.4L8 0L16 8L8 16L6.6 14.6L12.2 9H0V7Z" fill="#FAFAFA"/></svg></button>',
  responsive: [
{
      breakpoint: 1200,
      settings: {
        arrows: true,
        swipe:false,
        dots:false,
       
        slidesToShow: 3,
      }
    },


    {
      breakpoint: 768,
      settings: {
        arrows: false,
        swipe:true,
        dots: false,
       centerMode: false,
       
        slidesToShow: 2
      }
    },
    {
      breakpoint: 600,
      settings: {
        arrows: false,
        swipe:true,
        dots: false,
       slidesToShow: 1,
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        swipe:true,
        dots: false,
        
        slidesToShow: 1,
      }
    }
  ]
});
  $('.cart__item-img, .galery__item-img').click(function(event) {
    var i_path = $(this).attr('src');
    $('body').append('<div id="overlay"></div><div id="magnify"><img src="'+i_path+'"><div id="close-popup"><i></i></div></div>');
    $('#magnify').css({
     left: ($(document).width() - $('#magnify').outerWidth())/2,
     // top: ($(document).height() - $('#magnify').outerHeight())/2 upd: 24.10.2016
            top: ($(window).height() - $('#magnify').outerHeight())/2
   });
    $('#overlay, #magnify').fadeIn('fast');
  });
  
  $('body').on('click', '#close-popup, #overlay', function(event) {
    event.preventDefault();
    $('#overlay, #magnify').fadeOut('fast', function() {
      $('#close-popup, #magnify, #overlay').remove();
    });
  });
  




});


