document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        timeZone: 'America/Bogota',
        initialView: 'dayGridMonth',
        events: eventsJsonData,
        eventContent: function(arg) {

            // Creamos un elemento para el título del evento
            var titleElement = document.createElement('div');
            titleElement.style.color = arg.event.backgroundColor; // Usa el color de fondo del evento
            titleElement.style.fontWeight = 'bold'; // Aplica negrita
            titleElement.innerText = arg.event.title;
            

            // Creamos un elemento para el nombre del usuario
            var userElement = document.createElement('div');
            userElement.style.color = arg.event.backgroundColor; // Usa el color de fondo del evento
            userElement.style.fontWeight = 'bold'; // Aplica negrita
            userElement.innerText = "Usuario: " + arg.event.extendedProps.username;


            // Creamos un contenedor para los elementos
            var arrayOfDomNodes = [titleElement, userElement]

            return { domNodes: arrayOfDomNodes };
        },
        eventClick: function(info) {
            // Evita que FullCalendar trate de navegar
            info.jsEvent.preventDefault();
            // Si el evento tiene una URL, abre esa URL
            if (info.event.url) {
                window.open(info.event.url, "_self");
            }
        },
    });
    calendar.render();
    calendar.setOption('locale','es')
});
