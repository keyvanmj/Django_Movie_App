$(window).on("load",function(){var e=$("#status"),t=$("#preloader"),o=$("body");e.fadeOut(),t.delay(650).fadeOut("fast"),o.delay(650).css({overflow:"visible"});for(var i=document.getElementsByTagName("iframe"),n=0;n<i.length;n++)i[n].getAttribute("data-src")&&i[n].setAttribute("src",i[n].getAttribute("data-src"))}),$(function(){"use strict";var e=$(window).width();e>1024?$(".dropdown").hover(function(){$(this).children(".dropdown-menu").fadeIn(300)},function(){$(this).children(".dropdown-menu").fadeOut(300)}):$(".navbar a.dropdown-toggle").on("click",function(e){var t=$(this),o=$(this).offsetParent(".dropdown-menu"),i=$(".nav li.open");return $(this).parent("li").toggleClass("open"),o.parent().hasClass("nav")||t.next().css({top:t[0].offsetTop,left:o.outerWidth()-4}),i.not($(this).parents("li")).removeClass("open"),!1});$("#nav-icon1").on("click",function(){$(this).toggleClass("open")});var t=$('.tabs .tab-links input[type="radio"]+label,.tabs .tab-links a, .tab-links-2 input[type="radio"]+label,.tab-links-2 a, .tab-links-3 input[type="radio"]+label ,.tab-links-3 a'),o=$(".slick-multiItem"),i=$(".slick-multiItem2");t.on("click",function(e){var t=$(this).attr("href")||$(this).attr("data-url_root");$(".tabs "+t).show().siblings().hide(),$(this).parent("li").addClass("active").siblings().removeClass("active"),e.preventDefault(),o.slick("setPosition"),i.slick("setPosition")}),function(e,t){var o=document.getElementById(e);if(null!=o){var i=o.querySelector(".days"),n=o.querySelector(".hours"),r=o.querySelector(".minutes"),s=o.querySelector(".seconds"),a=function(){var e=function(e){var t=Date.parse(e)-Date.parse(new Date),o=Math.floor(t/1e3%60),i=Math.floor(t/1e3/60%60),n=Math.floor(t/36e5%24);return{total:t,days:Math.floor(t/864e5),hours:n,minutes:i,seconds:o}}(t);i.innerHTML=e.days,n.innerHTML=("0"+e.hours).slice(-2),r.innerHTML=("0"+e.minutes).slice(-2),s.innerHTML=("0"+e.seconds).slice(-2),e.total<=0&&clearInterval(l)};a();var l=setInterval(a,1e3)}}("clockdiv",new Date(Date.parse(new Date)+216e7));var n=jQuery(".tweet");jQuery(n).each(function(e,t){var o=jQuery(this).attr("id");twttr.widgets.createTweet(o,t,{conversation:"none",cards:"hidden",linkColor:"default",theme:"light"})}),i.slick({infinite:!0,slidesToShow:6,slidesToScroll:6,arrows:!1,dots:!0,responsive:[{breakpoint:1200,settings:{slidesToShow:3,slidesToScroll:3,infinite:!0,dots:!0}},{breakpoint:768,settings:{slidesToShow:3,slidesToScroll:3}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1}}]}),o.slick({infinite:!0,slidesToShow:4,slidesToScroll:4,arrows:!1,draggable:!0,dots:!0,responsive:[{breakpoint:1024,settings:{slidesToShow:3,slidesToScroll:3,infinite:!0,dots:!0}},{breakpoint:768,settings:{slidesToShow:2,slidesToScroll:2}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1}}]}),$(".slick-multiItemSlider").slick({infinite:!0,slidesToShow:4,slidesToScroll:4,arrows:!1,draggable:!0,autoplay:!0,autoplaySpeed:2e3,dots:!0,responsive:[{breakpoint:1024,settings:{slidesToShow:3,slidesToScroll:3,infinite:!0,dots:!0}},{breakpoint:768,settings:{slidesToShow:2,slidesToScroll:2}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1}}]}),$(".slider-single-item").slick({infinite:!0,slidesToShow:1,slidesToScroll:1,arrows:!0,dots:!0,draggable:!0,responsive:[{breakpoint:1024,settings:{slidesToShow:1,slidesToScroll:1,infinite:!0,dots:!0,arrows:!0}},{breakpoint:768,settings:{slidesToShow:1,slidesToScroll:1}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1,arrows:!1}}]}),$(".slick-tw").slick({infinite:!0,slidesToShow:1,slidesToScroll:1,dots:!0,draggable:!0,arrows:!1,responsive:[{breakpoint:1024,settings:{slidesToShow:1,slidesToScroll:1,infinite:!0,dots:!0,arrows:!1}},{breakpoint:768,settings:{slidesToShow:1,slidesToScroll:1}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1,arrows:!1}}]});var r=$(".slider-for"),s=$(".slider-nav");r.slick({slidesToShow:1,slidesToScroll:1,arrows:!1,fade:!0,asNavFor:".slider-nav"}),s.slick({slidesToShow:5,slidesToScroll:1,asNavFor:".slider-for",dots:!0,focusOnSelect:!0,responsive:[{breakpoint:1024,settings:{slidesToShow:3,slidesToScroll:3,infinite:!0,arrows:!0}},{breakpoint:768,settings:{slidesToShow:3,slidesToScroll:3}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1,arrows:!0}}]});var a=$(".slider-for-2"),l=$(".slider-nav-2");a.slick({slidesToShow:1,slidesToScroll:1,arrows:!1,fade:!0,asNavFor:".slider-nav-2"}),l.slick({slidesToShow:3,slidesToScroll:1,asNavFor:".slider-for-2",dots:!1,arrows:!0,focusOnSelect:!0,vertical:!0});var c=$(".fancybox-media");c.fancybox({openEffect:"float",closeEffect:"none",helpers:{media:{},overlay:{locked:!1}}}),c.attr("rel","playlist").fancybox({openEffect:"none",closeEffect:"none",prevEffect:"none",nextEffect:"none",helpers:{media:{}},youtube:{autoplay:1,hd:1,wmode:"opaque",vq:"hd720"}});var d=$(".img-lightbox");d.fancybox({helpers:{title:{type:"float"},overlay:{locked:!1}}}),d.fancybox({afterShow:function(){var e,t,o=this.group.length;this.index==o-1?(e=d.eq(0).attr("title"),t=d.eq(this.index-1).attr("title")):0==this.index?(e=d.eq(this.index+1).attr("title"),t=d.eq(o-1).attr("title")):(e=d.eq(this.index+1).attr("title"),t=d.eq(this.index-1).attr("title"));var i=$(".img-lightbox-next"),n=$(".img-lightbox-prev");i.attr("title",e),n.attr("title",t)}}),$(".close").on("click",function(e){e.preventDefault(),$(".overlay").removeClass("openform")});var u=$(".ui.fluid.dropdown");if(u.dropdown({allowLabels:!0}),u.dropdown({"set selected":"Role1,Role2"}),$(window).scroll(function(e){var t=$(window).scrollTop(),o=$("header");t>300?o.addClass("sticky"):o.removeClass("sticky")}),$("#back-to-top").on("click",function(e){e.preventDefault(),$("html,body").animate({scrollTop:0},700)}),$("#discover-now").on("click",function(e){e.preventDefault(),$("html,body").animate({scrollTop:$(document).height()-$(window).height()},700)}),e>1200){var h=$(".sticky-sb"),m=$(".main-content");if(h.length>0)var f=h.height(),_=h.offset().top;$(window).scroll(function(){if(h.length>0){var e=$(window).scrollTop();if(_<e){h.css("top",e-_+80);var t=h.offset().top+f;if(m.offset().top+m.height()<t){var o=m.height()-f+130;h.css("top",o)}}else h.css("top","0")}}),$(window).resize(function(){h.length>0&&(f=h.height())})}});var form=document.getElementById("profile_image_id"),profile_image_id=document.getElementById("id_image");profile_image_id&&($(profile_image_id).addClass("redbtn"),profile_image_id.style.width="228px",$("#upload_images label").remove(),$("#upload_images a").remove()),document.querySelector("html").classList.add("js"),$(document).ready(function(){$("#id_value").find("label[for=id_value_0]").addClass("thumbs_up"),$("#id_value").find("label[for=id_value_1]").addClass("thumbs_down")});var like_id=document.getElementById("id_value_0"),dislike_id=document.getElementById("id_value_1"),vote_arr=[like_id,dislike_id],score_count=document.getElementById("score_count"),both_ids=document.getElementById("like_or_dislike_id");function like_or_dislike(){if(both_ids){var e=both_ids.csrfmiddlewaretoken.value;$(both_ids).change(function(){like_data=$(this).serialize(),$.ajax({async:!0,url:both_ids.action,type:"POST",data:{csrfmiddlewaretoken:e,vote_data:both_ids.value.value},success:function(e){var t=e.vote_status,o=window.location.origin+e.create_vote_url;both_ids.action==o&&(window.location.reload(),score_count.innerHTML=`Status : ${t}`),score_count.innerHTML=`Status : ${t}`},error:function(e){alert("something went wrong")}})})}}function like_or_dislike_checked(){$(document).ready(function(){$("#id_value_0").prop("checked")?$("#id_value_0:checked").parent("label").addClass("green"):$("#id_value_1").prop("checked")&&$("#id_value_1:checked").parent("label").addClass("red"),$("#id_value_0").on("click submit",function(e){$this=$(this),$label=$this.parent(),$label.parent().parent().find("label").removeClass("red"),$("#id_value_0").prop("checked")&&$label.addClass("green")}),$("#id_value_1").on("click submit",function(e){$this=$(this),$label=$this.parent(),$label.parent().parent().find("label").removeClass("green"),$("#id_value_1").prop("checked")&&$label.addClass("red")})})}like_or_dislike(),like_or_dislike_checked();const star_one=document.getElementById("id_rate_0"),star_two=document.getElementById("id_rate_1"),star_three=document.getElementById("id_rate_2"),star_four=document.getElementById("id_rate_3"),star_five=document.getElementById("id_rate_4"),star_rating_form=document.querySelector(".star-rate-form"),csrf=document.getElementsByName("csrfmiddlewaretoken"),confirm_Box=document.getElementById("confirm-box"),arr_rate=[star_one,star_two,star_three,star_four,star_five],handleStarSelect=e=>{const t=star_rating_form.children;for(var o=0;o<t.length;o++)o<=e?t[o].classList.add("star-checked"):t[o].classList.remove("star-checked")},handleSelect=e=>{switch(e){case"id_rate_0":return void handleStarSelect(1);case"id_rate_1":return void handleStarSelect(2);case"id_rate_2":return void handleStarSelect(3);case"id_rate_3":return void handleStarSelect(4);case"id_rate_4":return void handleStarSelect(5)}},getNumericValue=e=>{let t;return t="id_rate_0"===e?1:"id_rate_1"===e?2:"id_rate_2"===e?3:"id_rate_3"===e?4:"id_rate_4"===e?5:0};if(star_one){const e=[star_one,star_two,star_three,star_four,star_five];e.forEach(e=>e.addEventListener("mouseover",e=>{handleSelect(e.target.id)})),e.forEach(e=>e.addEventListener("click",e=>{const t=e.target.id;let o=!1;star_rating_form.addEventListener("submit",e=>{if(e.preventDefault(),o)return;o=!0;const i=e.target.id,n=getNumericValue(t),r=document.getElementById("rate_avg_id");$.ajax({async:!0,type:"POST",url:star_rating_form.action,data:{csrfmiddlewaretoken:csrf[0].value,val_:n,el_id:i},success:function(e){r.innerHTML=Object.values(e.rate_data),document.getElementById("msg_text").innerHTML=`Your Rate => ${n}`,alert_success_msg()},error:function(e){console.log(e),confirm_Box.innerHTML="<p>something went wrong</p>"}})})}))}var searchInput=document.getElementById("id_q"),resultBox=document.getElementById("result_box"),searchForm=document.getElementById("id_search_form"),searchLoader=document.getElementById("search_loader"),viewMore=document.querySelector("#view_more");$(searchLoader).hide(),searchInput&&searchInput.addEventListener("keyup",e=>{$.ajax({async:!0,type:"GET",url:"/search",data:{q:searchInput.value},beforeSend:function(){searchInput.value.length>=3&&$(searchLoader).show()},success:function(e){$("#view_more_url").attr("href",`${searchForm.action}?q=${searchInput.value}`),setTimeout(function(){$(searchLoader).hide();let t=Array.from(e.obj);if($(resultBox).children(":not(#view_more)").remove(),Array.isArray(t)){resultBox.classList.remove("not-visible");let t=JSON.parse(e.obj);searchInput.value.length>=3?t.length>=5?(resultBox.innerHTML=viewMore.outerHTML,resultBox.innerHTML+=e.result_search):(resultBox.innerHTML="",resultBox.innerHTML+=e.result_search):resultBox.classList.add("not-visible")}},300)},error:function(e){resultBox.innerHTML="Something Went Wrong ..."}})}),searchInput&&($(document).on("click",function(e){$(window).on("scroll",function(){$(window).scrollTop()>=300&&resultBox.classList.add("not-visible")}),e.target.id===resultBox.id||e.target.id===searchInput.id||resultBox.contains(e.target)||resultBox.classList.add("not-visible")}),searchInput.addEventListener("keyup",e=>{resultBox.classList.contains("not-visible")&&resultBox.classList.remove("not-visible"),searchInput.value.length>=3&&resultBox.classList.add("result_box")}));var login_link=document.querySelectorAll("[data-open='login_modal']"),getUrlParameter=function(e){var t,o,i=window.location.search.substring(0).split("&");for(o=0;o<i.length;o++)if((t=i[o].split("="))[0]===e)return void 0===typeof t[1]||decodeURIComponent(t[1]);return!1},is_authenticated_user=null,redirect_login=($.ajax({async:!0,url:"/accounts/redirect-to-login/",type:"GET",data:{},success:function(e){is_authenticated_user=e.is_authenticated},error:function(e){}}),is_authenticated_user),login_required_clicks=null;function login_required(){$("a").on("click",function(e){if(!$(e.target).hasClass("allow")){e.stopPropagation(),e.preventDefault();var t=$(this);login_required_clicks=$(this);var o=$(this).attr("href")||$(this).parent().attr("action");$.ajax({url:o,type:"GET",data:{link:JSON.stringify(o)},success:function(i){0==i.is_authenticated?($(login_link).click(),history.pushState(null,null,"?next="+o)):($(t).unbind(e.preventDefault()),e.target.click())},error:function(e){console.log(e)}})}})}login_required(),$(document).ready(function(){1==is_authenticated_user?($("a").unbind("click"),window.location.search=="?next="+next_parameter&&(url_=document.location.href,history.pushState(null,null,url_.split("?")[0]))):(nex_p=window.location.search,nex_p!=="?next="+next_parameter||$(login_link).click())});var error_msg=document.getElementsByClassName("error-msg");function resetErrors(){$("form input, form select").removeClass("inputTxtError"),$("label.error-text").remove()}$waiting=$("#waiting"),$(document).ready(function(){var e=$(".ajax-form");$(e.one("click",function(){var e=$(this).attr("id"),t=$(this).attr("id",e),o=t.closest("form").find(".success-message"),i=t.closest("form").find(".error-msg");t.closest("form").find("button");t.on("submit",function(e){resetErrors(),e.preventDefault();var n=$(this).serialize(),r=t.attr("data-url_root");$.ajax({async:!0,type:"POST",url:r,data:n,success:function(e,t,i){$.each(e.form_error,function(e,t){var o='<label class="error-text" for="'+e+'"><i class="fa fa-times"></i>'+t+"</label>";$('input[name="'+e+'"],select[name="'+e+'"]').addClass("inputTxtError").after(o)});var n=Object.keys(e);($('input[name="'+n[0]+'"]').focus(),void 0===e.form_error||null===e.form_error)?(void 0!==e.redirect_to&&o.removeClass("not-visible"),o[0].innerHTML=e.success,$waiting.removeClass("not-visible"),setTimeout(function(){null===next_parameter&&void 0===next_parameter||(window.location=e.next_url),null!==next_parameter&&""!==window.location.search&&null!==window.location.search||(window.location=e.redirect_to)},2e3)):Object.values(e.form_error).forEach(function(e){})},error:function(e,t,o){console.log("error"),i&&alert_error_msg()}})})}))});var infinite=new Waypoint.Infinite({element:$(".infinite-container")[0],onBeforePageLoad:function(){$(".loading-infinite").show()},onAfterPageLoad:function(e){$(".loading-infinite").hide()}}),favourite_form=document.getElementById("favourite_form"),fav_heart=document.getElementById("fav_heart"),msg_text=document.getElementById("msg_text"),success_msg=document.getElementsByClassName("success-msg");$(favourite_form).on("click",function(e){e.stopPropagation(),e.preventDefault(),$.ajax({url:$(favourite_form).attr("action"),type:"POST",data:$(this).serialize(),success:function(e){e.data&&($(fav_heart).addClass("fa-heart"),"Created"===e.data.status?(msg_text.innerHTML=e.data.msg,$(fav_heart).removeClass("fa-heart-o"),$(fav_heart).addClass("fa-heart"),alert_success_msg()):"Deleted"===e.data.status&&(msg_text.innerHTML=e.data.msg,$(fav_heart).removeClass("fa-heart"),$(fav_heart).addClass("fa-heart-o"),alert_success_msg()))},error:function(e){console.log(e)}})});var closebtn=document.getElementsByClassName("closebtn");function close_btn(){$(closebtn).click(function(){$(this).parent().addClass("not-visible")})}function alert_success_msg(){close_btn(),$(success_msg).finish().show().delay(2e3).fadeOut()}function alert_error_msg(){close_btn(),$(error_msg).finish().show().delay(2e3).fadeOut()}const openEls=document.querySelectorAll("[data-open]"),closeEls=document.querySelectorAll("[data-close]"),isVisible="is-visible";var loginWrap=$(".login-wrapper"),overlay=$(".overlay");loginWrap.each(function(){$(this).wrap('<div class="overlay"></div>')});for(const e of openEls)e.addEventListener("click",function(){const e=this.dataset.open;document.getElementById(e).classList.add(isVisible);var t=$(document.getElementById(e).lastElementChild.children[0]),o=$(openEls).closest(openEls).not(this);$(o).each(function(){var e=this.dataset.open,t=$(document.getElementById(e));$(t).children().hasClass("openform")&&$(t).children().removeClass("openform").delay(500)}),event.preventDefault(),t.parents(overlay).addClass("openform"),$(document).on("click",function(e){var o=$(e.target);$(o).hasClass("overlay")&&($(o).find(t).each(function(){$(this).removeClass("openform")}),setTimeout(function(){$(o).removeClass("openform")},350))})});function click_menuToggle(){window.location="/",window.onload=function(){$("#menuToggle").click()}}$(document).ready(function(){if("/accounts/restore/password/done/"==window.location.pathname)var e=8,t=setInterval(function(){e<=0&&clearInterval(t);var o=document.getElementById("countdown_id");o.value=8-e,e-=1,o.innerHTML="Redirecting in : "+e+" sec",0===e&&(window.location.pathname="/")},1e3)});let type_select=$("#id_type_select"),select_form=$(".select_form"),object_list_length=document.getElementById("object_list_count");var submit_input=document.querySelector("#id_sidebar_filter input[type=submit]");$(select_form).on("change",e=>{submit_input.removeAttribute("disabled")});let form_url=null;var hashLocation=window.location.hash;let ajax_side_filter=()=>{$(select_form).on("submit",function(e){submit_input.setAttribute("disabled","disabled"),e.preventDefault(),$.ajax({async:!0,url:$(this).attr("data-url"),type:$(this).attr("method"),data:$(this).serialize(),beforeSend:function(e,t){return!(window.location.hash===`#${t.url}`)},success:function(e){window.history.replaceState(null,null,location.pathname),load_content(e),pagination(e),hashLocation=window.location.hash},error:function(e){console.log(e),object_list_length.innerHTML="Error",$(".object_list_body").html('<br><h5 class="text-white-2">Something Went Wrong !</h5><br>')}})})};ajax_side_filter();let load_content=e=>{let t=document.querySelector(".object_list_body"),o=document.querySelector("#paginate");window.location.hash=e.view_path,object_list_length.innerHTML='Loading  <i class="fa fa-circle-o-notch fa-spin"></i>',t.classList.add("not-visible"),o.classList.add("not-visible"),setTimeout(()=>{t.innerHTML=e.template,t.classList.remove("not-visible"),o.classList.remove("not-visible"),object_list_length.innerHTML=e.obj_count,submit_input.removeAttribute("disabled")},1500)},pagination=e=>{document.querySelector("#paginate").innerHTML=e.paginate_template;let t=document.querySelectorAll("#page_obj");t&&t.forEach(t=>{t.addEventListener("click",t=>{add_page_to_hash(t,e)}),t.addEventListener("auxclick",t=>{add_page_to_hash(t,e)})})},add_page_to_hash=(e,t)=>{e.preventDefault();let o=e.target.getAttribute("href");window.location.hash.includes(`page=${t.current_page}`)?window.location.hash=t.view_path.replace(`?page=${t.current_page}&`,`${o}&`):window.location.hash=t.view_path.replace("?",`${o}&`)},progressBar=()=>{let e=0;0===e&&(e=1);let t=document.querySelector(".progress-bar");t.parentElement.classList.remove("not-visible");let o=10,i=setInterval(()=>{o>=100&&(clearInterval(i),e=0),100===o?t.parentElement.classList.add("not-visible"):(o++,t.style.width=o+"%",t.setAttribute("data-value",o))},13)};$(window).on("hashchange",()=>{window.location.hash&&(IndexView.onRouteChange(),document.querySelector(".object_list_body").parentElement.scrollIntoView({top:0,behavior:"smooth"}))}),""!==hashLocation&&document.addEventListener("DOMContentLoaded",IndexView.init);let popupTrailer=()=>{let e=document.querySelector("#popup_trailer_btn"),t=document.querySelector(".trailer"),o=document.querySelector("iframe"),i=document.querySelector(".close_video");e&&(e.addEventListener("click",e=>{t.classList.add("active")}),i.addEventListener("click",e=>{t.classList.remove("active");let i=o.src;o.src=i}))};popupTrailer();let active=0,timer=3e3,slideshow=document.querySelector(".slideshow"),slides=document.querySelectorAll(".slide"),points=document.querySelectorAll(".points"),prev=document.querySelector(".prev"),next=document.querySelector(".next"),Switcher=()=>{slides.forEach(e=>e.classList.remove("active")),points.forEach(e=>{e.classList.remove("active")}),slides[active].classList.add("active"),points[active].classList.add("active"),points[active].scrollIntoView({behavior:"smooth"})},goNext=()=>{active=active==slides.length-1?0:active+1,Switcher()},goPrev=()=>{active=0==active?slides.length-1:active-1,Switcher()};points.forEach((e,t)=>{e.addEventListener("click",e=>{active=t,Switcher()})}),slideshow&&(next.addEventListener("click",e=>goNext()),prev.addEventListener("click",e=>goPrev()));let editComment=()=>{let e=document.querySelectorAll("#update_comment"),t=document.querySelectorAll("#delete_comment"),o=document.querySelector("#edit_comment_popup"),i=e=>{e.preventDefault(),async function(){fetch(e.target.parentElement.href,{method:"GET",credentials:"same-origin",headers:{Accept:"application/json","X-Requested-With":"XMLHttpRequest"}}).then(e=>e.text()).then(e=>{o.innerHTML=e}),await setTimeout(()=>{$(".hover_bkgr_fricc").show(),$(".popupCloseButton").on("click",function(){$(".hover_bkgr_fricc").hide()})},100)}()};e.forEach(e=>{e.addEventListener("click",e=>i(e)),e.addEventListener("contextmenu",e=>e.preventDefault()),e.addEventListener("auxclick",e=>e.preventDefault())}),t.forEach(e=>{e.addEventListener("click",e=>i(e)),e.addEventListener("contextmenu",e=>e.preventDefault()),e.addEventListener("auxclick",e=>e.preventDefault())})};editComment();let hideArrowSliders=()=>{document.querySelectorAll(".hide-arrow").forEach(e=>{setTimeout(()=>{e.classList.contains("hide-arrow")&&document.querySelectorAll("button.slick-arrow").forEach(e=>{e.classList.add("not-visible")})},0)})};$(document).on("DOMContentLoaded",hideArrowSliders),$(document).on("DOMContentLoaded",()=>{document.querySelectorAll("img").forEach(e=>{e.setAttribute("loading","lazy")})});