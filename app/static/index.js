function logout() {
    const xhr = new XMLHttpRequest();
    xhr.onload = () => {
        location.href = location.href;
    }
    xhr.open('POST', '/api/logout');
    xhr.send();
}

