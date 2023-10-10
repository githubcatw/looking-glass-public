
// Logs the passed message, either on screen or to the console.
function log(message) {
    // Get the visible log text
    var logMessage = document.getElementById("logMessage");
    // If it doesn't exist, print the message to the console
    if (logMessage == undefined) {
        console.log(message)
    }
    // Else:
    else {
        // Get the current text
        var logText = logMessage.innerHTML;
        // Break it into an array of lines
        var lines = logText.split('<br>');
        // Add the log message to the start of that array
        lines.unshift(message);
        // If there are more than 7 lines, remove the last one
        if (lines.length > 7) {
            lines.pop();
        }
        // Join the array back into a single string
        var newtext = lines.join('\n');
        // Show it on the log text, replacing new lines with HTML break tags
        logMessage.innerHTML = newtext.replaceAll("\n", "<br>");
    }
}