$(document).ready(function() {
    // Inicializar DataTables en la tabla con el ID consultas-table
    $('#consultas-table').DataTable({
        "paging": true,         // Activa la paginación
        "searching": true,      // Activa la barra de búsqueda
        "ordering": true,       // Activa el ordenamiento de columnas
        "info": true,           // Muestra información sobre la tabla
        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.11.5/i18n/Spanish.json" // Traducción al español
        },
        "responsive": true       // Hace la tabla responsiva en Bootstrap 5
    });

    $('.delete-form').on('submit', function(event){
        event.preventDefault();  // Evita el envío del formulario de manera predeterminada

        var form = $(this);
        var consultaId = form.data('id');
        var url = "{% url 'borrar_consulta' 'consulta_id_placeholder' %}".replace('consulta_id_placeholder', consultaId);
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();

        if(confirm("¿Estás seguro de que deseas eliminar esta consulta?")) {
            $.ajax({
                url: url,
                type: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken  // Asegura que se envíe el CSRF token
                },
                success: function(response) {
                    // Eliminar la fila de la tabla correspondiente a la consulta
                    $('#consulta-' + consultaId).remove();
                    alert('Consulta eliminada correctamente.');
                },
                error: function(xhr, status, error) {
                    alert('Hubo un error al intentar eliminar la consulta.');
                }
            });
        }
    });
});
$(document).ready(function() {
    // Manejo del evento de eliminación con AJAX
    $('.borrar-form').on('submit', function(e) {
        e.preventDefault();
        const form = $(this);
        const rowId = form.closest('tr').attr('id');
        
        $.ajax({
            url: form.attr('action'),
            type: 'POST',
            data: form.serialize(),
            success: function(response) {
                if (response.status === 'success') {
                    $('#' + rowId).fadeOut(300, function() {
                        $(this).remove();
                    });
                } else {
                    alert('Hubo un problema al eliminar la consulta.');
                }
            },
            error: function(xhr) {
                alert('Hubo un problema al eliminar la consulta.');
            }
        });
    });

    // Manejo del evento de actualización con AJAX
    $('.actualizar-form').on('submit', function(e) {
        e.preventDefault();
        const form = $(this);
        
        $.ajax({
            url: form.attr('action'),
            type: 'POST',
            data: form.serialize(),
            success: function(response) {
                if (response.status === 'success') {
                    alert('Estado actualizado correctamente.');
                } else {
                    alert('Hubo un problema al actualizar el estado.');
                }
            },
            error: function(xhr) {
                alert('Hubo un problema al actualizar el estado.');
            }
        });
    });
});
