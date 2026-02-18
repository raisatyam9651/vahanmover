function doPost(e) {
    try {
        // 1. Get the Spreadsheet
        var ss = SpreadsheetApp.getActiveSpreadsheet();
        var sheet;

        // 2. Check if a specific sheet name is provided (e.g., "Cal")
        if (e.parameter.sheet_name) {
            sheet = ss.getSheetByName(e.parameter.sheet_name);

            // If the sheet doesn't exist, create it to avoid losing data
            if (!sheet) {
                sheet = ss.insertSheet(e.parameter.sheet_name);
                // Add headers for the new sheet
                sheet.appendRow(["Full Name", "Phone", "Email", "Pickup City", "Drop City", "Vehicle Type", "Preferred Date", "Message", "Submission ID", "Timestamp"]);
            }
        } else {
            // Fallback to "Sheet1" or active sheet for other forms that don't specify a sheet
            sheet = ss.getSheetByName("Sheet1") || ss.getActiveSheet();
        }

        // 3. Extract data passed from PHP
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
        var timestamp = new Date();

        // 5. Append row to Google Sheet
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

        // 6. Return success message
        return ContentService.createTextOutput("success");

    } catch (error) {
        return ContentService.createTextOutput("error: " + error.toString());
    }
}
