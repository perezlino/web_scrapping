-- website -> https://www.adamchoi.co.uk/overs/detailed

function main(splash, args)
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