

var hc=0;

function disp()
{
    
    e=document.getElementById("mm");
    if(hc==0)
    {
    e.style.display="block";
    hc=1;
    }
    else{
        e.style.display="none";
        hc=0; 
    }
}

var fc=0;
function disp1()
{
    e=document.getElementById("ff");
    if (fc==0)
    {
    e.style.display="block";
    fc=1;
    }
    else{
        e.style.display="none";
        hc=0;
    }
}

var cr=0;
function disp2()
{
    
    e=document.getElementById("cc");
    if(cr==0)
    {
    e.style.display="block";
    cr=1;
    }
    else{
        e.style.display="none";
        cr=0;
    }
}

/* question part*/ 
// Fetch all details element
const details = Array.from(document.querySelectorAll("details"));

// Add onclick listeners
details.forEach(targetDetail => {
  targetDetail.addEventListener("click", () => {
    // Close all details that are not targetDetail
    details.forEach(detail => {
      if (detail !== targetDetail) {
        detail.removeAttribute("open");
      }
    });
  });
});

/* partner section*/ 

$(document).ready(function(){
    $('.customer-logos').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1500,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 4
            }
        }, {
            breakpoint: 520,
            settings: {
                slidesToShow: 3
            }
        }]
    });
});



