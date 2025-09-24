$(function () {
    console.log("Page is ready")

    // Javascript
    // Attach an event listener to entire document for the 'mousedown' event
    // On elements with the class 'game-button'
    $(document).on("mousedown", ".game-button", function (event) {

        // Get value of clicked button
        var buttonNumber = $(this).val();

        // Use a switch statement to check with mouse button was clicked
        switch (event.which) {

            // Left mouse button
            case 1:

                // Log the button number to console
                console.log("Button number " + buttonNumber + " was left clicked");

                // Call function 'doButtonUpdate' with button number and
                // Specific endpoint 
                doButtonUpdate(buttonNumber, 'button/ShowOneButton');
                break;

            // Middle mouse button
            case 2:
                alert("Middle mouse button clicked");
                break;

            // Right mouse click
            case 3:

                // Log the button number to console
                console.log("Button number " + buttonNumber + " was RIGHT clicked");

                // Call function 'doButtonUpdate' with button number and
                // Specific endpoint 
                doButtonUpdate(buttonNumber, 'button/RightClickShowOneButton');
                break;
            default:
                alert("Nothing was clicked.");
        }
    });

    // Bind new event to context menu to prevent right click menu from appearing
    // Whenever context menu shows up, call function
    $(document).bind("contextmenu", function (event) {

        // Stop right click menu from showing up
        event.preventDefault();
        console.log("Right Click. Prevented context menu");
    });

    // Define the function 'doButtonUpdate'; takes two parameters: 'buttonNumber' and 'urlString'
    function doButtonUpdate(buttonNumber, urlString) {

        // Make an AJAX request using jquery
        $.ajax({

            // Set expected data type to 'json' for response
            datatype: "json",

            // Use POST method for request
            method: "POST",

            // Set url for request using value passed in
            url: urlString,

            // Send data to server, specifically 'buttonNumber' as key value pair
            data: { "buttonNumber": buttonNumber },

            // Define callback function to handle successful response
            success: function (data) {

                // Log response to console
                console.log(data);

                // Update HTML content of element with ID
                $("#" + buttonNumber).html(data);
            }
        });
    }
}); 