function main(splash, args)
    -- Cambiar user agent (Opción 1)
    --splash: set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    -- Cambiar user agent (Opción 2)
    --[[
        headers = {
        ['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        splash: set_custom_headers(headers)
            --]]

    -- Cambiar user agent (Opción 3)
    splash: on_request(function(request)
    request: set_header('User-Agent',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
    end)

    -- Si un sitio web no se visualiza correctamente, desactivar el modo privado puede ayudar.
    -- Private mode es el equivalente a usar una ventana en Incognito en Google
    splash.private_mode_enabled = false
    -- Ir a la URL establecida en el navegador splash y luego esperar 3 segundos para que la página se renderice.
    assert(splash:go(args.url))
    assert(splash:wait(3))
    -- Selecciona todos los elementos que tengan el selector css "label.btn.btn-sm.btn-primary"
    all_matches = assert(splash:select_all("label.btn.btn-sm.btn-primary"))
    -- Se han seleccionado dos elementos. Queremos hacer clic en el segundo botón, a continuación, espere 3 segundos para que la página de renderizado
    all_matches[2]: mouse_click()
    assert (splash:wait(3))
    -- Aumentar la ventana gráfica para que todo el contenido sea visible.
    splash: set_viewport_full()
    return {splash: png(), splash: html()}
end