setInterval(
async function myTest() {
    let test = await eel.test_simconnect()();
    document.getElementById("altitude").textContent = test;
}, 3000)