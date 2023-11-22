let closeButton = document.querySelector('.alert .close');

// Добавьте прослушиватель событий клика к кнопке закрытия
closeButton.addEventListener('click', function () {
    // Получить родительский элемент кнопки закрытия (поле оповещения)
    let alertBox = this.parentElement;

    // Скрыть окно оповещения
    alertBox.style.display = 'none';
});