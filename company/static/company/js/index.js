function updateClock() {
    let now = new Date();
    let hours = String(now.getHours()).padStart(2, '0');
    let minutes = String(now.getMinutes()).padStart(2, '0');
    let seconds = String(now.getSeconds()).padStart(2, '0');
    let timeString = hours + ':' + minutes + ':' + seconds;
    document.getElementById('clock').innerHTML = timeString;
}

setInterval(updateClock, 1000)

function updateDate() {
    let now = new Date();
    let day = now.getDate();
    let month = String(now.getMonth() + 1).padStart(2, '0');
    let year = String(now.getFullYear()).padStart(2, '0');
    let dateString = day + '.' + month + '.' + year;
    document.getElementById('date').innerHTML = dateString;
}

// setInterval(updateDate, 1000);
window.onload = function() {
  updateDate();
};