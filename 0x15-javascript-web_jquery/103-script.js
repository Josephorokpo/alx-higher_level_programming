$(document).ready(function() {
            function fetchTranslation() {
                var languageCode = $('input#language_code').val();

                $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode, function(data) {
                    $('div#hello').text(data.hello);
                });
            }

            $('input#btn_translate').click(fetchTranslation);

            $('input#language_code').keypress(function(event) {
                if (event.which === 13) {
                    fetchTranslation();
                }
            });
        });
