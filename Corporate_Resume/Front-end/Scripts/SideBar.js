// Checks if document is ready
$(document).ready(function () {

    // Click event on sidebar collapse button
    $('#sidebarCollapse').on('click', function () {

        // Toggle active class for sidebar
        $('#sidebar').toggleClass('active');
    });
});