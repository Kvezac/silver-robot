$(document).ready(function () {
    $('#unassigned-profile').change(function () {
        let profileId = $(this).val();
        $.ajax({
            url: '/get-levels/',
            type: 'GET',
            data: {profile_id: profileId},
            success: function (data) {
                // Populate the "level" dropdown with the data received
            }
        });
    });

    $('#level').change(function () {
        let levelId = $(this).val();
        $.ajax({
            url: '/get-bosses/',
            type: 'GET',
            data: {level_id: levelId},
            success: function (data) {
                // Populate the "boss" dropdown with the data received
            }
        });
    });

    $('#employee-form').submit(function (e) {
        e.preventDefault();
        let formData = $(this).serialize();
        $.ajax({
            url: '/save-employee/',
            type: 'POST',
            data: formData,
            success: function (data) {

            }
        });
    });
});