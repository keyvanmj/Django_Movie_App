const IndexView = {
    init: function () {
        window.addEventListener('load', () => {
            IndexView.onRouteChange()
        });
    },
    onRouteChange: function () {
        const hashLocation = window.location.hash.substring(1);
        IndexView.loadContent(hashLocation);
    },
    loadContent: function (uri) {
        const contentUri = `${uri}`;
        fetch(contentUri).then(r => r.text()).then(content => IndexView.updateSlot(content));
    },
    updateSlot: function (content) {
        try {
            let content_object = JSON.parse(content);
            if (content_object.obj_count !== undefined && content_object.template !== undefined) {
                progressBar()
                load_content(content_object);
                pagination(content_object);
                document.querySelector('#id_sidebar_filter select').parentElement.innerHTML = content_object.form;
            } else {
                let regex = /[0-9]/;
                if (regex.test(window.location.hash)) {
                    window.location.hash = window.location.hash.replace(`page=${regex.exec(window.location.hash)}&`, '')
                } else {
                    object_list_length.innerHTML = 'Nothing Found'
                    $('.object_list_body').html('<br><h5 class="text-white-2"> NO RESULT FOUND ...</h5><br>');
                }
            }
        } catch (e) {
            object_list_length.innerHTML = 'Error'
            $('.object_list_body').html('<br><h5 class="text-white-2">Something Went Wrong !</h5><br>');
        }
    }
}
