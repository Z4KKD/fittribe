<?php
/**
 * Twenty Twenty-Two functions and definitions
 *
 * @link https://developer.wordpress.org/themes/basics/theme-functions/
 *
 * @package WordPress
 * @subpackage Twenty_Twenty_Two
 * @since Twenty Twenty-Two 1.0
 */

if ( ! function_exists( 'twentytwentytwo_support' ) ) :

	/**
	 * Sets up theme defaults and registers support for various WordPress features.
	 *
	 * @since Twenty Twenty-Two 1.0
	 *
	 * @return void
	 */
	function twentytwentytwo_support() {

		// Add support for block styles.
		add_theme_support( 'wp-block-styles' );

		// Enqueue editor styles.
		add_editor_style( 'style.css' );
	}

endif;

add_action( 'after_setup_theme', 'twentytwentytwo_support' );

if ( ! function_exists( 'twentytwentytwo_styles' ) ) :

	/**
	 * Enqueue styles.
	 *
	 * @since Twenty Twenty-Two 1.0
	 *
	 * @return void
	 */
	function twentytwentytwo_styles() {
		// Register theme stylesheet.
		$theme_version = wp_get_theme()->get( 'Version' );

		$version_string = is_string( $theme_version ) ? $theme_version : false;
		wp_register_style(
			'twentytwentytwo-style',
			get_template_directory_uri() . '/style.css',
			array(),
			$version_string
		);

		// Enqueue theme stylesheet.
		wp_enqueue_style( 'twentytwentytwo-style' );
	}

endif;

add_action( 'wp_enqueue_scripts', 'twentytwentytwo_styles' );

// Add block patterns.
require get_template_directory() . '/inc/block-patterns.php';

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

