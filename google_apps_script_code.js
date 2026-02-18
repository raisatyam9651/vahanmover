function doPost(e) {
    try {
        // 1. Get the Spreadsheet
        var ss = SpreadsheetApp.getActiveSpreadsheet();
        var sheet;

        // 2. Check if a specific sheet name is provided
        if (e.parameter.sheet_name) {
            sheet = ss.getSheetByName(e.parameter.sheet_name);

            // If the sheet doesn't exist, create it (optional, but good for safety)
            if (!sheet) {
                sheet = ss.insertSheet(e.parameter.sheet_name);
                // Add headers to new sheet if created
                sheet.appendRow(["Full Name", "Phone", "Email", "Pickup City", "Drop City", "Vehicle Type", "Preferred Date", "Message", "Submission ID", "Timestamp"]);
            }
        } else {
            // Fallback to the active sheet (default behavior for existing forms)
            sheet = ss.getActiveSheet();
        }

        // 3. Extract data passed from PHP (x-www-form-urlencoded)
        var p = e.parameter;

        var fullName = p.full_name;
        var phone = p.phone;
        var email = p.email;
        var pickupCity = p.pickup_city;
        var dropCity = p.drop_city;
        var vehicleType = p.vehicle_type;
        var preferredDate = p.preferred_date;
        var message = p.message;
        var submissionId = p.submission_id;

        // 4. Create regular timestamp
        var timestamp = new Date(); // Current date and time

        // 5. Append row to Google Sheet
        // Order: [Name, Phone, Email, Pickup, Drop, Vehicle, Date, Message, ID, Timestamp]
        sheet.appendRow([
            fullName,
            phone,
            email,
            pickupCity,
            dropCity,
            vehicleType,
            preferredDate,
            message,
            submissionId,
            timestamp
        ]);

        // 6. Return success message to PHP
        return ContentService.createTextOutput("success");

    } catch (error) {
        // Return error message if something fails
        return ContentService.createTextOutput("error: " + error.toString());
    }
}
