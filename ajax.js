function cargarArchivo(archivo) {
    $.ajax({
        type: "GET",
        url: archivo,
        success: function(data) {
            $("#contenido").html(data);
        }
    });
}