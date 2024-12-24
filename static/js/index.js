function obtenerHora() {
    fetch('http://worldtimeapi.org/api/timezone/Europe/Madrid')
        .then(response => response.json())
        .then(data => {
            const dateTime = new Date(data.datetime);

            const horaElemento = document.getElementById('hora_andalucía');

            horaElemento.textContent = `Fecha/Hora Andalucía: ${dateTime.toLocaleString()}`;
        })
        .catch(error => {
            const horaElemento = document.getElementById('hora_andalucía');
            horaElemento.textContent = 'No se pudo obtener la hora.';
            console.error('Error al obtener la hora:', error);
        });
}

setInterval(obtenerHora, 1000);

obtenerHora();
