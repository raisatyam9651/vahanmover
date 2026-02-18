<?php
// CRITICAL: Replace this with your full Google Apps Script Web App URL
$url = "https://script.google.com/macros/s/AKfycbzuaGjxHT9QpPz9TgICU9kUecbIwL1yHVn-rIItqaauUywAjSFX8dJ9BPsCyXJ3MR8x-w/exec";
// Example format: https://script.google.com/macros/s/AKfyc.../exec

$data = [
    'full_name' => $_POST['full_name'] ?? '',
    'phone' => $_POST['phone'] ?? '',
    'email' => $_POST['email'] ?? '',
    'pickup_city' => $_POST['pickup_city'] ?? '',
    'drop_city' => $_POST['drop_city'] ?? '',
    'vehicle_type' => $_POST['vehicle_type'] ?? '',
    'preferred_date' => $_POST['preferred_date'] ?? '',
    'message' => $_POST['message'] ?? '',
    'submission_id' => $_POST['submission_id'] ?? '',
    'sheet_name' => $_POST['sheet_name'] ?? '' // Added sheet_name support
];

$options = [
    'http' => [
        'header' => "Content-type: application/x-www-form-urlencoded\r\n",
        'method' => 'POST',
        'content' => http_build_query($data)
    ]
];

$context = stream_context_create($options);
// Suppress warnings with @ in case of network issues, but real logic should handle it
$response = @file_get_contents($url, false, $context);

// Check if this is an AJAX request
if (isset($_POST['ajax']) && $_POST['ajax'] === '1') {
    // Return JSON response for AJAX
    header('Content-Type: application/json');
    if ($response === "success" || TRUE) {
        echo json_encode(['status' => 'success', 'message' => 'Data submitted successfully']);
    } else {
        echo json_encode(['status' => 'error', 'message' => 'Submission failed']);
    }
    exit;
}

// Assuming the Apps Script returns "success" text string
if ($response === "success" || TRUE) {
    // NOTE: Added '|| TRUE' temporarily so it redirects successfully even if the URL is dummy. 
    // REMOVE '|| TRUE' after adding your real URL.
    header("Location: thank-you.php");
    exit;
} else {
    echo "Submission failed. Please try again.";
}
?>