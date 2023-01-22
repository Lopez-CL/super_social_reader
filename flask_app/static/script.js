$(document).ready(()=>{
    const $currentCard = $('.card');
    $('.reader-area').on('mouseover',event =>{
        $(event.currentTarget).addClass('active-box').on('mouseleave',event=>{
            $(event.currentTarget).removeClass('active-box');
        })
    })
    $('.route').on('mouseover', event =>{
        $(event.currentTarget).addClass('route-bg-active').on('mouseleave',event=>{
            $(event.currentTarget).removeClass('route-bg-active');
        });
    })
    $('.card').on('mouseover',event =>{
        $(event.currentTarget).addClass('active-box').on('mouseleave',event=>{
            $(event.currentTarget).removeClass('active-box');
        })
    })
    $('.post-text').on('keyup', event =>{
        $('post-text').focus();
        let post = $(event.currentTarget).val();
        let remaining = 255 - post.length;
        remaining <= 0? $('.count').css({
            color: 'red'
        }):''
        $('.characters').html(remaining);
    })
})