app.config(($httpProvider) ->
    getCookie = (name) ->
        for cookie in document.cookie.split ';' when cookie and 
        name is (cookie.trim().split '=')[0]
            return decodeURIComponent cookie.trim()[(1 + name.length)...]
        null
    $httpProvider.defaults.headers.common['X-CSRFToken'] = getCookie("csrftoken")
)