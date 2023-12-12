const slider = document.getElementById('render-factor-slider');
const renderFactorValue = document.getElementById('render-factor-value');

slider.addEventListener('input', function() {
    renderFactorValue.textContent = slider.value;
});

slider.addEventListener('change', function() {
    // Make an AJAX request to update render_factor on the server
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/update_render_factor', true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Optionally handle success
            console.log('Render factor updated successfully');
        } else {
            // Optionally handle errors
            console.error('Failed to update render factor');
        }
    };
    xhr.send(JSON.stringify({ render_factor: parseInt(slider.value) }));
});

const resubmitButton = document.getElementById('resubmit-button');

resubmitButton.addEventListener('click', function() {
    // Submit the form to trigger image colorization with the new render_factor
    document.getElementById('colorize-form').submit();
});