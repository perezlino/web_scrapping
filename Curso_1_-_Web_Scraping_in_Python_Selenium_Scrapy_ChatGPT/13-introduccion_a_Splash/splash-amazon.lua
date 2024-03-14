-- website: https://www.amazon.com/

function main(splash, args)
    -- Establecer la url
    url = args.url
    -- Ir a la url y esperar 2 segundos para que la página se muestre correctamente
    assert (splash:go(url))
    assert (splash:wait(1))

    -- Seleccione el text box con el selector css "#twotabsearchtextbox"
    input_box = assert(splash:select("#twotabsearchtextbox"))
    -- No podemos asumir que el elemento que queremos estará enfocado así que usamos ":focus()"
    input_box:focus()
    -- Enviamos el texto y esperamos 1 segundo para que la página se renderice correctamente (puedes añadir más tiempo si es necesario)
    input_box:send_text("books")
    assert(splash:wait(1))

    -- Seleccionamos el botón de búsqueda con el selector css "#nav-search-submit-button", pulsamos sobre él y esperamos 5 segundos
    button = assert(splash:select("#nav-search-submit-button"))
    button:mouse_click()
    assert(splash:wait(5))
    return {
        html = splash:html(),
        png = splash:png(),
    }
end