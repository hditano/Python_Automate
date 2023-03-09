setInterval(
async function myTest() {
    let data = await eel.test_simconnect()();
    document.getElementById("altitude").textContent = 'Altitude: ' + Math.trunc(data['altitude']);
    document.getElementById('speed').textContent = 'Speed: ' + Math.trunc(data['speed']);
    document.getElementById('latitude').textContent = 'Latitude: ' + data['latitude'];
    document.getElementById('longitude').textContent = 'Longitude: ' + data['longitude'];
    
}, 3000)


function myMap() {
    document.getElementById('google').src = document.getElementById('google').src
    console.log('iframe reloaded')
}