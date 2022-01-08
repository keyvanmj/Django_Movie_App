$(window).on('load', function () { // makes sure the whole site is loaded
    var status = $('#status');
    var preloader = $('#preloader');
    var body = $('body');
    status.fadeOut(); // will first fade out the loading animation
    preloader.delay(650).fadeOut('fast'); // will fade out the white DIV that covers the website.
    body.delay(650).css({'overflow': 'visible'});
    var vidDefer = document.getElementsByTagName('iframe');
    for (var i = 0; i < vidDefer.length; i++) {
        if (vidDefer[i].getAttribute('data-src')) {
            vidDefer[i].setAttribute('src', vidDefer[i].getAttribute('data-src'));
        }
    }
})
$(function () {
    'use strict';
    // js for dropdown menu
    var windowWidth = $(window).width();
    if (windowWidth > 1024) {
        var dropdown = $('.dropdown');
        dropdown.hover(
            function () {
                $(this).children('.dropdown-menu').fadeIn(300);
            },
            function () {
                $(this).children('.dropdown-menu').fadeOut(300);
            }
        );
    } else {
        var dropdownClick = $('.navbar a.dropdown-toggle');
        dropdownClick.on('click', function (e) {
            var $el = $(this);
            var $parent = $(this).offsetParent(".dropdown-menu");
            var $open = $('.nav li.open');
            $(this).parent("li").toggleClass('open');

            if (!$parent.parent().hasClass('nav')) {
                $el.next().css({"top": $el[0].offsetTop, "left": $parent.outerWidth() - 4});
            }
            $open.not($(this).parents("li")).removeClass("open");
            return false;
        });
    }
    //js for nav icon
    var clickMenubtn = $('#nav-icon1');
    clickMenubtn.on('click', function () {
        $(this).toggleClass('open');
    });
    //js for tabs
    var tabsClick = $('.tabs .tab-links input[type="radio"]+label,.tabs .tab-links a, .tab-links-2 input[type="radio"]+label,.tab-links-2 a, .tab-links-3 input[type="radio"]+label ,.tab-links-3 a');
    var multiItem = $('.slick-multiItem');
    var multiItem2 = $('.slick-multiItem2');
    tabsClick.on('click', function (e) {
        var currentAttrValue = $(this).attr('href') || $(this).attr('data-url_root');
        var tabsCurrent = $('.tabs ' + currentAttrValue);
        // Show/Hide Tabs
        tabsCurrent.show().siblings().hide();
        // Change/remove current tab to active
        $(this).parent('li').addClass('active').siblings().removeClass('active');
        e.preventDefault();
        //reset position for tabs
        multiItem.slick('setPosition');
        multiItem2.slick('setPosition');
    });

    // js for time count down
    function getTimeRemaining(endtime) {
        var t = Date.parse(endtime) - Date.parse(new Date());
        var seconds = Math.floor((t / 1000) % 60);
        var minutes = Math.floor((t / 1000 / 60) % 60);
        var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
        var days = Math.floor(t / (1000 * 60 * 60 * 24));
        return {
            'total': t,
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        };
    }

    function initializeClock(id, endtime) {
        var clock = document.getElementById(id);
        if (clock != null) {
            var daysSpan = clock.querySelector('.days');
            var hoursSpan = clock.querySelector('.hours');
            var minutesSpan = clock.querySelector('.minutes');
            var secondsSpan = clock.querySelector('.seconds');
            var updateClock = function () {
                var t = getTimeRemaining(endtime);

                daysSpan.innerHTML = t.days;
                hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
                minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
                secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

                if (t.total <= 0) {
                    clearInterval(timeinterval);
                }
            }
            updateClock();
            var timeinterval = setInterval(updateClock, 1000);
        }
    }

    var deadline = new Date(Date.parse(new Date()) + 25 * 24 * 60 * 60 * 1000);
    initializeClock('clockdiv', deadline);

    //js for twitter
    var tweets = jQuery(".tweet");
    jQuery(tweets).each(function (t, tweet) {
        var id = jQuery(this).attr('id');
        twttr.widgets.createTweet(
            id, tweet,
            {
                conversation: 'none',    // or all
                cards: 'hidden',  // or visible
                linkColor: 'default', // default is blue
                theme: 'light'    // or dark
            });
    });

    //slider for movie and tv show home 2
    multiItem2.slick({
        infinite: true,
        slidesToShow: 6,
        slidesToScroll: 6,
        arrows: false,
        // autoplay: true ,
        // autoplaySpeed: 2000,
        dots: true,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
    //slider movie and tv show home 1, 3
    multiItem.slick({
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 4,
        arrows: false,
        draggable: true,
        // autoplay: true,
        // autoplaySpeed: 2000,
        dots: true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
    //main slider home 1
    var multiItemSlider = $('.slick-multiItemSlider');
    multiItemSlider.slick({
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 4,
        arrows: false,
        draggable: true,
        autoplay: true,
        autoplaySpeed: 2000,
        dots: true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
    //slider for home v3 and home v2, twitter slider home 1, 2
    var singleItem = $('.slider-single-item');
    singleItem.slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        // autoplay: true,
        // autoplaySpeed: 2000,
        dots: true,
        draggable: true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true,
                    arrows: true
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                }
            }
        ]
    });
    //slider for tweeter
    var slickTw = $('.slick-tw');
    slickTw.slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        // autoplay: true,
        // autoplaySpeed: 2000,
        dots: true,
        draggable: true,
        arrows: false,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true,
                    arrows: false
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,

                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                }
            }
        ]
    });
    //for home v3
    var slidefor = $('.slider-for');
    var slidenav = $('.slider-nav');
    slidefor.slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav',
    });
    slidenav.slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: true,
        // centerMode: true,
        focusOnSelect: true,

        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    arrows: true
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: true
                }
            }
        ]
    });
    //for trailer v1 and 2
    var slidefor2 = $('.slider-for-2');
    var slidenav2 = $('.slider-nav-2');
    slidefor2.slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav-2',
    });
    slidenav2.slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.slider-for-2',
        dots: false,
        arrows: true,
        // centerMode: true,
        focusOnSelect: true,
        vertical: true,
        // autoplay: true,
        // autoplaySpeed: 2000
    });
    //== js for video lightbox
    var fancyboxmedia = $('.fancybox-media');
    fancyboxmedia.fancybox({
        openEffect: 'float',
        closeEffect: 'none',
        helpers: {
            media: {},
            overlay: {
                locked: false
            }
        }
    });
    //==js for show prev/next button in video lightbox
    fancyboxmedia
        .attr('rel', 'playlist')
        .fancybox({
            openEffect: 'none',
            closeEffect: 'none',
            prevEffect: 'none',
            nextEffect: 'none',
            helpers: {
                media: {}
            },
            youtube: {
                autoplay: 1,
                hd: 1,
                wmode: 'opaque', // shows X to close
                vq: 'hd720' // default 720p hd quality
            }
        });
    //== js for image lightbox
    var imglightbox = $(".img-lightbox");
    imglightbox.fancybox({
        helpers: {
            title: {
                type: 'float'
            },
            overlay: {
                locked: false
            }
        }
    });
    //== js for visibile next/prev fancybox
    imglightbox.fancybox({
        // loop: false, // gallery may not be cyclic
        afterShow: function () {
            // initialize some variables
            var gallerySize = this.group.length,
                next, prev;
            if (this.index == gallerySize - 1) {
                // this is the last element of the gallery so next is the first
                next = imglightbox.eq(0).attr("title"),
                    prev = imglightbox.eq(this.index - 1).attr("title");
            } else if (this.index == 0) {
                // this is the first image of the gallery so prev is the last
                next = imglightbox.eq(this.index + 1).attr("title"),
                    prev = imglightbox.eq(gallerySize - 1).attr("title");
            } else {
                // otherwise just add or substract to index
                next = imglightbox.eq(this.index + 1).attr("title"),
                    prev = imglightbox.eq(this.index - 1).attr("title");
            }
            // set title attributes to img-lightbox next/prev selectors
            var lightboxnext = $(".img-lightbox-next");
            var lightboxprev = $(".img-lightbox-prev");
            lightboxnext.attr("title", next);
            lightboxprev.attr("title", prev);
        }
    });

    // close popup for mobile
    var closebt = $(".close");
    closebt.on('click', function (e) {
        e.preventDefault();
        var overlay = $(".overlay");
        overlay.removeClass("openform");
    });
    //js for multi selected
    var multiselect = $(".ui.fluid.dropdown");
    multiselect.dropdown({
        allowLabels: true
    })
    multiselect.dropdown({'set selected': 'Role1,Role2'});
    //== scroll function for single page
    $(window).scroll(function (event) {
        /* Act on the event */
        var scrollPos = $(window).scrollTop(),
            header = $('header');
        //sticky for menu
        if (scrollPos > 300) {
            header.addClass('sticky');
        } else {
            header.removeClass('sticky');
        }
    });
    //back to top js
    var backtotop = $('#back-to-top');
    backtotop.on('click', function (e) {
        e.preventDefault();
        $('html,body').animate({
            scrollTop: 0
        }, 700);
    });

    // scroll down landing page
    var scrolldownlanding = $('#discover-now');
    scrolldownlanding.on('click', function (e) {
        e.preventDefault();
        $('html,body').animate({
            scrollTop: $(document).height() - $(window).height()
        }, 700);
    });

    //sticky sidebar
    if (windowWidth > 1200) {
        var stickySidebar = $('.sticky-sb');
        var mainCt = $('.main-content');
        if (stickySidebar.length > 0) {
            var stickyHeight = stickySidebar.height(),
                sidebarTop = stickySidebar.offset().top;
        }
        // on scroll move the sidebar
        $(window).scroll(function () {
            if (stickySidebar.length > 0) {
                var scrollTop = $(window).scrollTop();

                if (sidebarTop < scrollTop) {
                    stickySidebar.css('top', scrollTop - sidebarTop + 80);

                    // stop the sticky sidebar at the footer to avoid overlapping
                    var sidebarBottom = stickySidebar.offset().top + stickyHeight,
                        stickyStop = mainCt.offset().top + mainCt.height();
                    if (stickyStop < sidebarBottom) {
                        var stopPosition = mainCt.height() - stickyHeight + 130;
                        stickySidebar.css('top', stopPosition);
                    }
                } else {
                    stickySidebar.css('top', '0');
                }
            }
        });
        $(window).resize(function () {
            if (stickySidebar.length > 0) {
                stickyHeight = stickySidebar.height();
            }
        });
    }
    // $(window).on('load',function() {

    // });

});


