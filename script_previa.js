let previewContainer = document.querySelector('.products-preview');
let previewBoxes = previewContainer.querySelectorAll('.preview');

document.querySelectorAll('.ver-mas').forEach(link => {
    link.addEventListener('click', () => {
        let target = link.getAttribute('data-name');
        previewContainer.style.display = 'flex';
        previewBoxes.forEach(preview => {
            if (preview.getAttribute('data-target') === target) {
                preview.classList.add('active');
            }
        });
    });
});

previewBoxes.forEach(preview => {
    preview.querySelector('.fa-times').addEventListener('click', () => {
        preview.classList.remove('active');
        previewContainer.style.display = 'none';
    });
});

window.addEventListener('click', (event) => {
    if (event.target === previewContainer) {
        previewBoxes.forEach(preview => {
            preview.classList.remove('active');
        });
        previewContainer.style.display = 'none';
    }
});