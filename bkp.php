
add_action('rest_api_init', function () {
    register_rest_route('custom/v1', '/generate-image-id', array(
        'methods' => 'POST',
        'callback' => 'generate_image_id_from_url',
    ));
});

function generate_image_id_from_url($request) {
    $parameters = $request->get_params();
    
    // Check if the URL parameter exists
    if (empty($parameters['url'])) {
        return new WP_Error('missing_url', 'Image URL is required.', array('status' => 400));
    }

    // Fetch the image URL and alt text
    $image_url = $parameters['url'];
    $alt_text = isset($parameters['alt']) ? $parameters['alt'] : '';

    // Check if the image exists in the media library
    $attachment_id = attachment_url_to_postid($image_url);

    if ($attachment_id) {
        // Image already exists, return its ID
        return $attachment_id;
    } else {
        // Image doesn't exist, create it
        $attachment_id = wp_insert_attachment(array(
            'post_title'     => sanitize_file_name(basename($image_url)),
            'post_mime_type' => 'image/jpeg', // Adjust mime type based on your image type
            'post_status'    => 'inherit',
            'post_content'   => $alt_text,
            'guid'           => $image_url,
        ), $image_url);

        // Generate attachment metadata
        $attach_data = wp_generate_attachment_metadata($attachment_id, $image_url);
        wp_update_attachment_metadata($attachment_id, $attach_data);

        return $attachment_id;
    }
}