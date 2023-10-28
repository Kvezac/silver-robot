document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const alert = bootstrap.Alert.getOrCreateInstance('#top-alert');
        alert.close();
    }, 5000);
});