var form = document.getElementById('profile_image_id')
var profile_image_id = document.getElementById('id_image')
if (profile_image_id) {

    $(profile_image_id).addClass('redbtn')
    profile_image_id.style.width = '228px'
    $('#upload_images label').remove()
    $('#upload_images a').remove()
}

document.querySelector('html').classList.add('js')

$(document).ready(function () {
    $('#id_value').find('label[for=id_value_0]').addClass('thumbs_up')
    $('#id_value').find('label[for=id_value_1]').addClass('thumbs_down')
})

var like_id = document.getElementById('id_value_0')
var dislike_id = document.getElementById('id_value_1')
var vote_arr = [like_id, dislike_id]
var score_count = document.getElementById('score_count')
var both_ids = document.getElementById('like_or_dislike_id')
function like_or_dislike() {
    if (both_ids) {
        var csrf_token = both_ids['csrfmiddlewaretoken'].value
        $(both_ids).change(function () {
            like_data = $(this).serialize()
            $.ajax({
                async: true,
                url: both_ids.action,
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': csrf_token,
                    'vote_data': both_ids.value.value
                },
                success: function (response) {
                    var $vote_status = response.vote_status
                    // score_count.innerHTML = `Score : ${both_ids.value.value}`
                    var created_vote_url = window.location.origin + response.create_vote_url
                    if (both_ids.action == created_vote_url) {
                        window.location.reload()
                        score_count.innerHTML = `Status : ${$vote_status}`
                    }
                    score_count.innerHTML = `Status : ${$vote_status}`
                },
                error: function (error) {
                    alert('something went wrong')
                }
            })
        })
    }
}
like_or_dislike()
function like_or_dislike_checked() {
    $(document).ready(function () {
        if ($('#id_value_0').prop('checked')) {
            $('#id_value_0:checked').parent('label').addClass('green');

        } else if ($('#id_value_1').prop('checked')) {
            $('#id_value_1:checked').parent('label').addClass('red');
        }

        $('#id_value_0').on('click submit', function (event) {
            $this = $(this);
            $label = $this.parent();
            // first make ALL labels normal
            $label.parent().parent().find('label').removeClass('red');
            // then color just THIS one
            if ($('#id_value_0').prop('checked')) {
                $label.addClass('green');
            }
        });
        $('#id_value_1').on('click submit', function (event) {

            $this = $(this);
            $label = $this.parent();
            // first make ALL labels normal
            // $label.parent().parent().find('label').css('color', '');
            $label.parent().parent().find('label').removeClass('green');
            // then color just THIS one
            if ($('#id_value_1').prop('checked')) {
                // $label.css('color','red');
                $label.addClass('red');
            }
        });
    })
}
like_or_dislike_checked()


