 function googleTranslateElementInit() {
            new google.translate.TranslateElement(
                {pageLanguage: 'en'},
                'google_translate_element'
            );
        } 
        function translatePage(lang) {
            if (lang === "") return;

            var combo = document.querySelector(".goog-te-combo");
            if (combo) {
                combo.value = lang;
                combo.dispatchEvent(new Event("change"));
            } else {
                alert("Translate element not loaded yet. Please wait.");
    }
}
