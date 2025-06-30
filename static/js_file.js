   
const menu = document.getElementById("languageMenu");
   function scrollLeftMenu(){
        menu.scrollBy({ left: -150, behavior: "smooth" });
    }
    function scrollRightMenu() {
        menu.scrollBy({ left: 150, behavior: "smooth" }); /* Scroll right */
    } 
 

    
 function showOverlay(index, name, details) {
        document.getElementById("overlay").style.display = "flex";
        document.getElementById("crop-name").innerText = name;
        document.getElementById("crop-description").innerHTML = details;
    }
    
function hideOverlay() {
        document.getElementById("overlay").style.display = "none";
    }
function searchTasks(){
        let input = document.getElementById("search-input").value.toLowerCase();
        let cropItems = document.getElementsByClassName("crop-item"); 
        for(let i = 0; i < cropItems.length; i++){
            let cropName = cropItems[i].getElementsByTagName("p")[0].innerText.toLowerCase(); // Get crop name

            if (cropName.includes(input)) {
                cropItems[i].style.display = "block";
            } 
            else {
                cropItems[i].style.display = "none";
                }
                }
        }
function searchmessages() {
    let input = document.getElementById("search-message").value.toLowerCase();
    let messages = document.getElementsByClassName("entry"); 

    for (let i = 0; i < messages.length; i++) {
        let paragraph = messages[i].getElementsByTagName("p")[0];
        let dateTime = messages[i].getElementsByTagName("span")[0];

        let content = paragraph.innerText.toLowerCase();
        let dateText = dateTime ? dateTime.innerText.toLowerCase() : "";

        if (content.includes(input) || dateText.includes(input)) {
            messages[i].style.display = "block";
        } else {
            messages[i].style.display = "none";
        }
    }
}

            function viewhome(){
                document.getElementById('organic_farming').style.display = 'none';
                document.getElementById('Community_container').style.display = 'none';
                let aboutus_div = document.getElementById('aboutus_container');
                aboutus_div.style.display = 'block';
                aboutus_div.style.animation = 'fadeIn 1.5s ease-in-out';

                scrollToElementWithOffset('aboutus_container', 100);
            }

            function viewOrganicFarming(){
                document.getElementById('aboutus_container').style.display = 'none';
                document.getElementById('Community_container').style.display = 'none';
                let organic_farming = document.getElementById('organic_farming');
                organic_farming.style.display = 'block';
                organic_farming.style.animation = 'fadeIn 1.5s ease-in-out';

                scrollToElementWithOffset('organic_farming', 100);
            }

            function viewcommunity(){
                document.getElementById('aboutus_container').style.display = 'none';
                document.getElementById('organic_farming').style.display = 'none';
                let community_div = document.getElementById('Community_container');
                community_div.style.display = 'block';
                community_div.style.animation = 'fadeIn 1.5s ease-in-out';

                scrollToElementWithOffset('community_div', 100);
            }

            function scrollToElementWithOffset(elementId, offset = 100) {
                const element = document.getElementById(elementId);
                if (element) {
                    const elementPosition = element.getBoundingClientRect().top + window.scrollY;
                    window.scrollTo({ top: elementPosition - offset, behavior: "smooth" });
                }
    }


   /*----  window.addEventListener('load', setScrollMenuTop);
            window.addEventListener('resize', setScrollMenuTop);

            function setScrollMenuTop() {
                const header = document.getElementById('languageMenu');
                const scrollmenu = document.querySelector('.scrollmenu');
                const headerHeight = header.offsetHeight;
                scrollmenu.style.top = `${headerHeight}px`;


                const bg = document.querySelector('.background_image');
                const bgtop = scrollmenu.offsetHeight + header.offsetHeight;
                 document.documentElement.style.setProperty('--bg-top', `${totalTop}px`);
            }
                */