const star_one = document.getElementById('id_rate_0')
const star_two = document.getElementById('id_rate_1')
const star_three = document.getElementById('id_rate_2')
const star_four = document.getElementById('id_rate_3')
const star_five = document.getElementById('id_rate_4')
const star_rating_form = document.querySelector('.star-rate-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const confirm_Box = document.getElementById('confirm-box')

const arr_rate = [star_one, star_two, star_three, star_four, star_five]



const handleStarSelect = (size) => {
    const children = star_rating_form.children
    for (var i = 0; i < children.length; i++) {
        if (i <= size) {
            children[i].classList.add('star-checked')
        } else {
            children[i].classList.remove('star-checked')
        }
    }
}

const handleSelect = (selection) => {
    switch (selection) {
        case 'id_rate_0': {
            handleStarSelect(1)
            return
        }
        case 'id_rate_1': {
            handleStarSelect(2)
            return;
        }
        case 'id_rate_2': {
            handleStarSelect(3)
            return;
        }
        case 'id_rate_3': {
            handleStarSelect(4)
            return;
        }
        case 'id_rate_4': {
            handleStarSelect(5)
            return;
        }
    }
}

const getNumericValue = (stringValue => {
    let numericValue;
    if (stringValue === 'id_rate_0') {
        numericValue = 1
    } else if (stringValue === 'id_rate_1') {
        numericValue = 2
    } else if (stringValue === 'id_rate_2') {
        numericValue = 3
    } else if (stringValue === 'id_rate_3') {
        numericValue = 4
    } else if (stringValue === 'id_rate_4') {
        numericValue = 5
    } else {
        numericValue = 0
    }
    return numericValue
})



if (star_one) {
    const star_arr = [star_one, star_two, star_three, star_four, star_five]
    star_arr.forEach(item => item.addEventListener('mouseover', (event) => {
        handleSelect(event.target.id)
    }))
    star_arr.forEach(item => item.addEventListener('click', (event) => {
        const val = event.target.id
        let isSubmit = false
        star_rating_form.addEventListener('submit', e => {
            e.preventDefault()
            if (isSubmit) {
                return
            }
            isSubmit = true
            const id_ = e.target.id
            const num_val = getNumericValue(val)
            const show_rate_avg = document.getElementById('rate_avg_id')
            $.ajax({
                async: true,
                type: 'POST',
                url: star_rating_form.action,
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'val_': num_val,
                    'el_id': id_
                },
                success: function (response) {

                    // confirm_Box.innerHTML = `<p>successfully rated with ${num_val}</p>`
                    show_rate_avg.innerHTML = Object.values(response.rate_data)
                    var msg_text = document.getElementById('msg_text')
                    msg_text.innerHTML = `Your Rate => ${num_val}`
                    alert_success_msg()
                },
                error: function (error) {
                    console.log(error)
                    confirm_Box.innerHTML = `<p>something went wrong</p>`
                }
            })
        })
    }))
}
var searchInput = document.getElementById('id_q')
var resultBox = document.getElementById('result_box')
var searchForm = document.getElementById('id_search_form')
var searchLoader = document.getElementById('search_loader')
var viewMore = document.querySelector('#view_more');

