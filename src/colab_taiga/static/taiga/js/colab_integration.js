/* Make sure to clear the broser's local storage,
 * otherwise the user will remain logged on Taiga */
$(document.body).on('click', 'a[href="/account/logout"]', function() {
    localStorage.clear();
});
