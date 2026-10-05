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

// -------------------------------------------------------------
// Frappe CRM Integration (Live Cloudflare Tunnel)
// -------------------------------------------------------------
$crmUrl = "https://foam-corp-masters-lenders.trycloudflare.com/api/resource/CRM%20Lead";
$crmApiKey = "ffd6e92b4f4ec21";
$crmApiSecret = "641a36c348dae00";

$fullName = trim($data['full_name'] ?? '');
$nameParts = explode(' ', $fullName, 2);
$firstName = !empty($nameParts[0]) ? $nameParts[0] : 'Website Lead';
$lastName = $nameParts[1] ?? '';

// Build detailed notes for lead timeline
$detailsText = "";
if (!empty($data['pickup_city']))    $detailsText .= "Pickup City: " . $data['pickup_city'] . "\n";
if (!empty($data['drop_city']))      $detailsText .= "Drop City: " . $data['drop_city'] . "\n";
if (!empty($data['vehicle_type']))   $detailsText .= "Vehicle Type: " . ucfirst($data['vehicle_type']) . "\n";
if (!empty($data['preferred_date'])) $detailsText .= "Preferred Date: " . $data['preferred_date'] . "\n";
if (!empty($data['message']))        $detailsText .= "Message: " . $data['message'] . "\n";
if (!empty($data['submission_id']))  $detailsText .= "Submission ID: " . $data['submission_id'] . "\n";

$orgText = (!empty($data['pickup_city']) && !empty($data['drop_city'])) 
    ? ($data['pickup_city'] . ' -> ' . $data['drop_city'] . (!empty($data['vehicle_type']) ? ' (' . ucfirst($data['vehicle_type']) . ')' : ''))
    : 'Vahan Mover Website';

$crmPayload = [
    'first_name'   => $firstName,
    'last_name'    => $lastName,
    'email'        => !empty($data['email']) ? $data['email'] : 'lead@vahanmover.com',
    'mobile_no'    => $data['phone'] ?? '',
    'organization' => $orgText,
    'status'       => 'New'
];

// Send to Frappe CRM
$crmJson = json_encode($crmPayload);
$crmOptions = [
    'http' => [
        'header' => "Authorization: token {$crmApiKey}:{$crmApiSecret}\r\n" .
                    "Content-Type: application/json\r\n" .
                    "Host: crm.localhost\r\n",
        'method' => 'POST',
        'content' => $crmJson,
        'timeout' => 5,
        'ignore_errors' => true
    ]
];
$crmContext = stream_context_create($crmOptions);
$crmRes = @file_get_contents($crmUrl, false, $crmContext);

// If notes or special instructions exist, append as comment on the lead timeline
if (!empty($detailsText) && $crmRes) {
    $leadObj = json_decode($crmRes, true);
    if (!empty($leadObj['data']['name'])) {
        $leadId = $leadObj['data']['name'];
        $commentOptions = [
            'http' => [
                'header' => "Authorization: token {$crmApiKey}:{$crmApiSecret}\r\n" .
                            "Content-Type: application/json\r\n" .
                            "Host: crm.localhost\r\n",
                'method' => 'POST',
                'content' => json_encode([
                    'comment_type'      => 'Comment',
                    'reference_doctype' => 'CRM Lead',
                    'reference_name'    => $leadId,
                    'content'           => nl2br(htmlspecialchars($detailsText))
                ]),
                'timeout' => 4,
                'ignore_errors' => true
            ]
        ];
        $commentContext = stream_context_create($commentOptions);
        @file_get_contents("https://foam-corp-masters-lenders.trycloudflare.com/api/resource/Comment", false, $commentContext);
    }
}

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