$(searchLoader).hide()
if (searchInput) {
    searchInput.addEventListener('keyup', e => {
        $.ajax({
            async: true,
            type: 'GET',
            url: '/search',
            data: {
                'q': searchInput.value
            },

            beforeSend: function () {
                if (searchInput.value.length >= 3) {
                    $(searchLoader).show()
                }
            }
            ,
            success: function (response) {
                $('#view_more_url').attr('href', `${searchForm.action}?q=${searchInput.value}`)
                setTimeout(function () {
                    $(searchLoader).hide()
                    let obj_data = Array.from(response.obj)
                    $(resultBox).children(":not(#view_more)").remove()
                    if (Array.isArray(obj_data)) {
                        resultBox.classList.remove('not-visible')
                        let resultObject = JSON.parse(response.obj)
                        if (searchInput.value.length >= 3) {
                            if (resultObject.length >= 5) {
                                resultBox.innerHTML = viewMore.outerHTML
                                resultBox.innerHTML += response.result_search
                            } else {
                                resultBox.innerHTML = ''
                                resultBox.innerHTML += response.result_search
                            }
                        } else {
                            resultBox.classList.add('not-visible')
                        }
                    }
                }, 300)
            },
            error: function (error) {
                resultBox.innerHTML = 'Something Went Wrong ...'
            }

        })
    })

}

