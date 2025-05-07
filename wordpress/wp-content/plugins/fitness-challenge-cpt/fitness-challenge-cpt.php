<?php
/*
Plugin Name: Fitness Challenge Custom Post Type
Description: A custom post type for fitness challenges.
Version: 1.0
Author: Zachary Duncan
*/

function register_fitness_challenges_cpt() {
    register_post_type('fitness_challenge', array(
        'labels' => array(
            'name' => 'Fitness Challenges',
            'singular_name' => 'Fitness Challenge',
            'add_new' => 'Add New',
            'add_new_item' => 'Add New Fitness Challenge',
            'edit_item' => 'Edit Fitness Challenge',
            'new_item' => 'New Fitness Challenge',
            'view_item' => 'View Fitness Challenge',
            'all_items' => 'All Fitness Challenges',
            'search_items' => 'Search Fitness Challenges',
            'not_found' => 'No Fitness Challenges Found',
            'not_found_in_trash' => 'No Fitness Challenges Found in Trash',
            'menu_name' => 'Fitness Challenges',
        ),
        'public' => true,
        'has_archive' => true, // Enable archive page
        'show_in_rest' => true, // Enable REST API for access
        'supports' => array('title', 'editor', 'custom-fields', 'thumbnail'), // What to support (title, content, etc.)
        'rewrite' => array('slug' => 'fitness-challenges'), // URL slugs
    ));
}
add_action('init', 'register_fitness_challenges_cpt');
