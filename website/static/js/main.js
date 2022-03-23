$(function () {

    $(".services__inner").on("click","a", function (event) {
        //отменяем стандартную обработку нажатия по ссылке
  

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
    prevArrow:'<button type="button" class=" slick-arrow slick-prev"><img src="images/small_spb/Arrow-left.svg"></button>',
    nextArrow:'<button type="button" class="slick-arrow slick-next"><img src="images/small_spb/Arrow-riht.svg"></button>',
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
  $('.about__item-img').click(function(event) {
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
  function trackScroll() {
        var scrolled = window.pageYOffset;
        var coords = document.documentElement.clientHeight;

        if (scrolled > coords) {
            goTopBtn.classList.add('back_to_top-show');
        }
        if (scrolled < coords) {
            goTopBtn.classList.remove('back_to_top-show');
        }
    }

    function backToTop() {
        if (window.pageYOffset > 0) {
            window.scrollBy(0, -150);
            setTimeout(backToTop, 0);
        }
    }

    var goTopBtn = document.querySelector('.back_to_top');

    window.addEventListener('scroll', trackScroll);
    goTopBtn.addEventListener('click', backToTop);




});