if (searchInput) {

    $(document).on('click', function (e) {
        $(window).on('scroll', function () {
            if ($(window).scrollTop() >= 300) {
                resultBox.classList.add('not-visible')
            }
        })
        if (!(e.target.id === resultBox['id'] || e.target.id === searchInput['id'] || resultBox.contains(e.target))) {
            resultBox.classList.add('not-visible')
        }


    })


    searchInput.addEventListener('keyup', e => {
        if (resultBox.classList.contains('not-visible')) {
            resultBox.classList.remove('not-visible')
        }
        if (searchInput.value.length >= 3) {
            resultBox.classList.add('result_box')
        }
    })
}
var login_link = document.querySelectorAll("[data-open='login_modal']")
var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(0),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return typeof sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
    return false;
};

var is_authenticated_user = null;
var redirect_login = function () {
    $.ajax({
        async: true,
        url: '/accounts/redirect-to-login/',
        type: 'GET',
        data: {},
        success: function (response) {
            is_authenticated_user = response.is_authenticated
        },
        error: function (error) {
        }
    })
    return is_authenticated_user
}()

var login_required_clicks = null;
function login_required() {
    $('a').on('click', function (e) {
        if (!$(e.target).hasClass('allow')) {
            e.stopPropagation()
            e.preventDefault()
            var allLinks = $(this)
            login_required_clicks = $(this)
            var link = $(this).attr('href') || $(this).parent().attr('action')
            $.ajax({
                url: link,
                type: 'GET',
                data: {
                    'link': JSON.stringify(link)
                },
                success: function (response) {
                    if (response.is_authenticated == false) {
                        $(login_link).click()
                        history.pushState(null, null, '?next=' + link)
                    } else {
                        $(allLinks).unbind(e.preventDefault())
                        e.target.click()
                    }
                },
                error: function (error) {
                    console.log(error)
                }
            })
        }
    })

}
login_required()


$(document).ready(function () {
    if (is_authenticated_user == true) {
        $('a').unbind('click')
        if (window.location.search == '?next=' + next_parameter) {
            url_ = document.location.href
            history.pushState(null, null, url_.split('?')[0])
        }
    } else {
        // $(login_required_clicks).unbind('click')
        nex_p = window.location.search
        if (nex_p !== '?next=' + next_parameter) {
        } else {
            $(login_link).click()
        }
    }
})

