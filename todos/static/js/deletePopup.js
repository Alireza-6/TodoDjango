function openPopup(popupId) {
    document.getElementById(popupId).style.display = 'block';
    document.getElementById(popupId + 'Overlay').style.display = 'block';
}

function closePopup(popupId) {
    document.getElementById(popupId).style.display = 'none';
    document.getElementById(popupId + 'Overlay').style.display = 'none';
}