var error_msg = document.getElementsByClassName('error-msg')
$waiting = $('#waiting')
$(document).ready(function () {
    var $my_form = $('.ajax-form')
    $($my_form.one('click', function () {
        var current_form_id = $(this).attr('id')
        var $current_form = $(this).attr('id', current_form_id)
        var $current_success_box = $current_form.closest('form').find('.success-message')
        var $current_error_box = $current_form.closest('form').find('.error-msg')
        var $current_submit_btn = $current_form.closest('form').find('button')
        $current_form.on('submit', function (event) {
            resetErrors();
            event.preventDefault()
            var $formData = $(this).serialize()
            var $endPoint = $current_form.attr('data-url_root')
            $.ajax({
                async: true,
                type: 'POST',
                url: $endPoint,
                data: $formData,
                success: function (data, textStatus, jqXHR) {
                    $.each(data['form_error'], function (i, v) {
                        var msg = '<label class="error-text" for="' + i + '"><i class="fa fa-times"></i>' + v + '</label>';
                        $('input[name="' + i + '"],select[name="' + i + '"]').addClass('inputTxtError').after(msg)
                    });
                    var keys = Object.keys(data);
                    $('input[name="' + keys[0] + '"]').focus();

                    if (data.form_error === undefined || data.form_error === null) {
                        if (data.redirect_to !== undefined) {
                            $current_success_box.removeClass('not-visible')
                        }
                        $current_success_box[0].innerHTML = data.success
                        $waiting.removeClass('not-visible')

                        setTimeout(function () {
                            if (next_parameter !== null || next_parameter !== undefined) {
                                window.location = data.next_url
                            }
                            if (next_parameter === null || window.location.search === '' || window.location.search === null) {
                                window.location = data.redirect_to

                            }
                            // $waiting.addClass('not-visible')
                        }, 2000)
                    } else {
                        var values_ = Object.values(data.form_error);
                        values_.forEach(function (value) {
                        })
                        // $my_form[0].reset();
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.log('error')
                    if ($current_error_box) {
                        alert_error_msg()
                    }
                }
            })
        })
        // $($current_form).off('click')
    }))
})
function resetErrors() {
    $('form input, form select').removeClass('inputTxtError');
    $('label.error-text').remove();
}



var infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0],
    onBeforePageLoad: function () {
        $('.loading-infinite').show();
    },
    onAfterPageLoad: function ($items) {
        $('.loading-infinite').hide();
    }
});


var favourite_form = document.getElementById('favourite_form')
var fav_heart = document.getElementById('fav_heart')
var msg_text = document.getElementById('msg_text')
var success_msg = document.getElementsByClassName('success-msg')

$(favourite_form).on('click', function (e) {
    e.stopPropagation()
    e.preventDefault()
    $.ajax({
        url: $(favourite_form).attr('action'),
        type: 'POST',
        data: $(this).serialize(),
        success: function (response) {
            if (response.data) {
                $(fav_heart).addClass('fa-heart')
                if (response.data.status === 'Created') {
                    msg_text.innerHTML = response.data.msg
                    $(fav_heart).removeClass('fa-heart-o')
                    $(fav_heart).addClass('fa-heart')
                    alert_success_msg()
                } else if (response.data.status === 'Deleted') {
                    msg_text.innerHTML = response.data.msg
                    $(fav_heart).removeClass('fa-heart')
                    $(fav_heart).addClass('fa-heart-o')
                    alert_success_msg()
                }
            }
        },
        error: function (error) {
            console.log(error)
        }
    })
})

var closebtn = document.getElementsByClassName('closebtn')
function close_btn() {
    $(closebtn).click(function () {
        $(this).parent().addClass('not-visible')
    })
}
function alert_success_msg() {
    close_btn()
    $(success_msg).finish().show().delay(2000).fadeOut()
}
function alert_error_msg() {
    close_btn()
    $(error_msg).finish().show().delay(2000).fadeOut()
}



const openEls = document.querySelectorAll("[data-open]");
const closeEls = document.querySelectorAll("[data-close]");
const isVisible = "is-visible";
var loginWrap = $(".login-wrapper");
var overlay = $(".overlay");
loginWrap.each(function () {
    $(this).wrap('<div class="overlay"></div>')
});
for (const el of openEls) {
    el.addEventListener("click", function () {
        const modalId = this.dataset.open;
        document.getElementById(modalId).classList.add(isVisible);

        var loginct = $(document.getElementById(modalId).lastElementChild.children[0]);
        var other_modal = $(openEls).closest(openEls).not(this)
        $(other_modal).each(function () {
            var other_modalId = this.dataset.open
            var other_modalClass = $(document.getElementById(other_modalId))
            if ($(other_modalClass).children().hasClass('openform')) {
                $(other_modalClass).children().removeClass('openform').delay(500)
            } else {
            }
        })
        event.preventDefault();
        loginct.parents(overlay).addClass("openform");
        $(document).on('click', function (e) {
            var target = $(e.target);

            if ($(target).hasClass("overlay")) {
                $(target).find(loginct).each(function () {
                    $(this).removeClass("openform");
                });
                setTimeout(function () {
                    $(target).removeClass("openform");
                }, 350);
            }
        });
    });

    // });
}
function click_menuToggle() {
    window.location = '/'
    window.onload = function () {
        $('#menuToggle').click()
    }
}

$(document).ready(function () {
    if (window.location.pathname == '/accounts/restore/password/done/') {
        var timeleft = 8
        var timer = setInterval(function () {
            if (timeleft <= 0) {
                clearInterval(timer);
            }
            var countdown = document.getElementById('countdown_id')
            countdown.value = 8 - timeleft;
            timeleft -= 1;
            countdown.innerHTML = 'Redirecting in : ' + timeleft + ' sec'
            if (timeleft === 0) {
                window.location.pathname = '/'
            }
        }, 1000)
    }
})
let type_select = $('#id_type_select');
let select_form = $('.select_form');
let object_list_length = document.getElementById('object_list_count');

var submit_input = document.querySelector('#id_sidebar_filter input[type=submit]')
$(select_form).on('change', (e) => {
    submit_input.removeAttribute('disabled')
})
let form_url = null;
var hashLocation = window.location.hash;
let ajax_side_filter = () => {
    $(select_form).on('submit', function (e) {
        submit_input.setAttribute('disabled', 'disabled')
        e.preventDefault()
        $.ajax({
            async: true,
            url: $(this).attr('data-url'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            beforeSend: function (result, data) {
                return (!(window.location.hash === `#${data.url}`))
            },
            success: function (response) {
                window.history.replaceState(null, null, location.pathname)
                load_content(response);
                pagination(response);
                hashLocation = window.location.hash
            },
            error: function (error) {
                console.log(error)
                object_list_length.innerHTML = 'Error'
                $('.object_list_body').html('<br><h5 class="text-white-2">Something Went Wrong !</h5><br>');
            }
        })
    })
}

ajax_side_filter()



let load_content = (content) => {
    let object_body = document.querySelector('.object_list_body');
    let pagination = document.querySelector('#paginate')
    window.location.hash = content.view_path;
    object_list_length.innerHTML = `Loading  <i class="fa fa-circle-o-notch fa-spin"></i>`;

    object_body.classList.add('not-visible')
    pagination.classList.add('not-visible')

    setTimeout(() => {
        object_body.innerHTML = content.template;
        object_body.classList.remove('not-visible')
        pagination.classList.remove('not-visible')
        object_list_length.innerHTML = content.obj_count;
        submit_input.removeAttribute('disabled')
    }, 1500)
}

let pagination = (response) => {
    document.querySelector('#paginate').innerHTML = response.paginate_template;
    let page_obj = document.querySelectorAll('#page_obj');
    if (page_obj) {
        page_obj.forEach(number => {
            number.addEventListener('click', e => {
                add_page_to_hash(e, response)
            })
            number.addEventListener('auxclick', e => {
                add_page_to_hash(e, response)
            })
        })
    }
};

let add_page_to_hash = (e, response) => {
    e.preventDefault();
    let page_href = e.target.getAttribute('href');
    if (window.location.hash.includes(`page=${response.current_page}`)) {
        window.location.hash = response.view_path.replace(`?page=${response.current_page}&`, `${page_href}&`)
    } else {
        window.location.hash = response.view_path.replace('?', `${page_href}&`);
    }
};

let progressBar = () => {
    let i = 0
    if (i === 0) {
        i = 1;
    }
    let frame = () => {
        if (width >= 100) {
            clearInterval(id_)
            i = 0
        }
        if (width === 100) {
            elements.parentElement.classList.add('not-visible')
        } else {
            width++
            elements.style.width = width + '%'
            elements.setAttribute('data-value', width)
        }
    }
    let elements = document.querySelector('.progress-bar')
    elements.parentElement.classList.remove('not-visible')
    let width = 10;
    let id_ = setInterval(frame, 13);
}

$(window).on('hashchange', () => {
    if (window.location.hash) {
        IndexView.onRouteChange()
        document.querySelector('.object_list_body').parentElement.scrollIntoView({top: 0, behavior: 'smooth'})
    }
})

if (hashLocation !== '') {
    document.addEventListener('DOMContentLoaded', IndexView.init)
}

let popupTrailer = () => {
    let popup_btn = document.querySelector('#popup_trailer_btn')
    let trailer = document.querySelector('.trailer')
    let iframe = document.querySelector('iframe')
    let close_trailer = document.querySelector('.close_video')
    if (popup_btn) {
        popup_btn.addEventListener('click', e => {
            trailer.classList.add('active')
        })
        close_trailer.addEventListener('click', e => {
            trailer.classList.remove('active')
            let iframeSrc = iframe.src
            iframe.src = iframeSrc
        })
    }
}
popupTrailer()


let active = 0;
let timer = 3000;
let slideshow = document.querySelector('.slideshow');
let slides = document.querySelectorAll('.slide');
let points = document.querySelectorAll('.points');
let prev = document.querySelector('.prev');
let next = document.querySelector('.next');

let Switcher = () => {
    slides.forEach(slide => slide.classList.remove('active'))
    points.forEach(point => {
        point.classList.remove('active');
    })
    slides[active].classList.add('active')
    points[active].classList.add('active')
    points[active].scrollIntoView({behavior: 'smooth'})
}

let goNext = () => {
    active = (active == slides.length - 1) ? 0 : active + 1;
    Switcher()
}
let goPrev = () => {
    active = (active == 0) ? slides.length - 1 : active - 1;
    Switcher()
}

points.forEach((point, index) => {
    point.addEventListener('click', e => {
        active = index
        Switcher()
    })
})

if (slideshow) {
    next.addEventListener('click', e => goNext())
    prev.addEventListener('click', e => goPrev())
}

// setInterval(goNext,timer)


let editComment = () => {
    let update_comment_link = document.querySelectorAll('#update_comment');
    let delete_comment_link = document.querySelectorAll('#delete_comment');
    let edit_popup = document.querySelector('#edit_comment_popup');

    // load form in popup
    let loadForm = (e) => {
        e.preventDefault();

        function openModal() {
            $('.hover_bkgr_fricc').show();
            $('.popupCloseButton').on('click', function () {
                $('.hover_bkgr_fricc').hide();
            });
        }

        async function fetch_func() {
            fetch(e.target.parentElement.href, {
                method: 'GET',
                credentials: 'same-origin',
                headers: {'Accept': 'application/json', 'X-Requested-With': 'XMLHttpRequest'}
            }).then(r => r.text()).then(content => {
                edit_popup.innerHTML = content;
            });
            await setTimeout(() => {
                openModal()
            }, 100)
        }

        fetch_func()
    }

    // update comment
    update_comment_link.forEach(update_link => {
        update_link.addEventListener('click', e => loadForm(e))
        update_link.addEventListener('contextmenu', e => e.preventDefault())
        update_link.addEventListener('auxclick', e => e.preventDefault())
    })

    // delete comment
    delete_comment_link.forEach(delete_link => {
        delete_link.addEventListener('click', e => loadForm(e))
        delete_link.addEventListener('contextmenu', e => e.preventDefault())
        delete_link.addEventListener('auxclick', e => e.preventDefault())
    })
}
editComment()


let hideArrowSliders = () => {
    let arrows = document.querySelectorAll('.hide-arrow');
    arrows.forEach(arrow => {
        setTimeout(() => {
            if (arrow.classList.contains('hide-arrow')) {
                document.querySelectorAll('button.slick-arrow').forEach(arr => {
                    arr.classList.add('not-visible')
                })
            }
        }, 0)
    })
}
$(document).on("DOMContentLoaded", hideArrowSliders)
$(document).on("DOMContentLoaded", () => {
    document.querySelectorAll('img').forEach(image => {
        image.setAttribute('loading', 'lazy')
    })
})
